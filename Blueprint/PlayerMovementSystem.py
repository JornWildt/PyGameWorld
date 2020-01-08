import pygame
from Physics.PhysicsComponent import PhysicsComponent
from Physics.BodyComponent import BodyComponent
from Blueprint.PlayerMovementComponent import PlayerMovementComponent

class PlayerMovementSystem:
    def __init__(self, message_bus):
        message_bus.subscribe('tile_collision', PlayerMovementSystem.on_tile_collision)

    
    def on_tile_collision(p):
        entity = p[0]
        tile = p[1]

        # Make sure we react to player collisions only
        player = entity.get_component_of_type(PlayerMovementComponent)
        if player == None:
            return

        # Extract relevant componts from entity
        body = entity.get_component_of_type(BodyComponent)
        phys = entity.get_component_of_type(PhysicsComponent)

        # If hitting a map tile, backup to previous position
        if tile.tile_type.is_blocking:
            body.position = phys.previous_position


    def update(self, game_environment):
        maxv = 0.2
        max_directions = 40
        directions = ((0,-1), (0.7,-0.7), (1,0), (0.7,0.7), (0,1), (-0.7,0.7), (-1,0), (-0.7,-0.7))

        # Calcuate movement intention
        rotate_intent = None
        speed_intent = 'Stop'

        pressed_keys = pygame.key.get_pressed()
        
        if (pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_q]):
            rotate_intent = 'Left'
        elif (pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_w]):
            rotate_intent = 'Right'
        
        if (pressed_keys[pygame.K_UP]):
            speed_intent = 'Forward'
        elif (pressed_keys[pygame.K_DOWN]):
            speed_intent = 'Backward'
        else:
            speed_intent = 'Stop'

        # Go through all player components (only one, seems like a bit of overkill ...)
        for (pos,phys,mov) in game_environment.entities_repository.get_components_of_types(BodyComponent, PhysicsComponent, PlayerMovementComponent):

            # acc = 0.1
            # xdiff = mov.intended_velocity[0] - phys.velocity[0]
            # ydiff = mov.intended_velocity[1] - phys.velocity[1]
            # phys.acceleration = (
            #     max(-acc,min(acc, xdiff)),
            #     max(-acc,min(acc, ydiff)),
            #     0
            # )

            # if phys.velocity[0] > maxv or phys.velocity[0] < -maxv or phys.velocity[1] > maxv or phys.velocity[1] < -maxv or phys.velocity[2] > maxv or phys.velocity[2] < -maxv:
            #     phys.acceleration = (0,0,0)
            #     phys.velocity = (max(-maxv,min(maxv, phys.velocity[0])), min(maxv, phys.velocity[1]), min(maxv, phys.velocity[2]))
            if speed_intent == 'Forward':
                mov.intended_velocity = 0.1
                # mov.intended_velocity = (0.0, -0.1, 0.0)
            elif speed_intent == 'Backward':
                mov.intended_velocity = -0.05
                #mov.intended_direction = (mov.intended_direction + max_directions/2) % max_directions
                #mov.intended_velocity = (0.0, 0.1, 0.0)
            elif speed_intent == 'Stop':
                mov.intended_velocity = 0
                #mov.intended_velocity = (0.0, 0.0, 0.0)

            if rotate_intent == 'Left':
                mov.intended_direction = (mov.intended_direction - 1) % max_directions
                #mov.intended_velocity = (-0.1, 0.0, 0.0)
            elif rotate_intent == 'Right':
                mov.intended_direction = (mov.intended_direction + 1) % max_directions
                #mov.intended_velocity = (0.1, 0.0, 0.0)
                #phys.acceleration = (0.01,0.01,0.0)
            else:
                pass
                #mov.intended_velocity = 0
                #mov.intended_velocity = (0.0, 0.0, 0.0)

            phys.velocity = (
                mov.intended_velocity * directions[int(mov.intended_direction/5)][0],
                mov.intended_velocity * directions[int(mov.intended_direction/5)][1],
                0)


import pygame
from Physics.PhysicsComponent import PhysicsComponent
from Physics.BodyComponent import BodyComponent
from Blueprint.PlayerMovementComponent import PlayerMovementComponent
from Rendering.SpriteComponent import SpriteComponent

class PlayerMovementSystem:
    def __init__(self, message_bus):
        self.last_direction = 0
        message_bus.subscribe('tile_collision', PlayerMovementSystem.on_tile_collision)
        message_bus.subscribe('set_player_position', PlayerMovementSystem.on_set_player_position)

    direction_vectors = [
        (0,-1),
        (0.71,-0.71),
        (1,0),
        (0.71,0.71),
        (0,1),
        (-0.71,0.71),
        (-1,0),
        (-0.71,-0.71)
    ]
    
    def on_tile_collision(game_environment, p):
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
            player.hit_tile = tile


    def update(self, game_environment):
        (vector, speed, direction) = PlayerMovementSystem.get_current_input_vector()

        # Go through all player components (these is only one, so it seems like a bit of overkill ...)
        for (player, body, phys, sprite) in game_environment.entities_repository.get_components_of_types(PlayerMovementComponent, BodyComponent, PhysicsComponent, SpriteComponent):

            if direction != None and player.hit_tile != None:
                # Directional vector towards the hit tile
                tile_vector = (player.hit_tile.position[0] - body.position[0], player.hit_tile.position[1] - body.position[1])
                
                # Cross-product of intended movement and tile direction indicates their relationship
                c = vector[0] * tile_vector[1] - vector[1] * tile_vector[0]

                # c < 0 means tile is to the left of the intended movement direction, so turn right
                if c < 0:
                    direction = (direction + 1) % 8
                else:
                    direction = (direction - 1) % 8

                # Now update intended movement vector to the new direction
                vector = (PlayerMovementSystem.direction_vectors[direction][0] * speed, PlayerMovementSystem.direction_vectors[direction][1] * speed)
                player.hit_tile = None

            phys.velocity = (
                vector[0],
                vector[1],
                0)

            if pygame.key.get_pressed()[pygame.K_SPACE]:
                phys.velocity = (0,0,0)
                body.position = (1,1,1)
            
            if direction != None:
                self.last_direction = direction

            # Sprite images are for no specific reason shiftet 4 positions in the sprite file
            sprite_direction = (self.last_direction+4) % 8

            # Select the appropriate sprite for the direction
            sprite.sprite_id = 'player_' + str(sprite_direction)


    def get_current_input_vector():
        pressed_keys = pygame.key.get_pressed()
        
        vector = (0,0)
        direction = None

        if pressed_keys[pygame.K_LEFT] and pressed_keys[pygame.K_UP]:
            direction = 7
        elif pressed_keys[pygame.K_UP] and pressed_keys[pygame.K_RIGHT]:
            direction = 1
        elif pressed_keys[pygame.K_RIGHT] and pressed_keys[pygame.K_DOWN]:
            direction = 3
        elif pressed_keys[pygame.K_DOWN] and pressed_keys[pygame.K_LEFT]:
            direction = 5
        elif pressed_keys[pygame.K_LEFT]:
            direction = 6
        elif pressed_keys[pygame.K_UP]:
            direction = 0
        elif pressed_keys[pygame.K_RIGHT]:
            direction = 2
        elif pressed_keys[pygame.K_DOWN]:
            direction = 4

        speed = 0.25 if pressed_keys[pygame.K_LSHIFT] else 0.1

        if direction != None:
            direction = (direction + 1) % 8
            vector = (PlayerMovementSystem.direction_vectors[direction][0] * speed, PlayerMovementSystem.direction_vectors[direction][1] * speed)
        else:
            vector = (0,0)

        return (vector, speed, direction)
        

    def on_set_player_position(game_environment, msg):
        body = game_environment.player_entity.get_component_of_type(BodyComponent)
        phys = game_environment.player_entity.get_component_of_type(PhysicsComponent)
        phys.velocity = (0,0,0)
        body.position = msg.position
        


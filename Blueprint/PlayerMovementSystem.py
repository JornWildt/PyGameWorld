import pygame
from Core.Physics.PhysicsComponent import PhysicsComponent
from Core.Physics.BodyComponent import BodyComponent
from Core.Rendering.SpriteComponent import SpriteComponent
from Blueprint.PlayerMovementComponent import PlayerMovementComponent

class PlayerMovementSystem:
    def __init__(self, message_bus):
        self.last_direction = 0
        message_bus.subscribe('tile_collision', PlayerMovementSystem.on_tile_collision)
        message_bus.subscribe('body_collision', PlayerMovementSystem.on_body_collision)
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
            body.position = body.previous_position
            body.velocity = (0,0,0)
            player.hit_tile = tile

    def on_body_collision(game_environment, p):
        entity = p[0]
        hitBody = p[1]
        collisionNormal = p[2]

        # Make sure we react to player collisions only
        player = entity.get_component_of_type(PlayerMovementComponent)
        if player == None:
            return

        hitEntity = hitBody.entity
        hitPhys = hitEntity.get_component_of_type(PhysicsComponent)

        # Extract relevant componts from entity
        playerBody = entity.get_component_of_type(BodyComponent)
        playerPhys = entity.get_component_of_type(PhysicsComponent)

        relVelocity = (hitPhys.velocity[0] - playerPhys.velocity[0], hitPhys.velocity[1] - playerPhys.velocity[1], hitPhys.velocity[2] - playerPhys.velocity[2])

        dot = relVelocity[0] * collisionNormal[0] + relVelocity[1] * collisionNormal[1] + relVelocity[2] * collisionNormal[2]
        totalVelocity = 1.2 * dot

        playerVelocityChange = (totalVelocity * collisionNormal[0], totalVelocity * collisionNormal[1], totalVelocity * collisionNormal[2])

        #playerBody.position = playerBody.previous_position
        playerBody.position = (playerBody.position[0] + playerVelocityChange[0], playerBody.position[1] + playerVelocityChange[1], playerBody.position[2] + playerVelocityChange[2])
        #playerPhys.velocity = (playerPhys.velocity[0] + playerVelocityChange[0], playerPhys.velocity[1] + playerVelocityChange[1], playerPhys.velocity[2] + playerVelocityChange[2])


    def update(self, game_environment):
        pressed_keys = pygame.key.get_pressed()

        (vector, speed, direction) = PlayerMovementSystem.get_current_input_vector(pressed_keys)

        # Go through all player components (there is only one, so it seems like a bit of overkill ...)
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
                vector = (PlayerMovementSystem.direction_vectors[direction][0] * speed, PlayerMovementSystem.direction_vectors[direction][1] * speed, 0)

                player.hit_tile = None

            if pressed_keys[pygame.K_SPACE] and body.is_grounded:
                phys.velocity = (vector[0], vector[1], 0.4)
                phys.acceleration = (0.0, 0.0, 0.0)
            elif body.is_grounded:
                phys.velocity = (vector[0], vector[1], 0.0)
                phys.acceleration = (0,0,0)
            else:
                phys.velocity = (vector[0], vector[1], phys.velocity[2])
                phys.acceleration = (0,0,-0.05)

            if isinstance(body.ground_item, BodyComponent):
                ground_phys = body.ground_item.entity.get_component_of_type(PhysicsComponent)
                phys.velocity = (phys.velocity[0] + ground_phys.velocity[0], phys.velocity[1] + ground_phys.velocity[1], phys.velocity[2] + ground_phys.velocity[2])

            # if pygame.key.get_pressed()[pygame.K_0]:
            #     phys.velocity = (0,0,0)
            #     body.position = (1,1,1)

            if direction != None:
                self.last_direction = direction

            # Sprite images are for no specific reason shiftet 4 positions in the sprite file
            sprite_direction = (self.last_direction+4) % 8

            # Select the appropriate sprite for the direction
            sprite.sprite_id = 'player_' + str(sprite_direction)


    def get_current_input_vector(pressed_keys):
        vector = (0,0,0)
        direction = None

        if pressed_keys[pygame.K_a] and pressed_keys[pygame.K_w]:
            direction = 7
        elif pressed_keys[pygame.K_w] and pressed_keys[pygame.K_d]:
            direction = 1
        elif pressed_keys[pygame.K_d] and pressed_keys[pygame.K_s]:
            direction = 3
        elif pressed_keys[pygame.K_s] and pressed_keys[pygame.K_a]:
            direction = 5
        elif pressed_keys[pygame.K_a]:
            direction = 6
        elif pressed_keys[pygame.K_w]:
            direction = 0
        elif pressed_keys[pygame.K_d]:
            direction = 2
        elif pressed_keys[pygame.K_s]:
            direction = 4

        speed = 0.25 if pressed_keys[pygame.K_LSHIFT] or pressed_keys[pygame.K_RSHIFT] else 0.1

        if direction != None:
            direction = (direction + 1) % 8
            vector = (PlayerMovementSystem.direction_vectors[direction][0] * speed, PlayerMovementSystem.direction_vectors[direction][1] * speed, 0)
        else:
            vector = (0,0,0)

        return (vector, speed, direction)
        

    def on_set_player_position(game_environment, msg):
        body = game_environment.player_entity.get_component_of_type(BodyComponent)
        phys = game_environment.player_entity.get_component_of_type(PhysicsComponent)
        phys.velocity = (0,0,0)
        phys.acceleration = (0,0,0)
        body.position = msg.position
        


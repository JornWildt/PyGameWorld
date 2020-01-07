from Physics.PhysicsComponent import PhysicsComponent
from Physics.BodyComponent import BodyComponent
from Blueprint.InputHandler import InputHandler
from Blueprint.PlayerMovementComponent import PlayerMovementComponent

class PlayerMovementSystem:
    def __init__(self, message_bus):
        self.is_moving = False
        message_bus.subscribe('tile_collision', PlayerMovementSystem.on_tile_collision)

    def on_tile_collision(p):
        entity = p[0]
        tile = p[1]
        pos = entity.get_component_of_type(BodyComponent)
        body = entity.get_component_of_type(PhysicsComponent)
        if tile.tile_type.is_blocking:
            pos.position = body.previous_position


    def update(self, game_environment):
        maxv = 0.2
        for (pos,phys,mov) in game_environment.entities_repository.get_components_of_types(BodyComponent, PhysicsComponent, PlayerMovementComponent):

            acc = 0.1
            xdiff = mov.intended_velocity[0] - phys.velocity[0]
            ydiff = mov.intended_velocity[1] - phys.velocity[1]
            phys.acceleration = (
                max(-acc,min(acc, xdiff)),
                max(-acc,min(acc, ydiff)),
                0
            )

            # if phys.velocity[0] > maxv or phys.velocity[0] < -maxv or phys.velocity[1] > maxv or phys.velocity[1] < -maxv or phys.velocity[2] > maxv or phys.velocity[2] < -maxv:
            #     phys.acceleration = (0,0,0)
            #     phys.velocity = (max(-maxv,min(maxv, phys.velocity[0])), min(maxv, phys.velocity[1]), min(maxv, phys.velocity[2]))
            if InputHandler.intent == 'Forward':
                mov.intended_velocity = (0.0, -0.1, 0.0)
                #phys.acceleration = (0.01,-0.01,0.0)
            elif InputHandler.intent == 'Backward':
                mov.intended_velocity = (0.0, 0.1, 0.0)
                #phys.acceleration = (-0.01,0.01,0.0)
            elif InputHandler.intent == 'Left':
                mov.intended_velocity = (-0.1, 0.0, 0.0)
                #phys.acceleration = (-0.01,-0.01,0.0)
            elif InputHandler.intent == 'Right':
                mov.intended_velocity = (0.1, 0.0, 0.0)
                #phys.acceleration = (0.01,0.01,0.0)
            elif InputHandler.intent == 'Stop':
                mov.intended_velocity = (0.0, 0.0, 0.0)
                #phys.acceleration = (0.0,0.0,0.0)
                #phys.velocity = (0,0,0)
            else:
                mov.intended_velocity = (0.0, 0.0, 0.0)


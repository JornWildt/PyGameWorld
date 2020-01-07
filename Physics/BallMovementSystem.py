import random
from .BallMovementComponent import BallMovementComponent
from .PhysicsComponent import PhysicsComponent
from .BodyComponent import BodyComponent
from Blueprint.InputHandler import InputHandler

class BallMovementSystem:
    def __init__(self, message_bus):
        self.is_moving = False
        message_bus.subscribe('tile_collision', BallMovementSystem.on_tile_collision)

    def on_tile_collision(p):
        entity = p[0]
        tile = p[1]
        pos = entity.get_component_of_type(BodyComponent)
        body = entity.get_component_of_type(PhysicsComponent)
        if tile.tile_type.is_blocking:
            xdir = random.randint(0,1)*2-1
            ydir = random.randint(0,1)*2-1

            if (tile.pos[0] < pos.position[0]):
                xdir = -1
                #ydir = 1
            elif (tile.pos[0] > pos.position[0]):
                xdir = -1
                #ydir = 1
            elif (tile.pos[1] < pos.position[1]):
                #xdir = 1
                ydir = -1
            elif (tile.pos[1] > pos.position[1]):
                #xdir = 1
                ydir = -1

            pos.position = body.previous_position
            pos.position = (
                body.previous_position[0] - 2*body.velocity[0], 
                body.previous_position[1] - 2*body.velocity[1], 
                body.previous_position[2] - 2*body.velocity[2])

            body.velocity = (xdir * body.velocity[0]/2, ydir * body.velocity[1]/2, 0)
            body.acceleration = (
                xdir * body.acceleration[0],
                ydir * body.acceleration[1],
                body.acceleration[2])


    def update(self, game_environment):
        maxv = 0.2
        for (pos,body,mov) in game_environment.entities_repository.get_components_of_types(BodyComponent, PhysicsComponent, BallMovementComponent):
            if body.velocity[0] > maxv or body.velocity[0] < -maxv or body.velocity[1] > maxv or body.velocity[1] < -maxv or body.velocity[2] > maxv or body.velocity[2] < -maxv:
                body.acceleration = (0,0,0)
                body.velocity = (min(maxv, body.velocity[0]), min(maxv, body.velocity[1]), min(maxv, body.velocity[2]))
            # elif InputHandler.intent == 'Forward':
            #     body.acceleration = (0.01,-0.01,0.0)
            # elif InputHandler.intent == 'Backward':
            #     body.acceleration = (-0.01,0.01,0.0)
            # elif InputHandler.intent == 'Left':
            #     body.acceleration = (-0.01,-0.01,0.0)
            # elif InputHandler.intent == 'Right':
            #     body.acceleration = (0.01,0.01,0.0)
            # else:
            #     body.acceleration = (0,0,0)
            elif random.randint(0,50) == 0:
                body.acceleration = (
                    random.randint(0,100)/10000 - 0.0050,
                    random.randint(0,100)/10000 - 0.0050,
                    0)

            # if pos.position[0] < 0 or pos.position[0] > 20:
            #     body.velocity = (-body.velocity[0],0,0)
            #     body.acceleration = (
            #         -body.acceleration[0],
            #         body.acceleration[1],
            #         body.acceleration[2])

            # if pos.position[1] < 0 or pos.position[1] > 20:
            #     body.velocity = (0,-body.velocity[1],0)
            #     body.acceleration = (
            #         body.acceleration[0],
            #         -body.acceleration[1],
            #         body.acceleration[2])
            


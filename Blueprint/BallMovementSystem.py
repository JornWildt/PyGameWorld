import random
from .BallMovementComponent import BallMovementComponent
from Core.Physics.PhysicsComponent import PhysicsComponent
from Core.Physics.BodyComponent import BodyComponent

class BallMovementSystem:
    def __init__(self, message_bus):
        message_bus.subscribe('tile_collision', BallMovementSystem.on_tile_collision)

    def on_tile_collision(game_environment, p):
        entity = p[0]
        tile = p[1]
        
        ball = entity.get_component_of_type(BallMovementComponent)
        if ball == None:
            return

        body = entity.get_component_of_type(BodyComponent)
        phys = entity.get_component_of_type(PhysicsComponent)
        if tile.tile_type.is_blocking:
            xdir = random.randint(0,1)*2-1
            ydir = random.randint(0,1)*2-1

            if (tile.position[0] < body.position[0]):
                xdir = -1
                #ydir = 1
            elif (tile.position[0] > body.position[0]):
                xdir = -1
                #ydir = 1
            elif (tile.position[1] < body.position[1]):
                #xdir = 1
                ydir = -1
            elif (tile.position[1] > body.position[1]):
                #xdir = 1
                ydir = -1

            body.position = body.previous_position
            body.position = (
                body.previous_position[0] - 2*phys.velocity[0], 
                body.previous_position[1] - 2*phys.velocity[1], 
                body.previous_position[2] - 2*phys.velocity[2])

            phys.velocity = (xdir * phys.velocity[0]/2, ydir * phys.velocity[1]/2, 0)
            phys.acceleration = (
                xdir * phys.acceleration[0],
                ydir * phys.acceleration[1],
                phys.acceleration[2])


    def update(self, game_environment):
        maxv = 0.2
        for (body,phys,mov) in game_environment.entities_repository.get_components_of_types(BodyComponent, PhysicsComponent, BallMovementComponent):
            if phys.velocity[0] > maxv or phys.velocity[0] < -maxv or phys.velocity[1] > maxv or phys.velocity[1] < -maxv or phys.velocity[2] > maxv or phys.velocity[2] < -maxv:
                phys.acceleration = (0,0,0)
                phys.velocity = (min(maxv, phys.velocity[0]), min(maxv, phys.velocity[1]), min(maxv, phys.velocity[2]))
            elif random.randint(0,50) == 0:
                phys.acceleration = (
                    random.randint(0,100)/10000 - 0.0050,
                    random.randint(0,100)/10000 - 0.0050,
                    0)


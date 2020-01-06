import random
from .BallMovementComponent import BallMovementComponent
from .PhysicsComponent import PhysicsComponent
from .PositionComponent import PositionComponent

class BallMovementSystem:
    def update(self, game_environment):
        for (pos,body,mov) in game_environment.entities_repository.get_components_of_types(PositionComponent, PhysicsComponent, BallMovementComponent):            
            tile = game_environment.scene.get_tile_at(pos.position)
            tileE = game_environment.scene.get_tile_at((pos.position[0]+0.9, pos.position[1], pos.position[2]))
            tileS = game_environment.scene.get_tile_at((pos.position[0], pos.position[1]+0.9, pos.position[2]))
            if random.randint(0,15) == 0:
                body.acceleration = (
                    random.randint(0,80)/10000 - 0.00040,
                    random.randint(0,80)/10000 - 0.00040,
                    0)
            elif tile != None and tile.tile_type.is_blocking or tileE != None and tileE.tile_type.is_blocking or tileS != None and tileS.tile_type.is_blocking:
                pos.position = (
                    pos.position[0] - 3*body.velocity[0], 
                    pos.position[1] - 3*body.velocity[1], 
                    pos.position[2] - 3*body.velocity[2])

                ax = random.randint(0,1)*2-1
                bx = random.randint(0,1)*2-1

                body.velocity = (ax * body.velocity[0]/2, bx * body.velocity[1]/2, 0)
                body.acceleration = (
                    ax * body.acceleration[0],
                    bx * body.acceleration[1],
                    body.acceleration[2])
            else:
                if pos.position[0] < 0 or pos.position[0] > 20:
                    body.velocity = (-body.velocity[0],0,0)
                    body.acceleration = (
                        -body.acceleration[0],
                        body.acceleration[1],
                        body.acceleration[2])

                if pos.position[1] < 0 or pos.position[1] > 20:
                    body.velocity = (0,-body.velocity[1],0)
                    body.acceleration = (
                        body.acceleration[0],
                        -body.acceleration[1],
                        body.acceleration[2])
            


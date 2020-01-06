import random
from .PhysicsComponent import PhysicsComponent
from .PositionComponent import PositionComponent

class PhysicsSystem:
    def update(self, game_environment):
        for (pos,body) in game_environment.entities_repository.get_components_of_types(PositionComponent, PhysicsComponent):

            body.velocity = (
                body.velocity[0] + body.acceleration[0], 
                body.velocity[1] + body.acceleration[1],
                body.velocity[2] + body.acceleration[2])
            
            pos.position = (
                min(20, max(0, pos.position[0] + body.velocity[0])), 
                min(20, max(0, pos.position[1] + body.velocity[1])),
                min(3, max(0, pos.position[2] + body.velocity[2])))
            

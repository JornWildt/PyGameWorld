from .PhysicsComponent import PhysicsComponent
from .BodyComponent import BodyComponent

class PhysicsSystem:
    def update(self, game_environment):

        for (body,phys) in game_environment.entities_repository.get_components_of_types(BodyComponent, PhysicsComponent):

            phys.previous_position = body.position

            phys.velocity = (
                phys.velocity[0] + phys.acceleration[0], 
                phys.velocity[1] + phys.acceleration[1],
                phys.velocity[2] + phys.acceleration[2])
            
            body.position = (
                (body.position[0] + phys.velocity[0]),
                (body.position[1] + phys.velocity[1]),
                (body.position[2] + phys.velocity[2]))
            

from Core.Physics.PhysicsComponent import PhysicsComponent
from Core.Physics.BodyComponent import BodyComponent
from .PlatformMovementComponent import PlatformMovementComponent
from Blueprint.Constants import Constants

class PlatformMovementSystem:
    def __init__(self, message_bus):
        pass


    def update(self, game_environment):
        for (body,phys,plat) in game_environment.entities_repository.get_components_of_types(BodyComponent, PhysicsComponent, PlatformMovementComponent):
            plat.count += 1
            if plat.count > plat.route[plat.leg][2]:
                plat.count = 0
                plat.leg = plat.leg + 1
                if plat.leg >= len(plat.route):
                    plat.leg = 0
                    body.position = plat.start_position
                leg = plat.route[plat.leg]
                vector = Constants.direction_vectors[leg[0]]
                phys.velocity = (vector[0] * leg[1], vector[1] * leg[1], 0)
                
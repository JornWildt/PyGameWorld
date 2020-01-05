from .PhysicsComponent import PhysicsComponent

class PhysicsSystem:
    def update(self, game_environment):
        for moveable in game_environment.entities_repository.get_components_of_type(type(PhysicsComponent)):
            moveable.position += moveable.velocity

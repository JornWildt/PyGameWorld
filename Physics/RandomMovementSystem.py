import random
from .RandomMovementComponent import RandomMovementComponent
from .PhysicsComponent import PhysicsComponent

class RandomMovementSystem:
    def update(self, game_environment):
        for (body,mov) in game_environment.entities_repository.get_components_of_types(PhysicsComponent, RandomMovementComponent):
            body.acceleration = (
                max(-0.1, min(0.1, body.acceleration[0] if random.randint(0,5) > 0 else body.acceleration[0] * -1)),
                max(-0.1, min(0.1, body.acceleration[1] if random.randint(0,5) > 0 else body.acceleration[1] * -1)),
                0
            )
            


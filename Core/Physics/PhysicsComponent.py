from Core.ECS.Component import Component

class PhysicsComponent(Component):
    def __init__(self, vel, acc):
        super().__init__()
        self.velocity = vel
        self.acceleration = acc

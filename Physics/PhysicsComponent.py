from ECS.Component import Component

class PhysicsComponent(Component):
    def __init__(self, pos, vel):
        super().__init__()
        self.position = pos
        self.velocity = vel

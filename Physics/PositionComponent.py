from ECS.Component import Component

class PositionComponent(Component):
    def __init__(self, pos):
        super().__init__()
        self.position = pos

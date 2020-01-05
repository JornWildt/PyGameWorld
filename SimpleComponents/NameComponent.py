from ECS.Component import Component

class NameComponent(Component):
    def __init__(self, name):
        super().__init__()
        self.name = name

from Core.ECS.Component import Component

class BodyComponent(Component):
    def __init__(self, pos, size = (1,1,1)):
        super().__init__()
        self.previous_position = None
        self.position = pos
        self.size = size
        self.size_2 = (size[0]/2, size[1]/2, size[2]/2)

        self.is_grounded = False
        self.ground_item = None
        self.ground_size = (size[0], size[1], 0.05)
        self.ground_size_2 = (size[0]/2, size[1]/2, 0.025)
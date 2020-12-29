﻿from Core.ECS.Component import Component

class BodyComponent(Component):
    def __init__(self, pos, size = (1,1,1)):
        super().__init__()
        self.previous_position = None
        self.position = pos
        self.size = size

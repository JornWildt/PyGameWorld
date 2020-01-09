from ECS.Component import Component

class SpriteComponent(Component):
    def __init__(self, sprite_id, offset = (0,0,0)):
        super().__init__()
        self.sprite_id = sprite_id
        self.offset = offset

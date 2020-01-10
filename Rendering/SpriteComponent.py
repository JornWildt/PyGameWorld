from ECS.Component import Component

class SpriteComponent(Component):
    def __init__(self, sprite_id):
        super().__init__()
        self.sprite_id = sprite_id

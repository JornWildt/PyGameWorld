from ..Physics.BodyComponent import BodyComponent
from .SpriteComponent import SpriteComponent
from .DisplayComponent import DisplayComponent

class DisplaySystem:
    def update(self, game_environment):

        for (body, sprite) in game_environment.entities_repository.get_components_of_types(BodyComponent, SpriteComponent):
            game_environment.scene.register_item(body.position, body.size, game_environment.sprites[sprite.sprite_id])

        for component in game_environment.entities_repository.get_components_of_type(DisplayComponent):
            component.display.render(game_environment)

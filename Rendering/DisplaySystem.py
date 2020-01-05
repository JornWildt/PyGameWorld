from Physics.PositionComponent import PositionComponent
from .SpriteComponent import SpriteComponent
from .DisplayComponent import DisplayComponent

class DisplaySystem:
    def update(self, game_environment):

        for (pos_c, sprite_c) in game_environment.entities_repository.get_components_of_types(PositionComponent, SpriteComponent):
            game_environment.scene.register_item(pos_c.position, game_environment.sprites[sprite_c.sprite_id])

        for component in game_environment.entities_repository.get_components_of_type(DisplayComponent):
            component.display.render(game_environment.screen)

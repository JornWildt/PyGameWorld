from Physics.BodyComponent import BodyComponent
from .SpriteComponent import SpriteComponent
from .DisplayComponent import DisplayComponent

class DisplaySystem:
    def update(self, game_environment):

        for component in game_environment.entities_repository.get_components_of_type(DisplayComponent):
            component.display.render(game_environment)

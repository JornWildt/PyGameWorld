from .Scenes.Scene_A1_Builder import Scene_A1_Builder
from .Scenes.Scene_A2_Builder import Scene_A2_Builder
from .Messages.SetPlayerPositionMessage import SetPlayerPositionMessage
from Rendering.Fader import fade_screen
from ECS.GameEngine import GameEngine


class GameEngine2(GameEngine):
    new_scene_builder = None

    def __init__(self, settings, game_environment):
        super().__init__(settings, game_environment)


    def on_frame_end(self):
        if GameEngine2.new_scene_builder != None:
            fade_screen(self.game_environment.screen)
            GameEngine2.new_scene_builder(self.game_environment).build_scene()
            GameEngine2.new_scene_builder = None
            self.game_environment.message_bus.publish('set_player_position', SetPlayerPositionMessage(GameEngine2.new_scene_message.start_position))



    def on_new_scene(game_environment, collision):
        entity = collision[0]
        GameEngine2.new_scene_message = msg = collision[1]
        if msg.scene_name == 'Scene_A1':
            GameEngine2.new_scene_builder = Scene_A1_Builder
        else:
            GameEngine2.new_scene_builder = Scene_A2_Builder

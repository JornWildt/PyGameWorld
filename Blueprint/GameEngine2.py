from Core.Rendering.Fader import fade_screen
from Core.GameEngine import GameEngine
from .Scenes.Scene_A1_Builder import Scene_A1_Builder
from .Scenes.Scene_A2_Builder import Scene_A2_Builder
from .Scenes.Scene_A3_Builder import Scene_A3_Builder
from .Messages.SetPlayerPositionMessage import SetPlayerPositionMessage
from Blueprint.PlayerMovementComponent import PlayerMovementComponent


class GameEngine2(GameEngine):
    new_scene_builder = None

    def __init__(self, settings, game_environment):
        super().__init__(settings, game_environment)


    def on_frame_end(self):
        if GameEngine2.new_scene_builder != None:
            fade_screen(self.game_environment.screen)
            self.game_environment.entities_repository.clear_scene_entities()
            GameEngine2.new_scene_builder(self.game_environment).build_scene()
            GameEngine2.new_scene_builder = None
            self.game_environment.message_bus.publish('set_player_position', SetPlayerPositionMessage(GameEngine2.new_scene_message.start_position))



    def on_new_scene(game_environment, collision):
        entity = collision[0]
        
        player = entity.get_component_of_type(PlayerMovementComponent)
        if player == None:
            return

        GameEngine2.new_scene_message = msg = collision[1]
        if msg.scene_name == 'Scene_A1':
            GameEngine2.new_scene_builder = Scene_A1_Builder
        elif msg.scene_name == 'Scene_A2':
            GameEngine2.new_scene_builder = Scene_A2_Builder
        else:
            GameEngine2.new_scene_builder = Scene_A3_Builder

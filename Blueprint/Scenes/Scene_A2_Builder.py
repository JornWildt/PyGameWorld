from .Scene_A_Builder import Scene_A_Builder


class Scene_A2_Builder(Scene_A_Builder):
    def __init__(self, game_environment):
        super().__init__(game_environment)

        self.player_start_pos = (2,2,1)
        self.scene_map = '''
X X X X X X
x . . . . X
x . . . . X
x . . T1. X
x x x x x X
'''

    
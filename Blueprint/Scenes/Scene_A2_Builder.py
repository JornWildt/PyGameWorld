from .Scene_A_Builder import Scene_A_Builder


class Scene_A2_Builder(Scene_A_Builder):
    def __init__(self, game_environment):
        super().__init__(game_environment)

        self.scene_map = '''
X X X X X X X X X X X X
x . . . . X . . . . . X
x . . . . X . . . . . X
x . . T1. X . . . . . X
x . . . . X . . . . . X
x . X X X X X X X X X X
x . . . . . . . . . T3X
x x x x x X X X X X X X
'''

    
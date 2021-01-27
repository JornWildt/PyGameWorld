from Core.Scene.Tile import Tile
from Core.Scene.TileType import *
from .Scene_A_Builder import Scene_A_Builder

class Scene_A1_Builder(Scene_A_Builder):

    def __init__(self, game_environment):
        super().__init__(game_environment)

        self.player_start_pos = (2,2,1)
        self.scene_map = '''
x X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X
x . . . . . . . . . . X . . . . . . . . . . X . . . . . . . . . . . . . X
x . . . . . . . . X X X . . . . . . . . . . X . . . . . . . . . . . . . X
x . . . . . . . . B T2X . . . . . . . . . . X . . . . . B B . . . . . . X
x . . . . . . . . . . X . . . T4. . . . . . X . . . . . B B . . . . . . X
x . . . . . . . . . . X . . . . . . . . . . . . . . . . . . . . . . . . X
x . . . . . . . . . . X . . . . . . . . . . . . . . . . . . . . . . . . X
x . . . . . B . . . . X . . . . . b . . . . X . . . . . . . . . . . . . X
x . . . . . . . . . . X . . . . . . . . . . X X X X X X X . . . . . . . X
x . . . . . . P . . . X . . . . . . . . . . X . . . . . . . . . . . . . X
x . . . . . . . . . . X . . . . . . . . . . X . . . . . . . . . . . . . X
x . . . . . . . . . . X . . . . . B . . . . X . . . . . . . . . . . . . X
X B B B B B . . . X X X . . . . . . . . . . X . . . . . . . . . . . . . X
x . . . . b . . . . B X . . . . . . . . . . X . . . . . . B B B B B B B X
x . . . . . . . . . . X . . . . b . . . . . X . . . . . . . . . . . . . X
x . . . . B . . . . . X . . . . . . . . . . . . . . . . . . . . . . . . X
x . . . . . . . . . . X . . . . . . . . . . . . . . . . . B . . . . . . X
x . . . . . . . . . . X . . . . . . . . . . X . . . . . B B B . . . . . X
x . . . b . . . . b . X . . . . . . . . . . X . . . . . . B . . . . . . X
x . . . . . . . . b . X . . . . . . . . . . X . . . . . . . . . . . . . X
x . . . . . . . . . . X . . . . . . . . . . X . . . . . . . . . . . . . X
x x x x x x x x x x x X X X X X X X X X X X X X X X X X X X X X X X X X X
'''

        self.xscene_map = '''
X X X
x . X
x x x
'''
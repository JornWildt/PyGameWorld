from Scene.Tile import Tile
from Scene.TileType import *
from Blueprint.Scene_1_Builder import Scene_1_Builder
from .SceneBuilder import SceneBuilder


class Scene_2_Builder(Scene_1_Builder):
    def __init__(self, game_environment):
        super().__init__(game_environment)

        self.player_start_pos = (2,2,1)
        self.scene_map = '''
X X X X X X
x . . . . X
x . . . . X
x . . . . X
x x x x x X
'''

    
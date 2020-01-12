from Scene.Tile import Tile
from Scene.TileType import *
from .SceneBuilder import SceneBuilder

class Scene_1_Builder(SceneBuilder):


    def build_floor(self, symbol, pos):
        self.place_cube(pos[0],pos[1],0, TileType.Floor, self.floor_sprite)

    def build_see_through_wall(self, symbol, pos):
        self.place_cube(pos[0],pos[1],0, TileType.Floor, self.floor_wall_sprite)
        self.place_cube(pos[0],pos[1],1, TileType.Wall, None)
        self.place_cube(pos[0],pos[1],2, TileType.Wall, None)

    def build_wall(self, symbol, pos):
        self.place_cube(pos[0],pos[1],0, TileType.Floor, self.floor_wall_sprite)
        self.place_cube(pos[0],pos[1],1, TileType.Wall, self.wall_sprite)
        self.place_cube(pos[0],pos[1],2, TileType.Wall, self.wall_sprite)

    def build_box(self, symbol, pos):
        self.place_cube(pos[0],pos[1],0, TileType.Floor, self.floor_wall_sprite)
        self.place_cube(pos[0],pos[1],1, TileType.Wall, self.box_sprite)

    def build_barrel(self, symbol, pos):
        self.place_cube(pos[0],pos[1],0, TileType.Floor, self.floor_wall_sprite)
        self.place_cube(pos[0],pos[1],1, TileType.Wall, self.barrel_sprite)

    def __init__(self, scene, sprites):
        super().__init__(scene, sprites)

        self.floor_sprite = sprites['floor']
        self.floor_wall_sprite = sprites['floor_wall']
        self.wall_sprite = sprites['wall']
        self.box_sprite = sprites['box']
        self.barrel_sprite = sprites['barrel']

        self.define_tile('.', Scene_1_Builder.build_floor)
        self.define_tile('x', Scene_1_Builder.build_see_through_wall)
        self.define_tile('X', Scene_1_Builder.build_wall)
        self.define_tile('b', Scene_1_Builder.build_box)
        self.define_tile('B', Scene_1_Builder.build_barrel)

        self.scene_map = '''
x X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X
x . . . . . . . . . . . . . . . . . . . . . X . . . . . . . . . . . . . X
x . . . . . . . . . . X . . . . . . . . . . X . . . . . . . . . . . . . X
x . . . . . . X X X X X . . . . . . . . . . X . . . . . B B . . . . . . X
x . . . . . . . . . . X . . . . . . . . . . X . . . . . B B . . . . . . X
x . . . . . . . . . . X . . . . . . . . . . . . . . . . . . . . . . . . X
x . . . . . . . . . . X . . . . . . . . . . . . . . . . . . . . . . . . X
x . . . . . B . . . . X . . . . . b . . . . X . . . . . . . . . . . . . X
x . . . . . . . . . . X . . . . . . . . . . X X X X X X X . . . . . . . X
x . . . . . . . . . . X . . . . . . . . . . X . . . . . . . . . . . . . X
x . . . . . . . . . . . . . . . . . . . . . X . . . . . . . . . . . . . X
x . . . . . . . . . . X . . . . . B . . . . X . . . . . . . . . . . . . X
X B B B B B . . . X X X . . . . . . . . . . X . . . . . . . . . . . . . X
x . . . . b . . . . B X . . . . . . . . . . X . . . . . . B B B B B B B X
x . . . . . . . . . . X . . . . b . . . . . X . . . . . . . . . . . . . X
x . . . . B . . . . . X . . . . . . . . . . . . . . . . . . . . . . . . X
x . . . . . . . . . . X . . . . . . . . . . . . . . . . . . . . . . . . X
x . . . . . . . . . . X . . . . . . . . . . X . . . . . . . . . . . . . X
x . . . b . . . . b . X . . . . . . . . . . X . . . . . . . . . . . . . X
x . . . . . . . . b . X . . . . . . . . . . X . . . . . . . . . . . . . X
x . . . . . . . . . . X . . . . . . . . . . X . . . . . . . . . . . . . X
x x x x x x x x x x x X X X X X X X X X X X X X X X X X X X X X X X X X X
'''

        self.xscene_map = '''
X X X
x . X
x x x
'''
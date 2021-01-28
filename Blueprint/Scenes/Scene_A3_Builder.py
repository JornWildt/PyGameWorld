from Core.Scene.Tile import Tile
from Core.Scene.TileType import *
from .Scene_A_Builder import Scene_A_Builder
import Blueprint.PlatformFactory as PlatformFactory

class Scene_A3_Builder(Scene_A_Builder):

    def build_platform(self, symbol, pos):
        if symbol[1] == '1':
            # Include floor underneath
            self.scene.place_cube(pos[0],pos[1],0, TileType.Floor, self.floor_wall_sprite)
            route = [(4, 0.03, 2), (0, 0.03, 2)]
            platform = PlatformFactory.build_a_platform('Platform', (pos[0],pos[1],2), route)
        if symbol[1] == '2':
            # Include floor underneath
            self.scene.place_cube(pos[0],pos[1],0, TileType.Floor, self.floor_wall_sprite)
            route = [(0, 0.03, 2), (4, 0.03, 2)]
            platform = PlatformFactory.build_a_platform('Platform', (pos[0],pos[1],2), route)
        self.game_environment.entities_repository.add_entity(platform)


    def __init__(self, game_environment):
        super().__init__(game_environment)

        self.player_start_pos = (2,2,1)
        self.scene_map = '''
x X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X
x . . . . . . . . . . X . . . . . . . . . . . X . . . . . . . . . . . . . X
x . . . . . . . . . . X . . P1P1. . . . P1P1. X . . . . . . . . . . . . . X
x . . . . . . . . . . B B B B B B B B B B B B B . . . . . . . . . . . . . X
x . . . . . . . . . . X . . . . . P2P2. . . . X . . . . . . . . . . . . . X
x . . . . . . . . . . X . . . . . . . . . . . X . . . . . . . . . . . . . X
x x x x x x x x x x x X X X X X X X X X X X X X X X X X X X X X X X X X X X
'''

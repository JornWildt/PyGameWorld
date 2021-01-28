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
        if symbol[1] == '3':
            # Include floor underneath
            self.scene.place_cube(pos[0],pos[1],0, TileType.Floor, self.floor_wall_sprite)
            route = [(4, 0.02, 4), (2, 0.04, 3), (0,0.02,4), (6,0.04,3)]
            platform = PlatformFactory.build_a_platform('Platform', (pos[0],pos[1],1), route)
        if symbol[1] == '4':
            # Include floor underneath
            self.scene.place_cube(pos[0],pos[1],0, TileType.Floor, self.floor_wall_sprite)
            route = [(2,0.04,3), (0,0.02,4), (6, 0.04, 3), (4, 0.02, 4)]
            platform = PlatformFactory.build_a_platform('Platform', (pos[0],pos[1],1), route)
        self.game_environment.entities_repository.add_entity(platform)


    def __init__(self, game_environment):
        super().__init__(game_environment)

        self.player_start_pos = (23,3,2)
        self.scene_map = '''
x X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X
x . . . . . . . . . . X . . . . . . . . . . . X P3. . . . . . . . B . . . X
x . . . . . . . . . . X . . P1P1. . . . P1P1. X . . . . . . . . B B B . . X
x . . . . . . . . . . B B B B B B B B B B B B B . . . . . . . . B B B B . X
x . . . . . . . . . . X . . . . . P2P2. . . . B . . . . . . . . B B B . . X
x . . . . . . . . . . X . . . . . . . . . . . X . . . . P4. . . . B . . . X
x x x x x x x x x x x X x x x x x x x x x x x X x x x x x x x x x x x x x X
'''

from Core.Scene.Tile import Tile
from Core.Scene.TileType import *
from .Scene_A_Builder import Scene_A_Builder
import Blueprint.PlatformFactory as PlatformFactory
from Core.Messages.NewSceneMessage import NewSceneMessage

class Scene_A3_Builder(Scene_A_Builder):

    def build_platform(self, symbol, pos):
        # Include floor underneath

        if symbol[1] == '1':
            self.scene.place_animated_cube(pos[0],pos[1],0, TileType.Space, self.lava_sprite)
            self.place_location_event_trigger((pos[0],pos[1],0), (1,1,0.5), 'new_scene', NewSceneMessage('Scene_A3', self.player_start_pos))
            route = [(4, 0.03, 2), (0, 0.03, 2)]
            platform = PlatformFactory.build_a_platform('Platform', (pos[0],pos[1],2), route)
        if symbol[1] == '2':
            self.scene.place_animated_cube(pos[0],pos[1],0, TileType.Space, self.lava_sprite)
            self.place_location_event_trigger((pos[0],pos[1],0), (1,1,0.5), 'new_scene', NewSceneMessage('Scene_A3', self.player_start_pos))
            route = [(0, 0.03, 2), (4, 0.03, 2)]
            platform = PlatformFactory.build_a_platform('Platform', (pos[0],pos[1],2), route)
        if symbol[1] == '3':
            self.scene.place_animated_cube(pos[0],pos[1],0, TileType.Space, self.lava_sprite)
            self.place_location_event_trigger((pos[0],pos[1],0), (1,1,0.5), 'new_scene', NewSceneMessage('Scene_A3', self.player_start_pos))
            route = [(4, 0.02, 4), (2, 0.04, 3), (0,0.02,4), (6,0.04,3)]
            platform = PlatformFactory.build_a_platform('Platform', (pos[0],pos[1],1), route)
        if symbol[1] == '4':
            self.scene.place_animated_cube(pos[0],pos[1],0, TileType.Space, self.lava_sprite)
            self.place_location_event_trigger((pos[0],pos[1],0), (1,1,0.5), 'new_scene', NewSceneMessage('Scene_A3', self.player_start_pos))
            route = [(2,0.04,3), (0,0.02,4), (6, 0.04, 3), (4, 0.02, 4)]
            platform = PlatformFactory.build_a_platform('Platform', (pos[0],pos[1],1), route)
        if symbol[1] == '5':
            self.scene.place_cube(pos[0],pos[1],0, TileType.Floor, self.floor_wall_sprite)
            route = [(4,0.02,2), (0,0.02,2)]
            platform = PlatformFactory.build_a_platform('Platform', (pos[0],pos[1],1), route)
            
        self.game_environment.entities_repository.add_entity(platform)


    def __init__(self, game_environment):
        super().__init__(game_environment)

        self.player_start_pos = (3,3,2)
        self.scene_map = '''
x X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X
x B * * * * * * . . . X * * * * * * * * * * * X P3* * * * * * * * B . . . X
x B B . P5. . * * * B X * * P1P1* * * * P1P1* X * * * * * * * * B B B . . X
x B B B . . . * . . B B B B B B B B B B B B B B * * * * * * * * B B B B . X
x B B . . . . * * * B X * * * * * P2P2* * * * B * * * * * * * * B B B . . X
x B * * * * * * . . . X * * * * * * * * * * * X * * * * P4* * * * B . . . X
x x x x x x x x x x x X x x x x x x x x x x x X x x x x x x x x x x x x x X
'''

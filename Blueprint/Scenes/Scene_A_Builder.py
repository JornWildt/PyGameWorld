from Core.Scene.Tile import Tile
from Core.Scene.TileType import *
from ..SceneBuilder import SceneBuilder
from Core.Messages.NewSceneMessage import NewSceneMessage
from Blueprint.BallMovementSystem import BallMovementSystem
import Blueprint.PlatformFactory as PlatformFactory


class Scene_A_Builder(SceneBuilder):

    def build_floor(self, symbol, pos):
        self.scene.place_cube(pos[0],pos[1],0, TileType.Floor, self.floor_sprite)

    def build_see_through_wall(self, symbol, pos):
        self.scene.place_cube(pos[0],pos[1],0, TileType.Floor, self.floor_wall_sprite)
        self.scene.place_cube(pos[0],pos[1],1, TileType.Wall, None)
        self.scene.place_cube(pos[0],pos[1],2, TileType.Wall, None)
        self.scene.place_cube(pos[0],pos[1],3, TileType.Wall, None)

    def build_wall(self, symbol, pos):
        self.scene.place_cube(pos[0],pos[1],0, TileType.Floor, self.floor_wall_sprite)
        self.scene.place_cube(pos[0],pos[1],1, TileType.Wall, self.wall_sprite)
        self.scene.place_cube(pos[0],pos[1],2, TileType.Wall, self.wall_sprite)
        self.scene.place_cube(pos[0],pos[1],3, TileType.Wall, None)

    def build_box(self, symbol, pos):
        self.scene.place_cube(pos[0],pos[1],0, TileType.Floor, self.floor_wall_sprite)
        self.scene.place_cube(pos[0],pos[1],1, TileType.Wall, self.box_sprite)

    def build_barrel(self, symbol, pos):
        self.scene.place_cube(pos[0],pos[1],0, TileType.Floor, self.floor_wall_sprite)
        self.scene.place_cube(pos[0],pos[1],1, TileType.Wall, self.barrel_sprite)

    def build_platform(self, symbol, pos):
        self.scene.place_cube(pos[0],pos[1],0, TileType.Floor, self.floor_wall_sprite)
        platform = PlatformFactory.build_a_platform('Platform', (pos[0],pos[1],1))
        self.game_environment.entities_repository.add_entity(platform)

    def build_teleport(self, symbol, pos):
        self.scene.place_cube(pos[0],pos[1],0, TileType.Floor, self.floor_wall_sprite)
        self.scene.place_animated_cube(pos[0],pos[1],1, TileType.Space, self.teleport_sprite)
        self.place_location_event_trigger((pos[0],pos[1],1), (0.5,0.5,0.5), 'new_scene', NewSceneMessage(self.teleports[symbol[1]][0], self.teleports[symbol[1]][1]))

    def build_lava(self, symbol, pos):
        self.scene.place_animated_cube(pos[0],pos[1],0, TileType.Space, self.lava_sprite)
        self.place_location_event_trigger((pos[0],pos[1],0), (0.5,0.5,1), 'new_scene', NewSceneMessage('Scene_A3', self.player_start_pos))


    def __init__(self, game_environment):
        super().__init__(game_environment)

        assets = game_environment.assets
        self.floor_sprite = assets['floor']
        self.floor_wall_sprite = assets['floor_wall']
        self.wall_sprite = assets['wall']
        self.box_sprite = assets['box']
        self.barrel_sprite = assets['barrel']
        self.teleport_sprite = assets['teleport']
        self.lava_sprite = assets['lava']

        self.define_tile_builder('.', self.build_floor)
        self.define_tile_builder('x', self.build_see_through_wall)
        self.define_tile_builder('X', self.build_wall)
        self.define_tile_builder('B', self.build_box)
        self.define_tile_builder('b', self.build_barrel)
        self.define_tile_builder('*', self.build_lava)
        self.define_tile_builder('P', self.build_platform)

        self.teleports = {
            '1': ('Scene_A1', (10,5,1)),
            '2': ('Scene_A2', (2,3,1)),
            '3': ('Scene_A1', (16,4,1)),
            '4': ('Scene_A2', (9,6,1))
        }

        self.define_tile_builder('T', self.build_teleport)

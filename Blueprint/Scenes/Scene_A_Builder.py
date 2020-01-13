from Scene.Tile import Tile
from Scene.TileType import *
from ..SceneBuilder import SceneBuilder
from ECS.Messages.NewSceneMessage import NewSceneMessage


class Scene_A_Builder(SceneBuilder):

    def build_floor(self, symbol, pos):
        self.scene.place_cube(pos[0],pos[1],0, TileType.Floor, self.floor_sprite)

    def build_see_through_wall(self, symbol, pos):
        self.scene.place_cube(pos[0],pos[1],0, TileType.Floor, self.floor_wall_sprite)
        self.scene.place_cube(pos[0],pos[1],1, TileType.Wall, None)
        self.scene.place_cube(pos[0],pos[1],2, TileType.Wall, None)

    def build_wall(self, symbol, pos):
        self.scene.place_cube(pos[0],pos[1],0, TileType.Floor, self.floor_wall_sprite)
        self.scene.place_cube(pos[0],pos[1],1, TileType.Wall, self.wall_sprite)
        self.scene.place_cube(pos[0],pos[1],2, TileType.Wall, self.wall_sprite)

    def build_box(self, symbol, pos):
        self.scene.place_cube(pos[0],pos[1],0, TileType.Floor, self.floor_wall_sprite)
        self.scene.place_cube(pos[0],pos[1],1, TileType.Wall, self.box_sprite)

    def build_barrel(self, symbol, pos):
        self.scene.place_cube(pos[0],pos[1],0, TileType.Floor, self.floor_wall_sprite)
        self.scene.place_cube(pos[0],pos[1],1, TileType.Wall, self.barrel_sprite)

    def build_teleport(self, symbol, pos):
        self.scene.place_cube(pos[0],pos[1],0, TileType.Floor, self.floor_wall_sprite)
        self.scene.place_animated_cube(pos[0],pos[1],1, TileType.Space, self.teleport_sprite)
        self.place_location_event_trigger((pos[0],pos[1],1), 'new_scene', NewSceneMessage(self.teleports[symbol[1]][0], self.teleports[symbol[1]][1]))


    def __init__(self, game_environment):
        super().__init__(game_environment)

        sprites = game_environment.sprites
        self.floor_sprite = sprites['floor']
        self.floor_wall_sprite = sprites['floor_wall']
        self.wall_sprite = sprites['wall']
        self.box_sprite = sprites['box']
        self.barrel_sprite = sprites['barrel']
        self.teleport_sprite = sprites['teleport']

        self.define_tile_builder('.', Scene_A_Builder.build_floor)
        self.define_tile_builder('x', Scene_A_Builder.build_see_through_wall)
        self.define_tile_builder('X', Scene_A_Builder.build_wall)
        self.define_tile_builder('B', Scene_A_Builder.build_box)
        self.define_tile_builder('b', Scene_A_Builder.build_barrel)

        self.teleports = {
            '1': ('Scene_A1', (10,5,1)),
            '2': ('Scene_A2', (2,3,1)),
            '3': ('Scene_A1', (16,4,1)),
            '4': ('Scene_A2', (9,6,1))
        }

        self.define_tile_builder('T', Scene_A_Builder.build_teleport)

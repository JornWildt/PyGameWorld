from Scene.Tile import Tile


class SceneBuilder:
    def __init__(self, scene, sprites):
        self.scene = scene
        self.sprites = sprites
        self.symbol_map = {}

    def define_tile(self, symbol, method):
        self.symbol_map[symbol] = method

    def build_scene(self):
        self.load_scene_from_map()

    def load_scene_from_map(self):
        scene = self.scene
        scene_map_array = self.scene_map.split('\n')

        scene_map_array = list(filter(None,scene_map_array))

        scene.width = int(len(scene_map_array[0]) / 2) + 1
        scene.height = len(scene_map_array)
        scene.depth = 3
        scene.size = (scene.width, scene.height, scene.depth)
        scene.tile_map = [[[None for y in range(scene.height)] for x in range(scene.width)] for z in range(scene.depth)]

        
        for x in range(scene.width):
            for y in range(scene.height):
                symbol = scene_map_array[y][x*2]
                if symbol != ' ':
                    builder_method = self.symbol_map[symbol]
                    builder_method(self, symbol, (x,y))

    def place_cube(self, x,y,z, tile_type, sprite):
        self.scene.tile_map[z][x][y] = Tile((x,y,z), tile_type, sprite)


        #         for 
        #         if scene_src_array[y][x] == 'x' or scene_src_array[y][x] == 'X':
        #             self.tile_map[0][x][y] = Tile((x,y,0), TileType.Wall, floor_wall_sprite)
        #         elif scene_src_array[y][x] == 'B':
        #             self.tile_map[0][x][y] = Tile((x,y,0), TileType.Wall, floor_sprite)
        #         elif scene_src_array[y][x] == 'b':
        #             self.tile_map[0][x][y] = Tile((x,y,0), TileType.Wall, floor_sprite)
        #         else:
        #             self.tile_map[0][x][y] = Tile((x,y,0), TileType.Floor, floor_sprite)

        # for x in range(self.width):
        #     for y in range(self.height):
        #         if scene_src_array[y][x] == 'X':
        #             self.tile_map[1][x][y] = Tile((x,y,1), TileType.Wall, wall_sprite)
        #         elif scene_src_array[y][x] == 'x' or scene_src_array[y][x] == '#':
        #             self.tile_map[1][x][y] = Tile((x,y,1), TileType.Wall, None)
        #         elif scene_src_array[y][x] == 'B':
        #             self.tile_map[1][x][y] = Tile((x,y,1), TileType.Wall, box_sprite)
        #         elif scene_src_array[y][x] == 'b':
        #             self.tile_map[1][x][y] = Tile((x,y,1), TileType.Wall, barrel_sprite)

        # for z in range(2, self.depth):
        #     for x in range(self.width):
        #         for y in range(self.height):
        #             if scene_src_array[y][x] == 'X':
        #                 self.tile_map[z][x][y] = Tile((x,y,z), TileType.Wall, wall_sprite)
        #             if scene_src_array[y][x] == '#' and z == 2:
        #                 self.tile_map[z][x][y] = Tile((x,y,z), TileType.Wall, None)
        #             elif scene_src_array[y][x] == '#' and z != 2:
        #                 self.tile_map[z][x][y] = Tile((x,y,z), TileType.Wall, wall_sprite)



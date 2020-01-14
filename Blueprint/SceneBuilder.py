from Core.Scene.Tile import Tile


class SceneBuilder:
    def __init__(self, init_environment):
        self.scene = init_environment.scene
        self.assets = init_environment.assets
        self.collision_map = init_environment.collision_map
        self.symbol_map = {}


    def define_tile_builder(self, symbol, method):
        self.symbol_map[symbol] = method


    def build_scene(self):
        scene_map_array = self.scene_map.split('\n')

        scene_map_array = list(filter(None,scene_map_array))

        width = int(len(scene_map_array[0]) / 2) + 1
        height = len(scene_map_array)
        depth = 3
        self.scene.initialize(width, height, depth)
        self.collision_map.initialize(self.scene)
        
        for x in range(self.scene.width):
            for y in range(self.scene.height):
                symbol1 = scene_map_array[y][x*2]
                symbol2 = scene_map_array[y][x*2+1] if x*2+1 < len(scene_map_array[y]) else ' '
                if symbol1 != ' ':
                    builder_method = self.symbol_map[symbol1]
                    builder_method(self, (symbol1, symbol2), (x,y))

        self.collision_map.load_from_scene(self.scene)


    def place_location_event_trigger(self, pos, size, message_name, message):
        self.collision_map.register_static_item(pos, size, message_name, message)


        
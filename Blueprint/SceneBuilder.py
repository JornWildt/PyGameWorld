from Scene.Tile import Tile


class SceneBuilder:
    def __init__(self, init_environment):
        self.scene = init_environment.scene
        self.sprites = init_environment.sprites
        self.collision_map = init_environment.collision_map
        self.symbol_map = {}


    def define_tile(self, symbol, method):
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
                symbol = scene_map_array[y][x*2]
                if symbol != ' ':
                    builder_method = self.symbol_map[symbol]
                    builder_method(self, symbol, (x,y))

        self.collision_map.load_from_scene(self.scene)


    def place_location_event_trigger(self, pos, message_name, item):
        self.collision_map.register_static_item(pos, (1,1,1), message_name, item)


        
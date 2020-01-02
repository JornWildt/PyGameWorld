

class GameSettings:

    def __init__(self):
        self.map_width_tiles = 200
        self.map_height_tiles = 100
        self.map_viewport_xtiles = 30
        self.map_viewport_ytiles = 20
        self.map_tile_pixels = 32

        self.window_width = self.map_viewport_xtiles * self.map_tile_pixels
        self.window_height = self.map_viewport_ytiles * self.map_tile_pixels

        self.FPS = 5

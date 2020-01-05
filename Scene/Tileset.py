import pygame
from Tile import Tile

class Tileset:

    def __init__(self, map_tile_pixels):
        self.tiles = {}
        self.map_tile_pixels = map_tile_pixels

    
    def add(self, sprites, name, sprite_rect):
        r = pygame.Rect(sprite_rect)
        image = sprites.image_at(r)
        tile = Tile(r.width, r.height, image, self.map_tile_pixels)
        self.tiles[name] = tile

    
    def get(self, name):
        return self.tiles[name]

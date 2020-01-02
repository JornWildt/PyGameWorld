import pygame
import random
from Tileset import Tileset
from Tile import Tile

class Map:
 
    def __init__(self, settings, background_tile):
        self.width = settings.map_width_tiles
        self.height = settings.map_height_tiles
        self.tile_pixels = settings.map_tile_pixels
        self.background_tile = background_tile


    def load(self, tile_map):
        self.tiles = tile_map


    def draw(self, screen, left, top, width, height):
        for y in range(top, top+height):
            for x in range(left, left+width):

                if x < 0 or x >= self.width or y < 0 or y >= self.height:
                    tile = self.background_tile
                else:
                    tile = self.tiles[x][y]
                
                z = tile.height
                xpos = (x-left)*self.tile_pixels
                ypos = (y-top)*self.tile_pixels
                rel_ypos = ypos - z * self.tile_pixels
                tile.draw(screen, xpos, rel_ypos)

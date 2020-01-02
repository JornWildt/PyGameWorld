import random
import numpy as np
import pygame
import scipy
import scipy.ndimage
from Map import Map
from Tile import Tile
from TileType import TileType


class MapGenerator:

    def __init__(self, settings, sprites):
        self.width = settings.map_width_tiles
        self.height = settings.map_height_tiles
        self.settings = settings
        self.sprites = sprites

    
    def generate(self):

        heights = np.random.rand(self.width, self.height)
        average = np.array([[0.111,0.111,0.111],[0.111,0.111,0.111],[0.111,0.111,0.111]])

        for i in range(10):
            heights = scipy.ndimage.filters.convolve(heights, average)

        type_map = [[None for y in range(self.height)] for x in range(self.width)]

        for x in range(self.width):
            for y in range(self.height):

                if heights[x][y] < 0.50:
                    heights[x][y] = 0
                    type_map[x][y] = TileType.Sea
                else:
                    heights[x][y] = int((heights[x][y]-0.5) * 50)
                    type_map[x][y] = TileType.Grass


        background = Tile(0, TileType.Sea, 16, 16, self.sprites.get('background'), self.settings.map_tile_pixels, self.settings.map_tile_pixels)
        tiles = [[None for y in range(self.height)] for x in range(self.width)]

        for x in range(self.width):
            for y in range(self.height):

                typeNW = self.get_map_type(type_map,x-1,y-1)
                typeN = self.get_map_type(type_map,x,y-1)
                typeNE = self.get_map_type(type_map,x+1,y-1)
                typeW = self.get_map_type(type_map,x-1,y)
                typeC = self.get_map_type(type_map,x,y)
                typeE = self.get_map_type(type_map,x+1,y)
                typeSW = self.get_map_type(type_map,x-1,y+1)
                typeS = self.get_map_type(type_map,x,y+1)
                typeSE = self.get_map_type(type_map,x+1,y+1)

                sprite = None
                tile = None

                heightN = heights[x][y-1] if y > 0 else 0
                heightC = heights[x][y]
                heightS = heights[x][y+1] if y < self.height-1 else 0

                has_step_N = heightN != heightC

                if typeC == TileType.Grass and not has_step_N:
                    if typeW == TileType.Sea and typeN == TileType.Sea:
                        sprite = self.sprites.get('water_grass_NW')
                    elif typeE == TileType.Sea and typeN == TileType.Sea:
                        sprite = self.sprites.get('water_grass_NE')
                    elif typeW == TileType.Sea and typeS == TileType.Sea:
                        sprite = self.sprites.get('water_grass_SW')
                    elif typeE == TileType.Sea and typeS == TileType.Sea:
                        sprite = self.sprites.get('water_grass_SE')
                    elif typeS == TileType.Grass and typeSE == TileType.Sea and typeE == TileType.Grass:
                        sprite = self.sprites.get('grass_water_NW')
                    elif typeS == TileType.Sea:
                        sprite = self.sprites.get('grass_water_N')
                    elif typeW == TileType.Grass and typeSW == TileType.Sea and typeS == TileType.Grass:
                        sprite = self.sprites.get('grass_water_NE')
                    elif typeE == TileType.Sea:
                        sprite = self.sprites.get('grass_water_W')
                    elif typeW == TileType.Sea:
                        sprite = self.sprites.get('grass_water_E')
                    elif typeN == TileType.Grass and typeNE == TileType.Sea and typeE == TileType.Grass:
                        sprite = self.sprites.get('grass_water_SW')
                    elif typeN == TileType.Sea:
                        sprite = self.sprites.get('grass_water_S')
                    elif typeN == TileType.Grass and typeNE == TileType.Sea and typeE == TileType.Grass:
                        sprite = self.sprites.get('grass_water_SE')
                    else:
                        sprite = self.sprites.get('grass')
                elif typeC == TileType.Grass and has_step_N:
                    sprite = self.sprites.get('grass')
                elif typeC == TileType.Sea:
                    sprite = self.sprites.get('grass_water_C')
                else:
                    tile = background

                if tile == None:
                    height_diff = heightC - heightS
                    hmod = 1
                    if height_diff > 0:
                        hmod += height_diff
                        tmp_surface = pygame.Surface((16, 16 + height_diff*16))
                        tmp_surface.fill(pygame.Color("brown"))
                        tmp_surface.blit(sprite, (0,0))
                        pygame.draw.rect(tmp_surface, pygame.Color("blue"), (0,0,16,16), 1)
                        sprite = tmp_surface
                    tile = Tile(heights[x][y], typeC, 16,16, sprite, self.settings.map_tile_pixels, int(self.settings.map_tile_pixels*hmod))

                tiles[x][y] = tile

        map = Map(self.settings, background)
        map.load(tiles)

        return map

    def get_map_type(self, type_map, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return TileType.Sea
        else:
            return type_map[x][y]

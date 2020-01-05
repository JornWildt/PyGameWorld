import pygame as pygame
from .Tile import Tile
from .TileType import *

class Scene:

    def __init__(self, settings):
        self.settings = settings

    def load_scene_from_string(self, scene_src, sprites):
        scene_src_array = scene_src.split()

        self.width = len(scene_src_array[0])
        self.height = len(scene_src_array)
        self.depth = 4
        self.tile_map = [[[None for y in range(self.height)] for x in range(self.width)] for z in range(self.depth)]

        floor_sprite = sprites['floor']
        floor_wall_sprite = sprites['floor_wall']
        wall_sprite = sprites['wall']
        box_sprite = sprites['box']
        barrel_sprite = sprites['barrel']
        
        for x in range(self.width):
            for y in range(self.height):
                if scene_src_array[y][x] == 'x' or scene_src_array[y][x] == 'X':
                    self.tile_map[0][x][y] = Tile(TileType.Wall, floor_wall_sprite)
                else:
                    self.tile_map[0][x][y] = Tile(TileType.Floor, floor_sprite)

        for x in range(self.width):
            for y in range(self.height):
                if scene_src_array[y][x] == 'X':
                    self.tile_map[1][x][y] = Tile(TileType.Wall, wall_sprite)
                elif scene_src_array[y][x] == 'B':
                    self.tile_map[1][x][y] = Tile(TileType.Wall, box_sprite)
                elif scene_src_array[y][x] == 'b':
                    self.tile_map[1][x][y] = Tile(TileType.Wall, barrel_sprite)

        for z in range(2, self.depth):
            for x in range(self.width):
                for y in range(self.height):
                    if scene_src_array[y][x] == 'X':
                        self.tile_map[z][x][y] = Tile(TileType.Wall, wall_sprite)

        return scene_src


    def start_frame(self):
        self.items_index = [[[None for y in range(self.height)] for x in range(self.width)] for z in range(self.depth)]


    def register_item(self, pos, sprite):
        x = int(pos[0])
        y = int(pos[1])
        z = int(pos[2])
        if x >= 0 and x < self.width and y >= 0 and y < self.height and z >= 0 and z < self.depth:
            if self.items_index[z][x][y] == None:
                self.items_index[z][x][y] = []
            self.items_index[z][x][y].append(SceneItem(pos,sprite))


    def render(self, screen):

        xmult = self.settings.map_tile_pixels/2
        ymult = self.settings.map_tile_pixels/4
        zmult = self.settings.map_tile_pixels/2

        xoffset = 50
        yoffset = self.height * ymult + self.width * ymult

        for z in range(self.depth):
            for x in range(self.width-1,-1,-1):
                for y in range(self.height):
                    tile = self.tile_map[z][x][y]
                    if tile != None:
                        xpos = (x+y) * xmult + xoffset
                        ypos = (y-x) * ymult - z * zmult + yoffset
                        screen.blit(tile.image, (xpos,ypos))

                    items = self.items_index[z][x][y]
                    for item in items if items != None else []:
                        xpos = (item.pos[0]+item.pos[1]) * xmult + xoffset
                        ypos = (item.pos[1]-item.pos[0]) * ymult - item.pos[2] * zmult + yoffset
                        item.sprite.blit(screen, (xpos,ypos))


class SceneItem:
    def __init__(self, pos, sprite):
        self.pos = pos
        self.sprite = sprite
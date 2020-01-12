import pygame as pygame
from .Tile import Tile
from .TileType import *
from Physics.BodyComponent import BodyComponent

class Scene:

    def __init__(self, settings):
        self.settings = settings

        self.xmult = int(self.settings.map_tile_pixels/2)
        self.ymult = int(self.settings.map_tile_pixels/4)
        self.zmult = int(self.settings.map_tile_pixels/2)

        self.xviewsize = 40
        self.yviewsize = 40
        self.zviewsize = 32

        self.xviewsize_2 = int(self.xviewsize/2)
        self.yviewsize_2 = int(self.yviewsize/2)
        self.zviewsize_2 = int(self.zviewsize/2)

        # These constants define size which is cut out of the corners
        # Top-left
        self.corner_size_1 = int((self.xviewsize + self.yviewsize)/4) - 1
        # Top-right and bottom-left
        self.corner_size_2 = int((self.xviewsize + self.yviewsize)/2) - int(self.corner_size_1)/2
        # Bottom-right
        self.corner_size_3 = self.xviewsize + self.yviewsize - int((self.xviewsize + self.yviewsize)/4) - 1

        self.window_x = int(self.settings.window_width/2)
        self.window_y = int(self.settings.window_height/2)



    def start_frame(self):
        self.items_index = [[[None for y in range(self.height)] for x in range(self.width)] for z in range(self.depth)]


    def register_item(self, pos, size_box, sprite):
        # x0 = int(pos[0] - size_box[0]/2)
        # x1 = int(x0 + size_box[0]) + 1
        # y0 = int(pos[1] - size_box[1]/2)
        # y1 = int(y0 + size_box[1]) + 1
        # z0 = int(pos[2] - size_box[2]/2)
        # z1 = int(z0 + size_box[2]) + 1

        x0 = int(pos[0] + 0.5)
        x1 = int(x0+size_box[0] + 0.5)
        y0 = int(pos[1] + 0.5)
        y1 = int(y0+size_box[1] + 0.5)
        z0 = int(pos[2])
        z1 = int(pos[2]+size_box[2] + 0.5)
        for x in range(x0,x1):
            for y in range(y0,y1):
                for z in range(z0,z1):
                    if x >= 0 and x < self.width and y >= 0 and y < self.height and z >= 0 and z < self.depth:
                        if self.items_index[z][x][y] == None:
                            self.items_index[z][x][y] = []
                        self.items_index[z][x][y].append(SceneItem(pos,(x-x0,y-y0,z-z0),sprite))


    def get_tile_at(self, pos):
        return self.tile_map[int(pos[2])][int(pos[0])][int(pos[1])]


    def render(self, game_environment):
        screen = game_environment.screen
        center = game_environment.player_entity.get_component_of_type(BodyComponent).position

        # Subtract 32 and 48 to get center of cube at (0,0,0) right at screen position 0,0 
        # (since sprites are offset at their top left corner)
        xoffset = self.window_x - (center[0]+center[1]) * self.xmult - 32
        yoffset = self.window_y -(center[1]-center[0]) * self.ymult + center[2] * self.zmult - 48

        for z in range(max(0,int(center[2]-self.zviewsize_2)), min(int(center[2]+self.zviewsize_2),self.depth)):
            tile_map_z = self.tile_map[z]
            for xx in range(self.xviewsize-1,-1,-1):
                x = int(center[0]) - self.xviewsize_2 + xx
                if x >= 0 and x < self.width:
                    tile_map_x = tile_map_z[x]
                    for yy in range(self.yviewsize):
                        if xx + yy > self.corner_size_1 and xx + yy < self.corner_size_3 and xx - yy > -self.corner_size_2 and yy - xx > -self.corner_size_2:
                            y = int(center[1]) - self.yviewsize_2 + yy
                            if y >= 0 and y < self.height:
                                tile = tile_map_x[y]
                                if tile != None:
                                    xpos = (x+y) * self.xmult + xoffset# - 32
                                    ypos = (y-x) * self.ymult - z * self.zmult + yoffset# - 48
                                    if tile.image != None:
                                        screen.blit(tile.image, (xpos,ypos))

                                items = self.items_index[z][x][y]
                                for item in items if items != None else []:
                                    # Items are supposed to be slices into cubes/tiles matching the map tiles, and
                                    # each item is registered at a cube/tile location together with that cube's
                                    # offset relative to the item's origin position.
                                    ix = item.pos[0] + item.offset[0]
                                    iy = item.pos[1] + item.offset[1]
                                    iz = item.pos[2] + item.offset[2]
                                    xpos = (ix+iy) * self.xmult + xoffset# - 32
                                    ypos = (iy-ix) * self.ymult - iz * self.zmult + yoffset# - 48
                                    item.sprite.blit(screen, (xpos,ypos), item.offset)

        # Indicate tile (0,0,0) position with a 3x3 square
        pygame.draw.rect(screen, (0,128,0,128), (xoffset-1+32,yoffset+48-1,3,3), 1)

        # Indicate window (0,0,0) position with a 3x3 square
        pygame.draw.rect(screen, (0,128,0,128), (self.window_x-1,self.window_y-1,3,3), 1)



class SceneItem:
    def __init__(self, pos, offset, sprite):
        self.pos = pos
        self.offset = offset
        self.sprite = sprite
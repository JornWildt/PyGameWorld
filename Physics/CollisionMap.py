﻿class CollisionMap:

    def __init__(self, settings):
        self.settings = settings


    def initialize(self, scene):
        self.size = scene.size
        self.static_map = [[[[] for z in range(self.size[2])] for y in range(self.size[1])] for x in range(self.size[0])]


    def load_from_scene(self, scene):
        for x in range(scene.size[0]):
            for y in range(scene.size[1]):
                for z in range(scene.size[2]):
                    tile = scene.get_tile_at((x,y,z))
                    if tile != None:
                        self.static_map[x][y][z].append(CollisionRegistration(tile.position, 'tile_collision', tile))


    def register_static_item(self, pos, size, message_name, item):
        x0 = int(pos[0])
        x1 = int(x0 + size[0])+1
        y0 = int(pos[1])
        y1 = int(y0 + size[1])+1
        z0 = int(pos[2])
        z1 = int(z0 + size[2])+1

        # Register item in all the cubes it overlaps
        for x in range(x0,x1):
            for y in range(y0,y1):
                for z in range(z0,z1):
                    if x >= 0 and x < self.size[0] and y >= 0 and y < self.size[1] and z >= 0 and z < self.size[2]:
                        self.static_map[x][y][z].append(CollisionRegistration(pos, message_name, item))



    def start_frame(self):
        pass
        # self.map = [[[None for z in range(self.size[2])] for y in range(self.size[1])] for x in range(self.size[0])]


    def register_item(self, pos, size, item):
        x0 = int(pos[0])
        x1 = int(x0 + size[0])+1
        y0 = int(pos[1])
        y1 = int(y0 + size[1])+1
        z0 = int(pos[2])
        z1 = int(z0 + size[2])+1

        # Nothing here yet ...

        # Register item in all the cubes it overlaps
        # for x in range(x0,x1):
        #     for y in range(y0,y1):
        #         for z in range(z0,z1):
        #             if x >= 0 and x < self.size[0] and y >= 0 and y < self.size[1] and z >= 0 and z < self.size[2]:
        #                 if self.map[x][y][z] == None:
        #                     self.map[x][y][z] = []
        #                 self.map[x][y][z].append(item)


    def get_items_at(self, pos):
        if pos[0] >= 0 and pos[0] < self.size[0] and pos[1] >= 0 and pos[1] < self.size[1] and pos[2] >= 0 and pos[2] < self.size[2]:
            items = self.static_map[pos[0]][pos[1]][pos[2]]
            return items
        else:
            return None


class CollisionRegistration:
    def __init__(self, position, message_name, item):
        self.position = position
        self.message_name = message_name
        self.item = item
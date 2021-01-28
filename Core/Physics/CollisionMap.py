class CollisionMap:

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
                        self.static_map[x][y][z].append(CollisionRegistration(tile.position, (1,1,1), 'tile_collision', tile))


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
                        self.static_map[x][y][z].append(CollisionRegistration(pos, size, message_name, item))



    def start_frame(self):
        self.map = [[[None for z in range(self.size[2])] for y in range(self.size[1])] for x in range(self.size[0])]


    def register_body(self, body):
        x0 = max(0, int(body.position[0] - body.size_2[0]))
        x1 = min(int(body.position[0] + body.size[0] - body.size_2[0]), self.size[0])
        y0 = max(0, int(body.position[1] - body.size_2[1]))
        y1 = min(int(body.position[1] + body.size[1] - body.size_2[1]), self.size[1])
        z0 = max(0, int(body.position[2] - body.size_2[2]))
        z1 = min(int(body.position[2] + body.size[2] - body.size_2[2]), self.size[2])

        # Register item in all the cubes it overlaps
        for x in range(x0,x1):
            for y in range(y0,y1):
                for z in range(z0,z1):
                    list = self.map[x][y][z]
                    if list == None:
                        list = self.map[x][y][z] = []
                    list.append(CollisionRegistration(body.position, body.size, 'body_collision', body))


    def unregister_body(self, body):
        x0 = max(0, int(body.position[0] - body.size_2[0]))
        x1 = min(int(body.position[0] + body.size[0] - body.size_2[0]), self.size[0])
        y0 = max(0, int(body.position[1] - body.size_2[1]))
        y1 = min(int(body.position[1] + body.size[1] - body.size_2[1]), self.size[1])
        z0 = max(0, int(body.position[2] - body.size_2[2]))
        z1 = min(int(body.position[2] + body.size[2] - body.size_2[2]), self.size[2])

        # Register item in all the cubes it overlaps
        for x in range(x0,x1):
            for y in range(y0,y1):
                for z in range(z0,z1):
                    list = self.map[x][y][z]
                    if list != None:
                        for i, registration in enumerate(list):
                            if registration.item == body:
                                del list[i]


    def get_items_at(self, pos):
        if pos[0] >= 0 and pos[0] < self.size[0] and pos[1] >= 0 and pos[1] < self.size[1] and pos[2] >= 0 and pos[2] < self.size[2]:
            static_items = self.static_map[pos[0]][pos[1]][pos[2]]
            dynamic_items = self.map[pos[0]][pos[1]][pos[2]]
            if static_items == None:
                return dynamic_items
            if dynamic_items == None:
                return static_items
            return static_items + dynamic_items
        else:
            return None


class CollisionRegistration:
    def __init__(self, position, size, message_name, item):
        self.position = position
        self.size = size
        self.size_2 = (size[0]/2, size[1]/2, size[2]/2)
        self.message_name = message_name
        self.item = item

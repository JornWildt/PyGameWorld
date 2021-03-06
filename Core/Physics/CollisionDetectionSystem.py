﻿from Core.Scene.Tile import Tile
from .BodyComponent import BodyComponent


class CollisionDetectionSystem:
    def update(self, game_environment):

        collision_map = game_environment.collision_map
        collision_map.start_frame()

        for body in game_environment.entities_repository.get_components_of_type(BodyComponent):
            collision_map.register_body(body)

        for body in game_environment.entities_repository.get_components_of_type(BodyComponent):
            items = CollisionDetectionSystem.checkCollision(collision_map, body)
            for item in items:
                game_environment.message_bus.publish(item.item.message_name, (body.entity, item.item.item, item.collisionNormal))


    @classmethod
    def checkCollision(self, collision_map, body):
        body_x_min = body.position[0] - body.size_2[0]
        body_y_min = body.position[1] - body.size_2[1]
        body_z_min = body.position[2] # - body.size_2[2]

        body_x_max = body_x_min + body.size[0]
        body_y_max = body_y_min + body.size[1]
        body_z_max = body_z_min + body.size[2]

        x0 = max(0, int(body_x_min) - 2)
        x1 = min(int(body_x_max) + 2, collision_map.size[0])
        y0 = max(0, int(body_y_min) - 2)
        y1 = min(int(body_y_max) + 2, collision_map.size[1])
        z0 = max(0, int(body_z_min) - 2)
        z1 = min(int(body_z_max) + 2, collision_map.size[2])
        found = False

        result = []
        visited = set()

        for x in range(x0,x1) if  not found else []:
            for y in range(y0,y1) if not found else []:
                for z in range(z0,z1) if not found else []:
                    items = collision_map.get_items_at((x,y,z))
                    for item in items:
                        if item not in visited and item.item != body:
                            visited.add(item)

                            item_x_min = item.position[0] - item.size_2[0]
                            item_y_min = item.position[1] - item.size_2[1]
                            item_z_min = item.position[2] # - item.size_2[2]

                            item_x_max = item_x_min + item.size[0]
                            item_y_max = item_y_min + item.size[1]
                            item_z_max = item_z_min + item.size[2]

                            x_overlap = min(body_x_max - item_x_min, item_x_max - body_x_min)
                            y_overlap = min(body_y_max - item_y_min, item_y_max - body_y_min)
                            z_overlap = min(body_z_max - item_z_min, item_z_max - body_z_min)

                            collisionNormal = None

                            if x_overlap > 0 and y_overlap > 0 and z_overlap > 0:
                                if x_overlap <= y_overlap and x_overlap <= z_overlap:
                                    if body.position[0] < item.position[0]:
                                        collisionNormal = (-1,0,0)
                                    else:
                                        collisionNormal = (1,0,0)
                                elif y_overlap <= x_overlap and y_overlap <= z_overlap:
                                    if body.position[1] < item.position[1]:
                                        collisionNormal = (0,-1,0)
                                    else:
                                        collisionNormal = (0,1,0)
                                elif z_overlap <= x_overlap and z_overlap <= y_overlap:
                                    if body.position[2] < item.position[2]:
                                        collisionNormal = (0,0,-1)
                                    else:
                                        collisionNormal = (0,0,1)

                                if collisionNormal[1] == 1 and body.size[2] > 1:
                                    asdfdf = 341
                                result.append(CollisionData(item,collisionNormal))

        return result


class CollisionData:
    def __init__(self, item, collisionNormal):
        self.item = item
        self.collisionNormal = collisionNormal

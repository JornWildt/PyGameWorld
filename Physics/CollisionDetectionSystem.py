from .BodyComponent import BodyComponent
# from .CollisionMap import CollisionMap


class CollisionDetectionSystem:
    def update(self, game_environment):

        collision_map = game_environment.collision_map
        collision_map.start_frame()

        for body in game_environment.entities_repository.get_components_of_type(BodyComponent):
            collision_map.register_item(body.position, body.size, body)

        for body in game_environment.entities_repository.get_components_of_type(BodyComponent):
            x0 = max(0, int(body.position[0] - 0.25) - 2)
            x1 = min(int(body.position[0] + body.size[0] - 0.25) + 2, collision_map.size[0])
            y0 = max(0, int(body.position[1] - 0.25) - 2)
            y1 = min(int(body.position[1] + body.size[1] - 0.25) + 2, collision_map.size[1])
            z0 = 1 # int(body.position[2] - 0.25) - 1
            z1 = 2 # int(z0 + body.size[2]) + 2
            found = False
            # Only look for a colliding item until a item is found, then skip the rest for the current body
            for x in range(x0,x1) if  not found else []:
                for y in range(y0,y1) if not found else []:
                    for z in range(z0,z1) if not found else []:
                        box_x = body.position[0] - body.size[0]/2
                        box_y = body.position[1] - body.size[1]/2
                        items = game_environment.collision_map.get_items_at((x,y,z))
                        for item in items:
                            # TODO: size should be taken from item
                            if box_x <= item.position[0]+0.5 and box_x + body.size[0] >= item.position[0]-0.5 and box_y <= item.position[1]+0.5 and box_y + body.size[1] >= item.position[1]-0.5 and body.position[2] == item.position[2]:
                                game_environment.message_bus.publish(item.message_name, (body.entity, item.item))
                                found = True
                                break

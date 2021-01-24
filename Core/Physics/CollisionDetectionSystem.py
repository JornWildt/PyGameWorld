from .BodyComponent import BodyComponent


class CollisionDetectionSystem:
    def update(self, game_environment):

        collision_map = game_environment.collision_map
        collision_map.start_frame()

        for body in game_environment.entities_repository.get_components_of_type(BodyComponent):
            collision_map.register_body(body)

        for body in game_environment.entities_repository.get_components_of_type(BodyComponent):
            ground_body = BodyComponent((body.position[0], body.position[1], body.position[2]-0.05), body.ground_size)
            items = self.checkCollision(collision_map, ground_body)
            if len(items) > 0:
                # FIXME: Check if tile -> then if tile type is "blockable"
                body.is_grounded = True
                body.ground_item = items[0].item
            else:
                body.is_grounded = False
                body.ground_item = None

        for body in game_environment.entities_repository.get_components_of_type(BodyComponent):
            items = self.checkCollision(collision_map, body)
            for item in items:
                game_environment.message_bus.publish(item.message_name, (body.entity, item.item))



    def checkCollision(self, collision_map, body):
        x0 = max(0, int(body.position[0] - body.size_2[0]) - 2)
        x1 = min(int(body.position[0] + body.size[0] - body.size_2[0]) + 2, collision_map.size[0])
        y0 = max(0, int(body.position[1] - body.size_2[1]) - 2)
        y1 = min(int(body.position[1] + body.size[1] - body.size_2[1]) + 2, collision_map.size[1])
        z0 = max(0, int(body.position[2] - body.size_2[2]) - 2)
        z1 = min(int(body.position[2] + body.size[2] - body.size_2[2]) + 2, collision_map.size[2])
        found = False
        
        body_x_max = body.position[0] + body.size[0]
        body_y_max = body.position[1] + body.size[1]
        body_z_max = body.position[2] + body.size[2]

        # Only look for a colliding item until a item is found, then skip the rest for the current body
        for x in range(x0,x1) if  not found else []:
            for y in range(y0,y1) if not found else []:
                for z in range(z0,z1) if not found else []:
                    items = collision_map.get_items_at((x,y,z))
                    result = []
                    for item in items:
                        item_x_max = item.position[0] + item.size[0]
                        item_y_max = item.position[1] + item.size[1]
                        item_z_max = item.position[2] + item.size[2]
                        if item.item != body:
                            if (item.position[0] < body_x_max and body.position[0] < item_x_max) and (item.position[1] < body_y_max and body.position[1] < item_y_max) and (item.position[2] < body_z_max and body.position[2] < item_z_max):
                                result.append(item)
                    if len(result) > 0:
                        return result

        return []
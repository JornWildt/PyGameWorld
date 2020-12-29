from .BodyComponent import BodyComponent


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
            z0 = max(0, int(body.position[2] - 0.25) - 2)
            z1 = min(int(body.position[2] + body.size[2] - 0.25) + 2, collision_map.size[2])
            found = False
            
            body_x_max = body.position[0] + body.size[0]
            body_y_max = body.position[1] + body.size[1]
            body_z_max = body.position[2] + body.size[2]

            # Only look for a colliding item until a item is found, then skip the rest for the current body
            for x in range(x0,x1) if  not found else []:
                for y in range(y0,y1) if not found else []:
                    for z in range(z0,z1) if not found else []:
                        items = game_environment.collision_map.get_items_at((x,y,z))
                        for item in items:
                            item_x_max = item.position[0] + item.size[0]
                            item_y_max = item.position[1] + item.size[1]
                            item_z_max = item.position[2] + item.size[2]
                            if (item.position[0] < body_x_max and body.position[0] < item_x_max) and (item.position[1] < body_y_max and body.position[1] < item_y_max) and (item.position[2] < body_z_max and body.position[2] < item_z_max):
                                # overlap_x = min(item_x_max - body.position[0], body_x_max - item.position[0])
                                # overlap_y = min(item_y_max - body.position[1], body_y_max - item.position[1])
                                # overlap_z = min(item_z_max - body.position[2], body_z_max - item.position[2])
                                # plane = 0
                                # if overlap_x < overlap_y and overlap_x < overlap_z:
                                #     plane = 1
                                # if overlap_y < overlap_x and overlap_y < overlap_z:
                                #     plane = 2
                                # if overlap_z < overlap_x and overlap_z < overlap_y:
                                #     plane = 3
                                game_environment.message_bus.publish(item.message_name, (body.entity, item.item))
                                found = True
                                break

                            # delta_x = item.position[0] - body.position[0]
                            # delta_y = item.position[1] - body.position[1]
                            # delta_z = item.position[2] - body.position[2]
                            # size_x = item.size[0]/2 + body.size[0]/2
                            # size_y = item.size[1]/2 + body.size[1]/2
                            # size_z = item.size[2]/2 + body.size[2]/2
                            # if size_x > abs(delta_x) and size_y > abs(delta_y) and size_z > abs(delta_z):

                        # box_x = body.position[0] - body.size[0]/2
                        # box_y = body.position[1] - body.size[1]/2
                        # box_z = body.position[2] - body.size[2]/2
                        # items = game_environment.collision_map.get_items_at((x,y,z))
                        # for item in items:
                        #     item_size_x2 = item.size[0] / 2
                        #     item_size_y2 = item.size[1] / 2
                        #     item_size_z2 = item.size[2] / 2
                        #     if box_x <= item.position[0]+item_size_x2 and box_x + body.size[0] >= item.position[0]-item_size_x2 and box_y <= item.position[1]+item_size_y2 and box_y + body.size[1] >= item.position[1]-item_size_y2 and box_z <= item.position[2]+item_size_z2 and box_z + body.size[2] >= item.position[2]-item_size_z2:
                        #         game_environment.message_bus.publish(item.message_name, (body.entity, item.item))
                        #         found = True
                        #         break

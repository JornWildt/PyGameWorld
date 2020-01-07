from .BodyComponent import BodyComponent

class CollisionDetectionSystem:
    def update(self, game_environment):
        for body in game_environment.entities_repository.get_components_of_type(BodyComponent):
            x0 = int(body.position[0])
            x1 = int(body.position[0]+body.size[0]) + 1
            y0 = int(body.position[1])
            y1 = int(body.position[1]+body.size[1]) + 1
            z0 = int(body.position[2])
            z1 = int(body.position[2]+body.size[2]) + 1
            tile = None
            # Only look for a colliding tile until a tile is found, then skip the rest for the current body
            for x in range(x0,x1) if tile == None else []:
                for y in range(y0,y1) if tile == None else []:
                    for z in range(z0,z1) if tile == None else []:
                        tile = game_environment.scene.get_tile_at((x,y,z))
                        if tile != None:
                            game_environment.message_bus.publish('tile_collision', (body.entity, tile))
                            break

from .BodyComponent import BodyComponent

class CollisionDetectionSystem:
    def update(self, game_environment):
        for body in game_environment.entities_repository.get_components_of_type(BodyComponent):
            x0 = max(0, int(body.position[0] - 0.25) - 2)
            x1 = min(int(body.position[0] + body.size[0] - 0.25) + 2, game_environment.scene.width)
            y0 = max(0, int(body.position[1] - 0.25) - 2)
            y1 = min(int(body.position[1] + body.size[1] - 0.25) + 2, game_environment.scene.height)
            z0 = 1 # int(body.position[2] - 0.25) - 1
            z1 = 2 # int(z0 + body.size[2]) + 2
            tile = None
            # Only look for a colliding tile until a tile is found, then skip the rest for the current body
            for x in range(x0,x1) if tile == None else []:
                for y in range(y0,y1) if tile == None else []:
                    for z in range(z0,z1) if tile == None else []:
                        tile = game_environment.scene.get_tile_at((x,y,z))
                        if tile != None:
                            bodyx = body.position[0] + 0.25
                            bodyy = body.position[1] + 0.25
                            if bodyx <= tile.pos[0]+1 and bodyx + body.size[0] >= tile.pos[0] and bodyy <= tile.pos[1]+1 and bodyy + body.size[1] >= tile.pos[1] and body.position[2] == tile.pos[2]:
                                game_environment.message_bus.publish('tile_collision', (body.entity, tile))
                                break
                            else:
                                tile = None

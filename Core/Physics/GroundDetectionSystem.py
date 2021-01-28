from Core.Scene.Tile import Tile
from .BodyComponent import BodyComponent
from .CollisionDetectionSystem import CollisionDetectionSystem


class GroundDetectionSystem:
    def update(self, game_environment):

        collision_map = game_environment.collision_map

        for body in game_environment.entities_repository.get_components_of_type(BodyComponent):
            ground_body = BodyComponent((body.position[0], body.position[1], body.position[2]-0.05), body.ground_size)
            items = CollisionDetectionSystem.checkCollision(collision_map, ground_body)

            body.is_grounded = False
            body.ground_item = None
            if len(items) > 0:
                if isinstance(items[0].item.item, Tile) and items[0].item.item.tile_type.is_blocking or isinstance(items[0].item.item, BodyComponent):
                    body.is_grounded = True
                    body.ground_item = items[0].item.item


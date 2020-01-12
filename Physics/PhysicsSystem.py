import random
from .PhysicsComponent import PhysicsComponent
from .BodyComponent import BodyComponent
from Rendering.SpriteComponent import SpriteComponent

class PhysicsSystem:
    def __init__(self):
        pass


    def update(self, game_environment):

        # Use the scene as a 3D hashmap for item lookup
        # FIXME: not a perfect place for this!
        for (body, sprite) in game_environment.entities_repository.get_components_of_types(BodyComponent, SpriteComponent):
            game_environment.scene.register_item(body.position, body.size, game_environment.sprites[sprite.sprite_id])

        for (body,phys) in game_environment.entities_repository.get_components_of_types(BodyComponent, PhysicsComponent):

            phys.previous_position = body.position

            phys.velocity = (
                phys.velocity[0] + phys.acceleration[0], 
                phys.velocity[1] + phys.acceleration[1],
                phys.velocity[2] + phys.acceleration[2])
            
            body.position = (
                (body.position[0] + phys.velocity[0]),
                (body.position[1] + phys.velocity[1]),
                (body.position[2] + phys.velocity[2]))
            

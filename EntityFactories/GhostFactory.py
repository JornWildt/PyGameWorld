from ECS.Entity import Entity
from SimpleComponents.NameComponent import NameComponent
from Physics.PhysicsComponent import PhysicsComponent
from Physics.RandomMovementComponent import RandomMovementComponent
from Rendering.SpriteComponent import SpriteComponent


class GhostFactory:
    
    @classmethod
    def build_a_ghost(self, name, x,y):
        ghost = Entity(id = None, components = [
            NameComponent(name),
            PhysicsComponent((x,y), (1,0)),
            RandomMovementComponent(),
            SpriteComponent('ghost')
        ])

        return ghost

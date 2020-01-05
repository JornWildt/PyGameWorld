from ECS.Entity import Entity
from SimpleComponents.NameComponent import NameComponent
from Physics.PositionComponent import PositionComponent
from Physics.PhysicsComponent import PhysicsComponent
from Physics.RandomMovementComponent import RandomMovementComponent
from Rendering.SpriteComponent import SpriteComponent


class GhostFactory:
    
    @classmethod
    def build_a_ghost(self, name, x,y):
        ghost = Entity([
            NameComponent(name),
            PositionComponent((x,y,1)),
            PhysicsComponent((0,0,0), (0.001, 0.001, 0.001)),
            # PhysicsComponent((0,0,0), (0,0,0)), #(0.001, 0.001, 0.001)),
            RandomMovementComponent(),
            SpriteComponent('ghost')
        ])

        return ghost

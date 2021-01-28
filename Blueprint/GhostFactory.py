from Core.ECS.Entity import Entity
from Core.SimpleComponents.NameComponent import NameComponent
from Core.Physics.BodyComponent import BodyComponent
from Core.Physics.PhysicsComponent import PhysicsComponent
from Core.Rendering.SpriteComponent import SpriteComponent
from .BallMovementComponent import BallMovementComponent
from .PlayerMovementComponent import PlayerMovementComponent


class GhostFactory:
    
    @classmethod
    def build_a_ghost(self, name, x,y):
        ghost = Entity([
            NameComponent(name),
            BodyComponent((x,y,1), (0.9, 0.9, 0.9)),
            PhysicsComponent((0,0,0), (0.001, 0.001, 0.0)),
            # PhysicsComponent((0,0,0), (0,0,0)), #(0.001, 0.001, 0.001)),
            BallMovementComponent(),
            SpriteComponent('ghost')
        ], True)
        return ghost

    
    @classmethod
    def build_a_ball(self, name, x,y):
        ball = Entity([
            NameComponent(name),
            BodyComponent((x,y,1), (0.99,0.99,0.99)),
            PhysicsComponent((0,0,0), (0.001, 0.001, 0)),
            # PhysicsComponent((0,0,0), (0,0,0)), #(0.001, 0.001, 0.001)),
            BallMovementComponent(),
            SpriteComponent('ball')
        ], True)
        return ball

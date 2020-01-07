from ECS.Entity import Entity
from SimpleComponents.NameComponent import NameComponent
from Physics.BodyComponent import BodyComponent
from Physics.PhysicsComponent import PhysicsComponent
from Physics.RandomMovementComponent import RandomMovementComponent
from Physics.BallMovementComponent import BallMovementComponent
from Rendering.SpriteComponent import SpriteComponent
from .PlayerMovementComponent import PlayerMovementComponent


class GhostFactory:
    
    @classmethod
    def build_a_ghost(self, name, x,y):
        ghost = Entity([
            NameComponent(name),
            BodyComponent((x,y,1)),
            PhysicsComponent((0,0,0), (0.001, 0.001, 0.001)),
            # PhysicsComponent((0,0,0), (0,0,0)), #(0.001, 0.001, 0.001)),
            RandomMovementComponent(),
            SpriteComponent('ghost')
        ])
        return ghost

    
    @classmethod
    def build_a_ball(self, name, x,y):
        ball = Entity([
            NameComponent(name),
            BodyComponent((x,y,1), (1,1,1)),
            PhysicsComponent((0,0,0), (0.001, 0.001, 0)),
            # PhysicsComponent((0,0,0), (0,0,0)), #(0.001, 0.001, 0.001)),
            BallMovementComponent(),
            SpriteComponent('ball')
        ])
        return ball
    
    @classmethod
    def build_a_player(self, name, x,y):
        player = Entity([
            NameComponent(name),
            BodyComponent((x,y,1), (0.9,0.9,2.9)),
            PhysicsComponent((0,0,0), (0, 0, 0)),
            PlayerMovementComponent(),
            SpriteComponent('player')
        ])
        return player

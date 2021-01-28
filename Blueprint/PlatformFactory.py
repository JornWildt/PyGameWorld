from Core.ECS.Entity import Entity
from Core.SimpleComponents.NameComponent import NameComponent
from Core.Physics.BodyComponent import BodyComponent
from Core.Physics.PhysicsComponent import PhysicsComponent
from Core.Rendering.SpriteComponent import SpriteComponent
from .PlayerMovementComponent import PlayerMovementComponent
from .BallMovementComponent import BallMovementComponent
from .PlatformMovementComponent import PlatformMovementComponent


def build_a_platform(name, pos):
    route = [(0, 0.01, 400), (2, 0.01, 100), (4, 0.01, 400), (6, 0.01, 100)]
    vector = PlatformMovementComponent.direction_vectors[route[0][0]]
    platform = Entity([
        NameComponent(name),
        BodyComponent(pos, (0.99,0.99,0.99)),
        PhysicsComponent((vector[0] * route[0][1], vector[1] * route[0][1], 0), (0,0,0)),
        PlatformMovementComponent(route),
        SpriteComponent('platform')
    ], True)
    return platform

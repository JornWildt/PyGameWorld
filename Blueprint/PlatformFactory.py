from Core.ECS.Entity import Entity
from Core.SimpleComponents.NameComponent import NameComponent
from Core.Physics.BodyComponent import BodyComponent
from Core.Physics.PhysicsComponent import PhysicsComponent
from Core.Rendering.SpriteComponent import SpriteComponent
from .PlayerMovementComponent import PlayerMovementComponent
from .BallMovementComponent import BallMovementComponent
from .PlatformMovementComponent import PlatformMovementComponent
from Blueprint.Constants import Constants


def build_a_platform(name, pos, route = None):

    # Route is (direction, speed, distance)
    if route == None:
        route = [(0, 0.01, 4), (2, 0.01, 1), (4, 0.01, 4), (6, 0.01, 1)]

    # Convert distance to step count (distance / speed)
    for i, leg in enumerate(route):
        route[i] = (leg[0], leg[1], leg[2] / leg[1])

    vector = Constants.direction_vectors[route[0][0]]
    platform = Entity([
        NameComponent(name),
        BodyComponent(pos, (1,1,1)),
        PhysicsComponent((vector[0] * route[0][1], vector[1] * route[0][1], 0), (0,0,0)),
        PlatformMovementComponent(route, pos),
        SpriteComponent('platform')
    ], True)
    return platform

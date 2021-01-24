from Core.ECS.Entity import Entity
from Core.SimpleComponents.NameComponent import NameComponent
from Core.Physics.BodyComponent import BodyComponent
from Core.Physics.PhysicsComponent import PhysicsComponent
from Core.Rendering.SpriteComponent import SpriteComponent
from .PlayerMovementComponent import PlayerMovementComponent


def build_a_player(name, x,y):
    player = Entity([
        NameComponent(name),
        BodyComponent((x,y,1), (0.5,0.5,2)),
        PhysicsComponent((0,0,0), (0,0,0)),
        PlayerMovementComponent(),
        SpriteComponent('player_3')
    ])
    return player

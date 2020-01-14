import pygame
import pyganim
from GameSettings import GameSettings
from Core.GameEnvironment import GameEnvironment
from Core.ECS.SystemsRepository import SystemsRepository
from Core.ECS.EntityRepository import EntityRepository
from Core.ECS.Entity import Entity
from Core.MessageBus import MessageBus
from Core.SimpleComponents.NameComponent import NameComponent
from Core.Physics.PhysicsSystem import PhysicsSystem
from Core.Physics.CollisionMap import CollisionMap
from Core.Physics.CollisionDetectionSystem import CollisionDetectionSystem
from Core.Rendering.DisplaySystem import DisplaySystem
from Core.Rendering.DisplayComponent import DisplayComponent
from Core.Rendering.SpriteSheet import SpriteSheet
#from Core.Rendering.ExtPygAnimation import ExtPygAnimation
from Core.Scene.Scene import Scene
from Core.AssetsManager import AssetsManager
from Blueprint.GhostFactory import GhostFactory
from Blueprint.Scenes.Scene_A1_Builder import Scene_A1_Builder
from Blueprint.Scenes.Scene_A2_Builder import Scene_A2_Builder
from Blueprint.PlayerMovementSystem import PlayerMovementSystem
from Blueprint.BallMovementSystem import BallMovementSystem
from Blueprint.GameEngine2 import GameEngine2


settings = GameSettings()

pygame.init()

screen = pygame.display.set_mode((settings.window_width, settings.window_height))
#screen = pygame.display.set_mode(flags = pygame.FULLSCREEN)

pygame.display.set_caption(settings.window_caption)


assets = AssetsManager(settings)
assets.load_from_directory("Assets")

entities = EntityRepository()

#entities.add_entity(GhostFactory.build_a_ghost('Mam', 6,6))

#entities.add_entity(GhostFactory.build_a_ball('Bam', 2,2))
#entities.add_entity(GhostFactory.build_a_ball('Bam', 5,4))
player_entity = entities.add_entity(GhostFactory.build_a_player('Mum', 2,2))


game_environment = GameEnvironment(settings)
message_bus = MessageBus(game_environment)

systems = SystemsRepository()
systems.add(PhysicsSystem())
systems.add(CollisionDetectionSystem())
systems.add(BallMovementSystem(message_bus))
systems.add(PlayerMovementSystem(message_bus))
systems.add(DisplaySystem())

scene = Scene(settings)
collision_map = CollisionMap(settings)

game_environment.scene = scene
game_environment.collision_map = collision_map
game_environment.assets = assets
game_environment.message_bus = message_bus
game_environment.screen = screen
game_environment.player_entity = player_entity
game_environment.systems_repository = systems
game_environment.entities_repository = entities

Scene_A1_Builder(game_environment).build_scene()

sceneDisplay = Entity([
    NameComponent('Scene render'),
    DisplayComponent(scene)
])
entities.add_entity(sceneDisplay)


message_bus.subscribe('new_scene', GameEngine2.on_new_scene)

game = GameEngine2(settings, game_environment)
game.run_game_loop()

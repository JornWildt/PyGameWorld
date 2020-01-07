import pygame
import pyganim
from GameSettings import GameSettings
from ECS.GameEnvironment import GameEnvironment
from ECS.GameEngine import GameEngine
from ECS.SystemsRepository import SystemsRepository
from ECS.EntityRepository import EntityRepository
from ECS.Entity import Entity
from ECS.MessageBus import MessageBus
from SimpleComponents.NameComponent import NameComponent
from Physics.PhysicsSystem import PhysicsSystem
from Physics.RandomMovementSystem import RandomMovementSystem
from Physics.BallMovementSystem import BallMovementSystem
from Physics.CollisionDetectionSystem import CollisionDetectionSystem
from Rendering.DisplaySystem import DisplaySystem
from Rendering.DisplayComponent import DisplayComponent
from Blueprint.GhostFactory import GhostFactory
from Blueprint.SceneBuilder import SceneBuilder
from Blueprint.InputHandler import InputHandler
from Rendering.SpriteSheet import SpriteSheet
from Rendering.ExtPygAnimation import ExtPygAnimation
from Scene.Scene import Scene

pygame.init()

settings = GameSettings()

screen = pygame.display.set_mode((settings.window_width, settings.window_height))
#screen = pygame.display.set_mode(flags = pygame.FULLSCREEN)

pygame.display.set_caption("World")

barrels_sprites = SpriteSheet("OriginalPixelArt/JW/barrel3D.png")
barrels_sprites.define("barrel", (0,0,48,48))
barrel = barrels_sprites.get('barrel')

stub_sprites = SpriteSheet("OriginalPixelArt/JW/Stub3D.png")
stub_sprites.define("stub", (0,0,64,64))
stub = stub_sprites.get('stub')

furniture_sprites = SpriteSheet("OriginalPixelArt/JW/furniture3D.png")
furniture_sprites.define("box", (0,0,64,64))
box = furniture_sprites.get('box')

floor_sprites = SpriteSheet("OriginalPixelArt/JW/Floor3D.png")
floor_sprites.define("floor1", (0,0,64,64))
floor_sprites.define("floor2", (0,0,64,64))
floor_sprites.define("floor_wall", (64,0,64,64))
floor1 = floor_sprites.get('floor1')
floor2 = floor_sprites.get('floor2')

ghostImages = pyganim.getImagesFromSpriteSheet("OriginalPixelArt/JW/Ghost3D.png", rows=1, cols=1, rects=[])
ghostFrames = list(zip(ghostImages, [100] * len(ghostImages)))
ghostAnim = ExtPygAnimation(settings, ghostFrames)
ghostAnim.play()

ballImages = pyganim.getImagesFromSpriteSheet("OriginalPixelArt/JW/Ball3D.png", rows=1, cols=3, rects=[])
ballFrames = list(zip(ballImages, [100] * len(ballImages)))
ballAnim = ExtPygAnimation(settings, ballFrames)
ballAnim.play()

playerImages = pyganim.getImagesFromSpriteSheet("OriginalPixelArt/JW/Player.png", rows=1, cols=1, rects=[])
playerFrames = list(zip(playerImages, [100] * len(playerImages)))
playerAnim = ExtPygAnimation(settings, playerFrames, (1,1,3))
#playerAnim = pyganim.PygAnimation(playerFrames)
playerAnim.play()

scene = Scene(settings)
scene_sprites = {
    'floor': floor1,
    'floor_wall': floor_sprites.get('floor_wall'),
    'wall': box,
    'box': box,
    'barrel': stub,
    'ghost': ghostAnim,
    'ball': ballAnim,
    'player': playerAnim
}

SceneBuilder.build_scene1(scene, scene_sprites)

clock = pygame.time.Clock()

message_bus = MessageBus()

systems = SystemsRepository()
systems.add(PhysicsSystem())
systems.add(CollisionDetectionSystem())
systems.add(RandomMovementSystem())
systems.add(BallMovementSystem(message_bus))
# Display registered last! Ensures other systems can register as displayable for rendering
systems.add(DisplaySystem())

entities = EntityRepository()

game_environment = GameEnvironment()
game_environment.systems_repository = systems
game_environment.entities_repository = entities
game_environment.sprites = scene_sprites
game_environment.scene = scene
game_environment.screen = screen
game_environment.message_bus = message_bus

game_environment.message_bus.subscribe('key_down', InputHandler.on_key_down)
game_environment.message_bus.subscribe('key_up', InputHandler.on_key_up)

game = GameEngine(settings, game_environment)

#entities.add_entity(GhostFactory.build_a_ghost('Mam', 6,6))

entities.add_entity(GhostFactory.build_a_ball('Bam', 2,2))
# entities.add_entity(GhostFactory.build_a_ball('Bam', 5,4))
#entities.add_entity(GhostFactory.build_a_player('Mum', 2,3))

sceneDisplay = Entity([
    NameComponent('Main scene'),
    DisplayComponent(scene)
])
entities.add_entity(sceneDisplay)

game.run_game_loop()

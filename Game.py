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
from Physics.BallMovementSystem import BallMovementSystem
from Physics.CollisionMap import CollisionMap
from Physics.CollisionDetectionSystem import CollisionDetectionSystem
from Rendering.DisplaySystem import DisplaySystem
from Rendering.DisplayComponent import DisplayComponent
from Blueprint.GhostFactory import GhostFactory
from Blueprint.SceneBuilder import SceneBuilder
from Blueprint.PlayerMovementSystem import PlayerMovementSystem
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

scene_sprites = {
    'floor': floor1,
    'floor_wall': floor_sprites.get('floor_wall'),
    'wall': box,
    'box': box,
    'barrel': stub,
    'ghost': ghostAnim,
    'ball': ballAnim
}

pillar_sprites = SpriteSheet("OriginalPixelArt/JW/1x1Pilar3D.png")
pillar_sprites.define("pillar", (0,0,64,64))
pillar = pillar_sprites.get('pillar')

playerAnimations = []
playerSpritesheet =  SpriteSheet("OriginalPixelArt/JW/Player.png")
for d in range(0,8):
    playerImages = []
    for f in range(0,1):
        #image = pillar
        image = playerSpritesheet.image_at((f*64,d*96,64,96))
        playerImages.append(image)
    playerFrames = list(zip(playerImages, [100] * len(playerImages)))
    playerAnim = ExtPygAnimation(settings, playerFrames, (1,1,2))
    playerAnim.play()
    playerAnimations.append(playerAnim)
    scene_sprites['player_' + str(d)] = playerAnim

entities = EntityRepository()

#entities.add_entity(GhostFactory.build_a_ghost('Mam', 6,6))

#entities.add_entity(GhostFactory.build_a_ball('Bam', 2,2))
#entities.add_entity(GhostFactory.build_a_ball('Bam', 5,4))
player_entity = entities.add_entity(GhostFactory.build_a_player('Mum', 2,2))

scene = Scene(settings)
SceneBuilder.build_scene1(scene, scene_sprites)

sceneDisplay = Entity([
    NameComponent('Main scene'),
    DisplayComponent(scene)
])
entities.add_entity(sceneDisplay)



collision_map = CollisionMap(settings, scene)

message_bus = MessageBus()

systems = SystemsRepository()
systems.add(PhysicsSystem())
systems.add(CollisionDetectionSystem())
systems.add(BallMovementSystem(message_bus))
systems.add(PlayerMovementSystem(message_bus))
# Display registered last! Ensures other systems can register as displayable for rendering
systems.add(DisplaySystem())

game_environment = GameEnvironment()
game_environment.player_entity = player_entity
game_environment.systems_repository = systems
game_environment.entities_repository = entities
game_environment.sprites = scene_sprites
game_environment.scene = scene
game_environment.screen = screen
game_environment.collision_map = collision_map
game_environment.message_bus = message_bus

game = GameEngine(settings, game_environment)

game.run_game_loop()

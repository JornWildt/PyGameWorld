import pygame
import pyganim
from GameSettings import GameSettings
from Core.GameEnvironment import GameEnvironment
#from Core.ECS.GameEngine import GameEngine
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
from Core.Rendering.ExtPygAnimation import ExtPygAnimation
from Core.Scene.Scene import Scene
from Core.AssetsManager import AssetsManager
from Blueprint.GhostFactory import GhostFactory
from Blueprint.Scenes.Scene_A1_Builder import Scene_A1_Builder
from Blueprint.Scenes.Scene_A2_Builder import Scene_A2_Builder
from Blueprint.PlayerMovementSystem import PlayerMovementSystem
from Blueprint.BallMovementSystem import BallMovementSystem
from Blueprint.GameEngine2 import GameEngine2


settings = GameSettings()


def load_animation(filename, rows, cols):
    images = pyganim.getImagesFromSpriteSheet(filename, rows=rows, cols=cols, rects=[])
    frames = list(zip(images, [100] * len(images)))
    anim = pyganim.PygAnimation(frames)
    anim.play()
    return anim


def load_ext_animation(filename, rows, cols):
    images = pyganim.getImagesFromSpriteSheet(filename, rows=rows, cols=cols, rects=[])
    frames = list(zip(images, [100] * len(images)))
    anim = ExtPygAnimation(settings, frames)
    return anim


pygame.init()


screen = pygame.display.set_mode((settings.window_width, settings.window_height))
#screen = pygame.display.set_mode(flags = pygame.FULLSCREEN)

pygame.display.set_caption(settings.window_caption)


assets = AssetsManager()
assets.load_from_directory("Assets")


# stub_sprites = SpriteSheet("Assets/Random/Stub3D.png")
# stub_sprites.define("stub", (0,0,64,64))
# stub = stub_sprites.get('stub')

# furniture_sprites = SpriteSheet("Assets/Random/furniture3D.png")
# furniture_sprites.define("box", (0,0,64,64))
# box = furniture_sprites.get('box')

# floor_sprites = SpriteSheet("Assets/Random/Floor3D.png")
# floor_sprites.define("floor1", (0,0,64,64))
# floor_sprites.define("floor_wall", (64,0,64,64))
# floor1 = floor_sprites.get('floor1')

# ghostImages = pyganim.getImagesFromSpriteSheet("Assets/Random/Ghost3D.png", rows=1, cols=1, rects=[])
# ghostFrames = list(zip(ghostImages, [100] * len(ghostImages)))
# ghostAnim = ExtPygAnimation(settings, ghostFrames)
# ghostAnim.play()

# ballImages = pyganim.getImagesFromSpriteSheet("Assets/Random/Ball3D.png", rows=1, cols=3, rects=[])
# ballFrames = list(zip(ballImages, [100] * len(ballImages)))
# ballAnim = ExtPygAnimation(settings, ballFrames)
# ballAnim.play()

# teleport_sprite = load_animation("Assets/Random/Teleport3D.png", 1, 6)

scene_sprites = {
    'floor': assets.get('floor'),
    'floor_wall': assets.get('floor_wall'),
    'wall': assets.get('box'),
    'box': assets.get('box'),
    'barrel': assets.get('box'),
    # 'ghost': ghostAnim,
    # 'ball': ballAnim,
    'teleport': assets.get('teleport')
}

# pillar_sprites = SpriteSheet("Assets/Random/1x1Pilar3D.png")
# pillar_sprites.define("pillar", (0,0,64,64))
# pillar = pillar_sprites.get('pillar')

playerAnimations = []
playerSpritesheet =  SpriteSheet("Assets/Random/Player.png")
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
game_environment.sprites = scene_sprites
game_environment.message_bus = message_bus
game_environment.screen = screen
game_environment.player_entity = player_entity
game_environment.systems_repository = systems
game_environment.entities_repository = entities

Scene_A1_Builder(game_environment).build_scene()

sceneDisplay = Entity([
    NameComponent('Main scene'),
    DisplayComponent(scene)
])
entities.add_entity(sceneDisplay)


message_bus.subscribe('new_scene', GameEngine2.on_new_scene)

game = GameEngine2(settings, game_environment)
game.run_game_loop()

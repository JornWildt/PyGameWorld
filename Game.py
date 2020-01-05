﻿import pygame
import pyganim
from GameSettings import GameSettings
from ECS.GameEnvironment import GameEnvironment
from ECS.GameEngine import GameEngine
from ECS.SystemsRepository import SystemsRepository
from ECS.EntityRepository import EntityRepository
from ECS.Entity import Entity
from SimpleComponents.NameComponent import NameComponent
from Physics.PhysicsSystem import PhysicsSystem
from Physics.RandomMovementSystem import RandomMovementSystem
from Rendering.DisplaySystem import DisplaySystem
from Rendering.DisplayComponent import DisplayComponent
from Blueprint.GhostFactory import GhostFactory
from Blueprint.SceneBuilder import SceneBuilder
from Rendering.SpriteSheet import SpriteSheet
from Scene.Scene import Scene

pygame.init()

settings = GameSettings()

screen = pygame.display.set_mode((settings.window_width, settings.window_height))
#screen = pygame.display.set_mode(flags = pygame.FULLSCREEN)

pygame.display.set_caption("World")

barrels_sprites = SpriteSheet("OriginalPixelArt/JW/barrel3D.png")
barrels_sprites.define("barrel", (0,0,48,48))
barrel = barrels_sprites.get('barrel')

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
ghostAnim = pyganim.PygAnimation(ghostFrames)
ghostAnim.play()

scene = Scene(settings)
scene_sprites = {
    'floor': floor1,
    'floor_wall': floor_sprites.get('floor_wall'),
    'wall': box,
    'box': box,
    'barrel': barrel,
    'ghost': ghostAnim
}

SceneBuilder.build_scene1(scene, scene_sprites)

clock = pygame.time.Clock()

systems = SystemsRepository()
systems.add(PhysicsSystem())
systems.add(RandomMovementSystem())
# Display registered last! Ensures other systems can register as displayable for rendering
systems.add(DisplaySystem())

entities = EntityRepository()

game_environment = GameEnvironment()
game_environment.systems_repository = systems
game_environment.entities_repository = entities
game_environment.sprites = scene_sprites
game_environment.scene = scene
game_environment.screen = screen

game = GameEngine(settings, game_environment)

ghost = GhostFactory.build_a_ghost('Mammo', 3,3)
entities.add_entity(ghost)

entities.add_entity(GhostFactory.build_a_ghost('Mammi', 8,8))
entities.add_entity(GhostFactory.build_a_ghost('Mammy', 8,6))
entities.add_entity(GhostFactory.build_a_ghost('Mam', 6,6))

sceneDisplay = Entity([
    NameComponent('Main scene'),
    DisplayComponent(scene)
])
entities.add_entity(sceneDisplay)

game.run_game_loop()

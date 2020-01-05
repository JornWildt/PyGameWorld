import pygame
import pyganim
import sys
import random
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
from Rendering.VisualComponent import VisualComponent
from EntityFactories.GhostFactory import GhostFactory

from Tile import Tile
from Tileset import Tileset
from SpriteSheet import SpriteSheet
from Scene import Scene

pygame.init()

settings = GameSettings()

screen = pygame.display.set_mode((settings.window_width, settings.window_height))
#screen = pygame.display.set_mode(flags = pygame.FULLSCREEN)

pygame.display.set_caption("World")

all_sprites_list = pygame.sprite.Group()


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

scene_src = '''
XXXXXXXXXXXX
x..........X
x..........X
x..........X
x..........X
x..........X
XXXXXXXX*XXX
x...b.....BX
x...b......X
x..........X
x...bbb..b.X
x........b.X
x..........X
xxxxxxxxxxxx
'''

scene_sprites = {
    'floor': floor1,
    'floor_wall': floor_sprites.get('floor_wall'),
    'wall': box,
    'box': box,
    'barrel': barrel,
    'ghost': ghostAnim
}

scene.load_scene_from_string(scene_src, scene_sprites)

clock = pygame.time.Clock()

player_x = 400
player_y = 300


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

sceneVisual = Entity(components = [
    NameComponent('Main scene'),
    VisualComponent(scene)
])
entities.add_entity(sceneVisual)


game.run_game_loop()

1/0

while True:
    # Event processing here, stuff the users does.
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= 1
            if event.key == pygame.K_RIGHT:
                player_x += 1
            if event.key == pygame.K_UP:
                player_y -= 1
            if event.key == pygame.K_DOWN:
                player_y += 1

    for ent in all_sprites_list:
        ent.update()

    screen.fill(pygame.Color("black"))
    #map.draw(screen, player_x,player_y, settings.map_width_tiles, settings.map_height_tiles)

    player_x += 1
    if player_x > 600:
        player_x = 400

    # for bx in range(16):
    #     for by in range(10):
    #         bxpos = (bx+by) * 32 + settings.window_width/2 - 400
    #         bypos = (by-bx) * 16 + settings.window_height/2 - 100
    #         floor = floor1 if (bx+by) % 2 == 0 else floor2
    #         screen.blit(floor, (bxpos,bypos))

    # for bx in range(16,0,-1):
    #     for by in range(10):
    #         if (bx+1) % 4 != 0 and (by+1) % 4 != 0:
    #             bxpos = (bx+by) * 32 + settings.window_width/2 - 400
    #             bypos = (by-bx) * 16 + settings.window_height/2 - 100
    #             screen.blit(box, (bxpos,bypos))

    scene.draw(screen)

    ghostAnim.blit(screen, (player_x,player_y))

    all_sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(settings.FPS)

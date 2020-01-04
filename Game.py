﻿import pygame
import pyganim
import sys
import random
from GameSettings import GameSettings
from Tile import Tile
from Tileset import Tileset
from SpriteSheet import SpriteSheet
from Scene import Scene

pygame.init()

settings = GameSettings()

screen = pygame.display.set_mode((settings.window_width, settings.window_height))

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

ghostImages = pyganim.getImagesFromSpriteSheet("OriginalPixelArt/JW/Ghost.png", rows=1, cols=5, rects=[])
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
    'barrel': barrel
}

scene.load_scene_from_string(scene_src, scene_sprites)

clock = pygame.time.Clock()

player_x = 400
player_y = 300

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

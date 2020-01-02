import pygame
import sys
import random
from GameSettings import GameSettings
from Tile import Tile
from Tileset import Tileset
from SpriteSheet import SpriteSheet
from Map import Map
from MapGenerator import MapGenerator

pygame.init()

settings = GameSettings()

screen = pygame.display.set_mode((settings.window_width, settings.window_height))

pygame.display.set_caption("World")

all_sprites_list = pygame.sprite.Group()

world_sprites = SpriteSheet("OriginalPixelArt\ArMM1998-Zelda\Overworld.png")
world_sprites.define('background', (16,0,16,16))
world_sprites.define('grass', (0,0,16,16))
world_sprites.define('grass_water_NW', (32,96,16,16))
world_sprites.define('grass_water_N', (32+16,96,16,16))
world_sprites.define('grass_water_NE', (32+32,96,16,16))
world_sprites.define('grass_water_W', (32,96+16,16,16))
world_sprites.define('grass_water_C', (32+16,96+16,16,16))
world_sprites.define('grass_water_E', (32+32,96+16,16,16))
world_sprites.define('grass_water_SW', (32,96+32,16,16))
world_sprites.define('grass_water_S', (32+16,96+32,16,16))
world_sprites.define('grass_water_SE', (32+32,96+32,16,16))
world_sprites.define('water_grass_NW', (32,144,16,16))
world_sprites.define('water_grass_NE', (32+16,144,16,16))
world_sprites.define('water_grass_SW', (32,144+16,16,16))
world_sprites.define('water_grass_SE', (32+16,144+16,16,16))

mapGenerator = MapGenerator(settings, world_sprites)
map = mapGenerator.generate()

clock = pygame.time.Clock()

player_x = 10
player_y = 10

while True:
    # Event processing here, stuff the users does.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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
    map.draw(screen, player_x,player_y, settings.map_width_tiles, settings.map_height_tiles)
    
    all_sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(settings.FPS)

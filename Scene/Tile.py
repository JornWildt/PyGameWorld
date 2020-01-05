import pygame

class Tile():

    def __init__(self, tile_type, image):
        self.tile_type = tile_type
        self.image = image


    def draw(self, screen, xpos, ypos):
        screen.blit(self.image, (xpos, ypos))

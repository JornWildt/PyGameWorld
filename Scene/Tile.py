import pygame

class Tile():

    def __init__(self, pos, tile_type, image):
        self.position = pos
        self.tile_type = tile_type
        self.image = image


    # def draw(self, screen, xpos, ypos):
    #     screen.blit(self.image, (xpos, ypos))

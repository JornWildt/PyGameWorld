import pygame

class Tile():

    def __init__(self, pos, tile_type, sprite, image):
        self.position = pos
        self.size = (1,1,1)
        self.tile_type = tile_type
        self.sprite = sprite
        self.image = image


    # def draw(self, screen, xpos, ypos):
    #     screen.blit(self.image, (xpos, ypos))

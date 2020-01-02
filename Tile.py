import pygame

class Tile():

    def __init__(self, height, tile_type, image_width, image_height, image, xpixels, ypixels):
        self.tile_type = tile_type
        self.height = height
        self.image = pygame.transform.scale(image, (xpixels, ypixels))


    def draw(self, screen, xpos, ypos):
        ts = self.image.get_size()
        screen.blit(self.image, (xpos, ypos))

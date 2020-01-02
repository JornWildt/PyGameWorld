import pygame

class Entity(pygame.sprite.Sprite):
    """Inherited by any object in the game."""
 
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
 
        self.x = x
        self.y = y
        self.width = width
        self.height = height
 
        # This makes a rectangle around the entity, used for anything
        # from collision to moving around.
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
 
 

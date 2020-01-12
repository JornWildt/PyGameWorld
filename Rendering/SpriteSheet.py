import pygame;


class SpriteSheet:

    def __init__(self, filename):
        """Load the image sprite sheet from file."""
        try:
            self.sheet = pygame.image.load(filename).convert_alpha()
        except pygame.error as e:
            print(f"Unable to load sprite sheet image: {filename}")
            raise SystemExit(e)

        self.sprites = {}

    
    def image_at(self, rectangle, colorkey = None):
        """Load a specific image from a specific rectangle."""
        # Loads image from x, y, x+offset, y+offset.
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size, pygame.SRCALPHA)
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    
    def define(self, name, sprite_rect):
        r = pygame.Rect(sprite_rect)
        image = self.image_at(r)
        self.sprites[name] = image


    def get(self, name):
        return self.sprites[name]

import pygame

def show_text(screen, text, pos):
    myfont = pygame.font.SysFont(None, 30)
    text_surface = myfont.render(text, False, (255,255,255))
    screen.blit(text_surface, pos)

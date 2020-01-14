import pygame


def fade_screen(screen):
    veil = pygame.Surface((screen.get_size()))
    veil.fill((0,0,0))
    for alpha in range(0, 50):
        veil.set_alpha(20)
        #
        screen.blit(veil, (0,0))

        pygame.display.flip()
        pygame.time.delay(10)

        
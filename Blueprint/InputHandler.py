import pygame

class InputHandler:

    direction = 0
    intent = None    

    def on_key_down(event):
        # InputHandler.intent = None

        if event.key == pygame.K_UP:
            InputHandler.intent = 'Forward'
        elif event.key == pygame.K_RIGHT:
            InputHandler.intent = 'Right'
        elif event.key == pygame.K_LEFT:
            InputHandler.intent = 'Left'
        elif event.key == pygame.K_DOWN:
            InputHandler.intent = 'Backward'
        elif event.key == pygame.K_SPACE:
            InputHandler.intent = 'Stop'
        # elif event.key == pygame.K_RIGHT:
        #     direction = (direction + 1) % 16
        # elif event.key == pygame.K_LEFT:
        #     direction = (direction - 1) % 16

    def on_key_up(event):
        InputHandler.intent = None

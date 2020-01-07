import pygame
import sys

class GameEngine:
    def __init__(self, settings, game_environment):
        self.settings = settings
        self.game_environment = game_environment

    
    def run_game_loop(self):
        
        clock = pygame.time.Clock()

        while True:
            # Event processing here, stuff the users does.
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.game_environment.message_bus.publish('key_down', event)
                elif event.type == pygame.KEYUP:
                    self.game_environment.message_bus.publish('key_up', event)

            self.game_environment.scene.start_frame()

            for system in self.game_environment.systems_repository.get_all():
                self.game_environment.message_bus.dispatch_messages()
                system.update(self.game_environment)

            pygame.display.flip()

            clock.tick(self.settings.FPS)



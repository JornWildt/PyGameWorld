import pygame
import sys
from Utility import Texts

class GameEngine:
    def __init__(self, settings, game_environment):
        self.settings = settings
        self.game_environment = game_environment

    
    def run_game_loop(self):
        
        clock = pygame.time.Clock()
        frame_time = 0

        while True:
            
            self.game_environment.screen.fill((0,0,0))

            self.on_frame_start()
            
            # Event processing here, stuff the users does.
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()

            self.game_environment.scene.start_frame()

            self.on_frame_start()

            for system in self.game_environment.systems_repository.get_all():
                self.game_environment.message_bus.dispatch_messages()
                system.update(self.game_environment)

            # Debug, show frame time
            Texts.show_text(self.game_environment.screen, str(frame_time), (10,10))

            pygame.display.flip()

            self.on_frame_end()

            frame_time = clock.tick(self.settings.FPS)


    
    def on_frame_start(self):
        pass

    
    def on_frame_end(self):
        pass
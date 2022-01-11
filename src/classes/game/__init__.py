from .player import Player
from ...utils.colors import BLACK
from ...utils.constants import GAME_NAME, FPS, VALKYRIE
from .settings import Settings
import sys, pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

"""
Game
====

A class to handle all in-game logic.
"""
class Game:
    def __init__(self):
        self.settings = Settings()
        self.size = (self.settings.settings.get("width"), self.settings.settings.get("height"))
        self.running = True
        self.chromaKey = pygame.Color(186, 254, 202)
        
        pygame.init()

        self.fpsClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(GAME_NAME)

    def _events(self):
        for event in pygame.event.get():
            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    self.running = False

            elif event.type == QUIT:
                self.running = False

    def start(self):
        # 1. criar personagem
        player = Player(VALKYRIE, self.chromaKey) # valor a mudar depois

        while self.running:
            self._events()
            
            # Handle key pressing
            pressed_keys = pygame.key.get_pressed()
            player.update(pressed_keys, self.settings.settings.get("width"), self.settings.settings.get("height"))

            # Show background and player
            self.screen.fill(BLACK)
            player.blitme(self.screen)

            pygame.display.flip()
            self.fpsClock.tick(FPS)
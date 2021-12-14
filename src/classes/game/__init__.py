from ...utils.colors import BLACK
from .settings import Settings
import sys, pygame

"""
Game
====

A class to handle all in-game logic.
"""
class Game:
    def __init__(self):
        self.settings = Settings()
        self.size = (self.settings.settings.get("width"), self.settings.settings.get("height"))
        print(self.size)

    def start(self):
        pygame.init()

        screen = pygame.display.set_mode(self.size)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            
            screen.fill(BLACK)
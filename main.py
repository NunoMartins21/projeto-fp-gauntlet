import sys, pygame
from src.utils.colors import BLACK

pygame.init()

size = width, height = 320, 240
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    screen.fill(BLACK)
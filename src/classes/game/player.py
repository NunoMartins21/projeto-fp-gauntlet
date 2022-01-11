from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP
from ...utils.spritesheet import SpriteSheet
from ...utils.exception_handler import exception_handler
from ...utils.constants import ELF, RIGHT, UP, DOWN, LEFT, VALKYRIE, WARRIOR, WIZARD
import pygame

class Player(pygame.sprite.Sprite):
    @exception_handler
    def __init__(self, character, colorKey):
        super(Player, self).__init__()

        # Default attributes
        self.character = character
        self.colorKey = colorKey
        self.images = {
            DOWN: None,
            LEFT: None,
            UP: None,
            RIGHT: None
        }
        self.x, self.y = (0.0, 0.0)

        # Load sprites
        self._load_sprites()

        # Character direction
        self.direction = DOWN

        self.rect = self.images[self.character][self.direction].get_rect()

    @exception_handler
    def _load_sprites(self):
        file = "./src/assets/player-sprites.png"
        ss = SpriteSheet(file)

        self.images = {
            VALKYRIE: {
                DOWN: ss.image_at((8, 174, 21, 18), self.colorKey),
                LEFT: ss.image_at((8, 203, 22, 23), self.colorKey),
                UP: ss.image_at((8, 233, 20, 23), self.colorKey),
                RIGHT: ss.image_at((8, 266, 23, 23), self.colorKey),
            },
            WIZARD: {
                DOWN: ss.image_at((8, 174, 21, 18), self.colorKey),
                LEFT: ss.image_at((8, 203, 22, 23), self.colorKey),
                UP: ss.image_at((8, 233, 20, 23), self.colorKey),
                RIGHT: ss.image_at((8, 266, 23, 23), self.colorKey),
            },
            ELF: {
                DOWN: ss.image_at((8, 174, 21, 18), self.colorKey),
                LEFT: ss.image_at((8, 203, 22, 23), self.colorKey),
                UP: ss.image_at((8, 233, 20, 23), self.colorKey),
                RIGHT: ss.image_at((8, 266, 23, 23), self.colorKey),
            },
            WARRIOR: {
                DOWN: ss.image_at((8, 174, 21, 18), self.colorKey),
                LEFT: ss.image_at((8, 203, 22, 23), self.colorKey),
                UP: ss.image_at((8, 233, 20, 23), self.colorKey),
                RIGHT: ss.image_at((8, 266, 23, 23), self.colorKey),
            },
        }

    def blitme(self, screen):
        """Draw the piece at its current location."""
        self.rect = self.images[self.character][self.direction].get_rect()
        self.rect.topleft = self.x, self.y
        screen.blit(self.images[self.character][self.direction], (self.x, self.y))

    @exception_handler
    def update(self, pressed_keys, width, height):
        if pressed_keys[K_UP]:
            self.direction = UP
            self.y -= 5
        if pressed_keys[K_DOWN]:
            self.direction = DOWN
            self.y += 5
        if pressed_keys[K_LEFT]:
            self.direction = LEFT
            self.x -= 5
        if pressed_keys[K_RIGHT]:
            self.direction = RIGHT
            self.x += 5

        # Keep player on the screen
        if self.x < 0:
            self.x = 0
        if self.x > width:
            self.x = width
        if self.y <= 0:
            self.y = 0
        if self.y >= height:
            self.y = height

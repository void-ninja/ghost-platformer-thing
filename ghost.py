import pygame
from settings import *

class Ghost(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.Surface((TILE_SIZE // 2, TILE_SIZE))
        self.image.fill(GHOST_COLOR)
        self.rect = self.image.get_rect(topleft = pos)
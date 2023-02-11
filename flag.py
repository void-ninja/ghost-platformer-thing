import pygame
from settings import *

class Flag(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
        self.image.fill(FLAG_COLOR)
        self.rect = self.image.get_rect(topleft = pos)
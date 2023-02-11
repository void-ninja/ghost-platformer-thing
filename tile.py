import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.transform.scale(pygame.image.load("art/brick.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft = pos)
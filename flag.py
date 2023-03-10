import pygame
from settings import *

class Flag(pygame.sprite.Sprite):
    def __init__(self,pos,image,groups):
        super().__init__(groups)
        self.image = pygame.transform.scale(image.convert_alpha(), (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft = pos).inflate(-20,-20)
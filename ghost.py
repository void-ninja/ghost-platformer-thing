import pygame
from settings import *
from debug import debug

class Ghost(pygame.sprite.Sprite):
    def __init__(self,pos,groups,path=[]):
        super().__init__(groups)
        self.image = pygame.image.load("art/ghost.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*4,self.image.get_height()*4))
        self.image.set_alpha(200)
        
        self.rect = self.image.get_rect(topleft = pos).inflate(-5,-20)
        
        self.path = path
        self.nodeNum = 0
        
        self.direction = pygame.math.Vector2()
        self.xSpeed = 5
        self.ySpeed = 5
    
    def update(self):  
        if self.nodeNum >= len(self.path):
            self.nodeNum = 0
            self.rect.center = self.path[0][0]
        
        dest = self.path[self.nodeNum]
        xDest = dest[0][0]
        yDest = dest[0][1]  
            
        self.nodeNum += 1
        self.rect.centerx = xDest # this stuff works bc I'm capturing the players position every frame
        self.rect.centery = yDest
            
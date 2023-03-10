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
        self.xSpeed = 6
        self.ySpeed = 6 
        
    def set_direction(self):
        dest = self.path[self.nodeNum]
        xDiff = self.rect.centerx - dest[0]
        yDiff = self.rect.centery - dest[1]
        if xDiff == 0:
            self.direction.x = 0
        elif xDiff > 0:
            self.direction.x = -1
        elif xDiff < 0:
            self.direction.x = 1
            
        if yDiff == 0:
            self.direction.y = 0
        elif yDiff > 0:
            self.direction.y = -1
        elif yDiff < 0:
            self.direction.y = 1
        
        if self.rect.centerx > dest[0]-30 and self.rect.centerx < dest[0]+30:
            if self.rect.centery > dest[1]-30 and self.rect.centery < dest[1]+30:
                if self.nodeNum < len(self.path)-1:
                    self.nodeNum += 1
                else:
                    self.nodeNum = 0
                    self.rect.center = self.path[0]
        
    def update(self):
        self.set_direction()
        self.direction.normalize()
        self.rect.centerx += self.direction.x * self.xSpeed
        self.rect.centery += self.direction.y * self.ySpeed
        
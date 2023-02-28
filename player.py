import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,collisionSprites,visibleSprites):
        super().__init__(groups)
        self.image = pygame.Surface((TILE_SIZE // 2, TILE_SIZE))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect(topleft = pos)
        
        self.direction = pygame.math.Vector2()
        self.speed = 7
        self.gravity = 0.8
        self.jumpHeight = 16
        self.collisionSprites = collisionSprites
        self.visibleSprites = visibleSprites
        self.onFloor = False
        
        
    def input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_d]: #right
            self.direction.x = 1
        elif keys[pygame.K_a]: #left
            self.direction.x = -1
        else:
            self.direction.x = 0
            
        if keys[pygame.K_SPACE] and self.onFloor: #jump
            self.direction.y = -self.jumpHeight
            
    def check_collisions(self):
        if self.rect.y > LEVEL_HEIGHT: #checks if you have fallen past the level
            pygame.event.post(pygame.event.Event(FELL_DOWN))
        
        #checks for level end (hit the flag)  
        for sprite in self.visibleSprites.sprites():
            if sprite.__class__.__name__ == "Flag" and sprite.rect.colliderect(self.rect):
                pygame.event.post(pygame.event.Event(FLAG_HIT))
                
        for sprite in self.collisionSprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left
                    
        self.apply_gravity() #important that it happens before vertical collisions
        
        for sprite in self.collisionSprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.onFloor = True
                if self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0

        if self.onFloor and self.direction.y != 0: #prevents double jumps
            self.onFloor = False
            
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.centery += self.direction.y
            
    def update(self):
        self.input()
        self.rect.centerx += self.direction.x * self.speed
        self.check_collisions()
        
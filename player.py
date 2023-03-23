import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,collisionSprites,visibleSprites):
        super().__init__(groups)        
        self.runFrames = []
        
        for i in range(1,9):
            image = pygame.image.load(f"./art/animations/player_animated_run{i}.png").convert_alpha()
            image = pygame.transform.scale_by(image, 4)
            self.runFrames.append(image)
        
        self.image = self.runFrames[0]
        self.rect = self.image.get_rect(topleft=pos) # used for drawing
        
        self.hitbox = self.rect.copy() # used for collision and moving
        self.hitbox.inflate_ip(-80,-40)
        
        self.runAnimation = False
        
        self.direction = pygame.math.Vector2()
        self.speed = 7
        self.gravity = 0.8
        self.jumpHeight = 16
        self.collisionSprites = collisionSprites
        self.visibleSprites = visibleSprites
        self.onFloor = False
        
        self.currentRunFrame = 0
        
        self.prevMoves = [] #list storing the moves from last level
        self.currentMoves = [] #list storing moves that are being made
        
    def input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_d]: #right
            self.direction.x = 1
            self.animate_run("right")
        elif keys[pygame.K_a]: #left
            self.direction.x = -1
            self.animate_run("left")
        else:
            self.direction.x = 0
            self.runAnimation = False
            
        if keys[pygame.K_SPACE] and self.onFloor: #jump
            self.direction.y = -self.jumpHeight
            
    def check_collisions(self):
        if self.hitbox.y > LEVEL_HEIGHT: #checks if you have fallen past the level
            pygame.event.post(pygame.event.Event(GAME_OVER))
                
        for sprite in self.collisionSprites.sprites():
            if sprite.rect.colliderect(self.hitbox):
                if self.direction.x < 0:
                    self.hitbox.left = sprite.rect.right
                if self.direction.x > 0:
                    self.hitbox.right = sprite.rect.left
                    
        self.apply_gravity() #important that it happens before vertical collisions
        
        for sprite in self.collisionSprites.sprites():
            if sprite.rect.colliderect(self.hitbox):
                if self.direction.y > 0:
                    self.hitbox.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.onFloor = True
                if self.direction.y < 0:
                    self.hitbox.top = sprite.rect.bottom
                    self.direction.y = 0

        if self.onFloor and self.direction.y != 0: #prevents double jumps
            self.onFloor = False
            
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.hitbox.centery += self.direction.y
        
    def save_pos(self):
        self.currentMoves.append([(self.rect.centerx,self.rect.centery),self.currentRunFrame,True]) # each nested list needs to have this: (x,y), currentAnimationFrame, killsPlayer
    
    def save_current_moves(self):   
        startX = self.currentMoves[0][0][0] # should be where the player starts from
        startY = self.currentMoves[0][0][1]
        for i in range(1,WAIT_FRAMES+1): # effectively makes the ghost come in from 4 seconds worth of frames away #! This will make it so the repeat takes a while to happen
            self.currentMoves.insert(0,[(startX, startY),0,False])
            
        self.prevMoves = self.currentMoves.copy()
        self.currentMoves.clear()
        
    def animate_run(self,direction):
        self.runAnimation = direction # can be either "right" or "left"
            
    def update(self):
        self.input()
        self.hitbox.centerx += self.direction.x * self.speed
        self.check_collisions()
        self.rect.center = self.hitbox.center
        
        if self.runAnimation == "right":
            self.currentRunFrame += 0.3
        elif self.runAnimation == "left":
            self.currentRunFrame -= 0.3
        else:
            self.currentRunFrame = 0
        
        if self.currentRunFrame >= len(self.runFrames):
            self.currentRunFrame = 0
            
        if self.currentRunFrame <= -len(self.runFrames):
            self.currentRunFrame = 0
        
        self.image = self.runFrames[int(self.currentRunFrame)]
        
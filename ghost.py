import pygame
from settings import *
from debug import debug

class Ghost(pygame.sprite.Sprite):
    def __init__(self,pos,groups,path=[]):
        super().__init__(groups)
        self.runFrames = []
        
        for i in range(1,9):
            image = pygame.image.load(f"./art/animations/ghost_animated_run{i}.png").convert_alpha()
            image = pygame.transform.scale_by(image, 4)
            image.set_alpha(220)
            self.runFrames.append(image)
        
        self.image = self.runFrames[0]
        
        self.rect = self.image.get_rect(topleft = pos).inflate(-5,-20)
        self.hitbox = self.rect.copy() # used for collision
        self.hitbox.inflate_ip(-50,-10)
        
        self.path = path
        self.nodeNum = 0
        
        self.direction = pygame.math.Vector2()
        self.xSpeed = 5
        self.ySpeed = 5
        
        self.killsPlayer = False
    
    def update(self):          
        # pathfinding stuff
        if self.nodeNum >= len(self.path): # this evaluates to true if the ghost has reached the end of the players path
            for i in range(1,WAIT_FRAMES + 1): # this makes it so that the ghost doesn't wait around before starting each repetition of the path after completing the first one. This is done by removing the frames that cause it to wait
                self.path.pop(self.path[0])
            self.nodeNum = 0
            self.rect.center = self.path[0][0]
            
        self.image = self.runFrames[int(self.path[self.nodeNum][1])] # animation
        
        self.killsPlayer = self.path[self.nodeNum][2]
        
        dest = self.path[self.nodeNum]
        xDest = dest[0][0]
        yDest = dest[0][1]  
            
        self.nodeNum += 1
        self.rect.centerx = xDest # this stuff works bc I'm capturing the players position every frame
        self.rect.centery = yDest
        
        self.hitbox.center = self.rect.center
            
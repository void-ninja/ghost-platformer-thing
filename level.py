import pygame
from pytmx.util_pygame import load_pygame

from settings import *
from tile import Tile
from flag import Flag
from player import Player
from ghost import Ghost
from debug import debug

class Level:
    
    def __init__(self):
        self.displaySurface = pygame.display.get_surface()
        
        self.visibleSprites = CameraGroup() #only group that gets drawn
        self.activeSprites = pygame.sprite.Group() #only group that gets updated
        self.collisionSprites = pygame.sprite.Group() #sprites the player can collide with
        
        self.currentLevel = 1

    def return_next_level(self):
        self.currentLevel += 1
        return self.currentLevel
    
    def level_clear(self):
        self.visibleSprites.empty()
        self.activeSprites.empty()
        self.collisionSprites.empty()
        
    def level_reset_and_load_next(self,levelNum):
        self.level_clear()
        self.level_setup(levelNum)
    
    def level_reset_and_load_first(self):
        self.level_clear()
        self.currentLevel = 1
        
        self.level_setup(self.currentLevel)
    
    # def levelSetup(self, levelNum):
    #     levelMap = LEVEL_MAPS[levelNum-1]
        
    #     for rowIndex,row in enumerate(levelMap):
    #         for colIndex,col in enumerate(row):
    #             x = colIndex * TILE_SIZE
    #             y = rowIndex * TILE_SIZE
    #             if col == "X":
    #                 Tile((x,y),[self.visibleSprites,self.collisionSprites])
    #             if col == "P":
    #                 self.player = Player((x,y),[self.visibleSprites,self.activeSprites],self.collisionSprites,self.visibleSprites,levelMap)
    #             if col == "F":
    #                 Flag((x,y),[self.visibleSprites])
    
    def level_setup(self,levelNum):
        levelMap = LEVEL_MAPS[levelNum-1]
        
        for layer in levelMap.visible_layers:
            if hasattr(layer,"data"):
                for x,y,image in layer.tiles():
                    pos = (x*TILE_SIZE,y*TILE_SIZE)
                    Tile(pos=pos, image=image, groups=[self.visibleSprites,self.collisionSprites])
                    
        for obj in levelMap.objects:
            pos = (obj.x*4,obj.y*4) # x4 needed bc of scaling the tiles from 16 px to 64px
            if obj.name == "Player":
                self.player= Player(pos,[self.visibleSprites,self.activeSprites],self.collisionSprites,self.visibleSprites)
                Ghost(pos,[self.visibleSprites,self.activeSprites])
            elif obj.name == "Flag":
                Flag(pos,obj.image,[self.visibleSprites])
             
    def run(self):
        self.activeSprites.update()
        self.visibleSprites.custom_draw(self.player)
        
class CameraGroup(pygame.sprite.Group):
        def __init__(self):
            super().__init__()
            self.displaySurface = pygame.display.get_surface()
            self.offset = pygame.math.Vector2()
            
            camLeft = CAMERA_BORDERS["left"]
            camTop = CAMERA_BORDERS["top"]
            camWidth = self.displaySurface.get_size()[0] - (CAMERA_BORDERS["right"] + CAMERA_BORDERS["left"])
            camHeight = self.displaySurface.get_size()[1] - (CAMERA_BORDERS["bottom"] + CAMERA_BORDERS["top"])
            
            self.cameraRect = pygame.Rect(camLeft,camTop,camWidth,camHeight)
                        
        def custom_draw(self,player): #camera stuff
            
            if player.rect.left < self.cameraRect.left:
                self.cameraRect.left = player.rect.left
            if player.rect.right > self.cameraRect.right:
                self.cameraRect.right = player.rect.right
            if player.rect.top < self.cameraRect.top:
                self.cameraRect.top = player.rect.top
            if player.rect.bottom > self.cameraRect.bottom:
                self.cameraRect.bottom = player.rect.bottom
            
            #camera offset
            self.offset = pygame.math.Vector2(self.cameraRect.left - CAMERA_BORDERS["left"],self.cameraRect.top - CAMERA_BORDERS['top'])
            
            for sprite in self.sprites():
                offsetPos = sprite.rect.topleft - self.offset
                self.displaySurface.blit(sprite.image,offsetPos)
import pygame

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
        self.player.save_current_moves()
        self.level_setup(levelNum,False)
    
    def level_reset_and_load_first(self):
        self.level_clear()
        self.currentLevel = 1
        
        self.level_setup(self.currentLevel,True)
    
    def level_setup(self,levelNum,first):
        levelMap = LEVEL_MAPS[levelNum-1]
        
        for layer in levelMap.visible_layers:
            if hasattr(layer,"data"):
                for x,y,image in layer.tiles():
                    pos = (x*TILE_SIZE,y*TILE_SIZE)
                    Tile(pos=pos, image=image, groups=[self.visibleSprites,self.collisionSprites])
                    
        for obj in levelMap.objects:
            pos = (obj.x*4,obj.y*4) # x4 needed bc of scaling the tiles from 16 px to 64px
            if obj.name == "Player":
                if first:    
                    self.player = Player(pos,[self.visibleSprites,self.activeSprites],self.collisionSprites,self.visibleSprites)
                else:
                    self.player.hitbox.topleft = pos
                    self.visibleSprites.add(self.player)
                    self.activeSprites.add(self.player)
                    self.ghost = Ghost((pos[0] - 400,pos[1]),[self.visibleSprites,self.activeSprites],self.player.prevMoves)
            elif obj.name == "Flag":
                Flag(pos,obj.image,[self.visibleSprites])
                
        self.visibleSprites.reset_camera(self.player)
        
    def player_save_pos(self):
        self.player.save_pos()
        
    def check_player_collisions(self):
        #checks for level end (hit the flag) and hitting the ghost
        for sprite in self.visibleSprites.sprites():
            if sprite.__class__.__name__ == "Flag" and sprite.rect.colliderect(self.player.hitbox):
                pygame.event.post(pygame.event.Event(FLAG_HIT))
            if sprite.__class__.__name__ == "Ghost" and sprite.hitbox.colliderect(self.player.hitbox) and self.ghost.killsPlayer == True:
                pygame.event.post(pygame.event.Event(GAME_OVER))
             
    def run(self):
        self.check_player_collisions()
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
                
        def reset_camera(self,player):
            self.cameraRect.center = (player.rect.centerx + 100, player.rect.centery - 200)
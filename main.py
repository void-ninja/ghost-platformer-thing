import pygame,sys
from settings import *
from level import Level
#test
class StateController:
    def __init__(self):
        self.game_state = "title"
            
    def title(self): #? maybe change this to only build the level once the level is started
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.game_state = "level"
        
    
        SCREEN.fill(BG_COLOR)
    
        SCREEN.blit(TITLE_IMAGE,(SCREEN_WIDTH/2-100,SCREEN_HEIGHT/2-100))    #centers the title by positioning the upper left corner at half the width of the SCREEN minus half the width of the image
        pygame.display.update()
    
    def game_over(self):        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.go_to_title_screen()    
    
        SCREEN.fill(BG_COLOR)
    
        SCREEN.blit(GAME_OVER_IMAGE,(SCREEN_WIDTH/2-100,SCREEN_HEIGHT/2-100))    #centers the title by positioning the upper left corner at half the width of the SCREEN minus half the width of the image
        pygame.display.update()
        
    def game_won(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.go_to_title_screen() 
    
        SCREEN.fill(BG_COLOR)
    
        SCREEN.blit(GAME_WON_IMAGE,(SCREEN_WIDTH/2-100,SCREEN_HEIGHT/2-100))    #centers the title by positioning the upper left corner at half the width of the SCREEN minus half the width of the image
        pygame.display.update()
    
    def level(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == FLAG_HIT:
                pygame.time.wait(500)
                self.go_to_next_level()
            if event.type == FELL_DOWN:
                self.go_to_game_over()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE: #TODO this should pause
                    self.go_to_title_screen() 
                
    
        SCREEN.fill(BG_COLOR)
        level.run()  #updates and draws stuff
        pygame.display.update()
        
    def state_manager(self):
        if self.game_state == "title":
            self.title()
        if self.game_state == "level":
            self.level()
        if self.game_state == "gameover":
            self.game_over()
        if self.game_state == "gamewon":
            self.game_won()
        
    def go_to_game_over(self):
        level.level_clear()
        self.game_state = "gameover"
    
    def go_to_game_won(self):
        level.level_clear()
        self.game_state = "gamewon"
    
    def go_to_title_screen(self):
        level.level_reset_and_load_first()#this sets the currently active level to the first one
        self.game_state = "title"
    
    def go_to_next_level(self):
        nextLevel = level.return_next_level()
        if nextLevel > MAX_LEVEL_NUM: self.go_to_game_won() #checks to make sure that you arent trying to go to a level that dosent exist
        else: level.level_reset_and_load_next(nextLevel)

pygame.init()
clock = pygame.time.Clock()
level = Level()
gameState = StateController()

while True:
    gameState.state_manager()
    clock.tick(FPS)
    
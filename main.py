import pygame,sys
import pygame_widgets

from settings import *
from level import Level
from screen_handler import ScreenHandler

from debug import debug

#? widgets arent clearing  maybe
#^ level select buttons dont clear
#! fix the screen images not showing e.g. on gameover screen

#player camera wont reset from being pushed down after falling through a level

#TODO----------------
#

class StateController:
    def __init__(self):
        pass
    
    def screen_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == CHANGE_STATE:
                self.change_state(event.__dict__["state"])

        pygame_widgets.update(pygame.event.get())
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
                
    
        SCREEN.blit(BG,(0,0))
        level.run()  #updates and draws stuff
        debug(round(clock.get_fps()))
        pygame.display.update()
        
    def state_manager(self):
        if self.game_state == "level":
            self.level()
        else:
            self.screen_loop()
            
    def change_state(self, state):
        
        
        if state == "startgame":
            self.start_game()
        if state == "title":
            self.go_to_title_screen()
        if state == "gameover":
            self.go_to_game_over()
        if state == "gamewon":
            self.go_to_game_won()
        if state == "levelselect":
            self.go_to_level_select()
        
    def go_to_game_over(self):
        level.level_clear()
        screenHandler.setup_screen("gameover")
        self.game_state = "gameover"
    
    def go_to_game_won(self):
        level.level_clear()
        screenHandler.setup_screen("gamewon")
        self.game_state = "gamewon"
    
    def go_to_title_screen(self):
        level.level_clear()
        screenHandler.setup_screen("title")
        self.game_state = "title"
        
    def go_to_level_select(self):
        level.level_clear()
        screenHandler.setup_screen("levelselect")
        self.game_state = "levelselect"
    
    def go_to_next_level(self):
        nextLevel = level.return_next_level()
        if nextLevel > MAX_LEVEL_NUM: self.go_to_game_won() #checks to make sure that you arent trying to go to a level that dosent exist
        else: level.level_reset_and_load_next(nextLevel)
    
    def start_game(self):
        level.level_reset_and_load_first()#this sets the currently active level to the first one
        self.game_state = "level"

pygame.init()
clock = pygame.time.Clock()
level = Level()
gameState = StateController()
screenHandler = ScreenHandler()

gameState.go_to_title_screen()

while True:
    gameState.state_manager()
    clock.tick(FPS)
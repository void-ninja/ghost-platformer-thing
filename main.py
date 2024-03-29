import pygame,sys
import pygame_widgets

from settings import *
from level import Level
from screen_handler import ScreenHandler

from debug import debug 

#TODO----------------
# add tutorial

class StateController:
    def __init__(self):
        self.tutorial_page = 1
    
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
                return
            if event.type == GAME_OVER:
                self.go_to_game_over()
                return
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE: #TODO this should pause ?
                    self.go_to_title_screen() 
                    return
            if event.type == SAVE_POS:
                if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_SPACE]:
                    level.player_save_pos()
    
        SCREEN.blit(BG,(0,0))
        level.run()  #updates and draws stuff
        pygame.display.update()
    
    def tutorial(self):
        
        if self.tutorial_page > 2:
            self.change_state("title")
            self.tutorial_page = 1
        elif self.tutorial_page == 1:
            SCREEN.blit(TUTORIAL_IMAGE_1,(0,0))
            pygame.display.update()
        elif self.tutorial_page == 2:
            SCREEN.blit(TUTORIAL_IMAGE_2,(0,0))
            pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.tutorial_page += 1
        
    def state_manager(self):
        if self.game_state == "level":
            self.level()
        elif self.game_state == "tutorial":
            self.tutorial()
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
        if state == "tutorial":
            self.game_state = "tutorial"
        
    def go_to_game_over(self):
        level.level_clear()
        pygame.time.set_timer(SAVE_POS, 0)
        screenHandler.setup_screen("gameover")
        self.game_state = "gameover"
    
    def go_to_game_won(self):
        level.level_clear()
        pygame.time.set_timer(SAVE_POS, 0)
        screenHandler.setup_screen("gamewon")
        self.game_state = "gamewon"
    
    def go_to_title_screen(self):
        level.level_clear()
        pygame.time.set_timer(SAVE_POS, 0)
        screenHandler.setup_screen("title")
        self.game_state = "title"
    
    def go_to_next_level(self):
        nextLevel = level.return_next_level()
        if nextLevel > MAX_LEVEL_NUM: self.go_to_game_won() # checks to make sure that you arent trying to go to a level that dosent exist
        else: level.level_reset_and_load_next(nextLevel)
    
    def start_game(self):
        level.level_reset_and_load_first() # this sets the currently active level to the first one
        pygame.time.set_timer(SAVE_POS, 16) # save position in ms (16 = once every frame at 60fps)
        self.game_state = "level"

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    level = Level()
    
    pygame.mixer.music.load(MUSIC_START)
    pygame.mixer.music.play()
    
    gameState = StateController()
    screenHandler = ScreenHandler()

    gameState.game_state = "tutorial"

    while True:
        if pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.load(MUSIC_LOOP)
            pygame.mixer.music.play()
        
        gameState.state_manager()
        clock.tick(FPS)

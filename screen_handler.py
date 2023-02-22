import pygame
from pygame_widgets.button import Button
from pygame_widgets.button import ButtonArray

from settings import *

class ScreenHandler: #this handles displaying every screen other than the level
    def __init__(self):
        pass
    #screen setups
    def setup_screen(self, screen): # screen needs to be a text input, "title","gameover","gamewon","levelselect" are all valid options
        if screen == "title":
            SCREEN.fill(BG_COLOR)
            SCREEN.blit(TITLE_IMAGE,(SCREEN_WIDTH/2-100,SCREEN_HEIGHT/2-100))
            
            self.startButton = Button(
                win=SCREEN,
                x=SCREEN_WIDTH/2-100,
                y=SCREEN_HEIGHT/2+100,
                width=200,
                height=100,
                margin=0, 
                radius=20,
                image=TITLE_SCREEN_START_BUTTON_IMAGE,
                onClick=lambda: pygame.event.post(pygame.event.Event(CHANGE_STATE,state="startgame"))
            )
            
        elif screen == "gameover":
            SCREEN.fill(BG_COLOR)
            SCREEN.blit(GAME_OVER_IMAGE,(SCREEN_WIDTH/2-100,SCREEN_HEIGHT/2-100))    
           
            self.titleScreenButton = Button(
                win=SCREEN,
                x=SCREEN_WIDTH/2-100,
                y=SCREEN_HEIGHT/2+100,
                width=200,
                height=100,
                margin=0,
                radius=20,
                image=GO_TO_TITLE_BUTTON_IMAGE,
                onClick=lambda: pygame.event.post(pygame.event.Event(CHANGE_STATE,state="title"))
            )
            
        elif screen == "gamewon":
            SCREEN.fill(BG_COLOR)
            SCREEN.blit(GAME_WON_IMAGE,(SCREEN_WIDTH/2-100,SCREEN_HEIGHT/2-100))    
            
            self.titleScreenButton = Button(
                win=SCREEN,
                x=SCREEN_WIDTH/2-100,
                y=SCREEN_HEIGHT/2+100,
                width=200,
                height=100,
                margin=0,
                radius=20,
                image=GO_TO_TITLE_BUTTON_IMAGE,
                onClick=lambda: pygame.event.post(pygame.event.Event(CHANGE_STATE,state="title"))
            )
            
        elif screen == "levelselect":
            SCREEN.fill(BG_COLOR)
            SCREEN.blit(LEVEL_SELECT_IMAGE,(SCREEN_WIDTH/2-100,SCREEN_HEIGHT/2-300))    
            
            self.titleScreenButton = Button(     
                win=SCREEN,
                x=SCREEN_WIDTH/2-100,
                y=SCREEN_HEIGHT/2+100,
                width=200,
                height=100,
                margin=0,
                radius=20,
                image=GO_TO_TITLE_BUTTON_IMAGE,
                onClick=lambda: pygame.event.post(pygame.event.Event(CHANGE_STATE,state="title"))
            )

            self.levelSelectButtons = ButtonArray(
                SCREEN,
                SCREEN_WIDTH/2,
                SCREEN_HEIGHT/2-200,
                400,
                200,
                (3,2),
                colour=BG_COLOR,
                texts=("1","2","3","4","5","6"),
                onClicks=(lambda: print('1'), lambda: print('2'), lambda: print('3'), lambda: print('4'), lambda: print('5'), lambda: print('6'))
            )
            


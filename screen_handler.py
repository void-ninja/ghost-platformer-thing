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
            SCREEN.blit(BG,(0,0))
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
            
            self.tutorialButton = Button(
                win=SCREEN,
                x=SCREEN_WIDTH/2-100,
                y=SCREEN_HEIGHT/2+230,
                width=200,
                height=100,
                margin=0, 
                radius=20,
                image=TUTORIAL_BUTTON_IMAGE,
                onClick=lambda: pygame.event.post(pygame.event.Event(CHANGE_STATE,state="tutorial"))
            )
            
        elif screen == "gameover":
            SCREEN.blit(BG,(0,0))
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
            SCREEN.blit(BG,(0,0))
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
            


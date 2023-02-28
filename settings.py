import pygame
import pygame_widgets
from pygame_widgets.button import Button
from pytmx.util_pygame import load_pygame

pygame.init()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#deprecated -------------------------
# LEVEL_MAPS = [[
#     "                  X  F  X   ",
#     "                   XXXXX    ",
#     "                      X  X  ",
#     " P                    X     ",
#     "XXXX                   X    ",
#     "XXX       F            XX   ",
#     "        XXXXXXXXXXXX        ",
#     "       XX          XX      X",
#     "   X XXXX            X     X",
#     "  XX    X             XXXXXX",
#     " XXX    X                   ",
#     "XXXX XXXX                   ",
# ],[
#     "             XXXXXX  F                   XXXXXX  F      ",
#     "                   XXXX                        XXXX     ",
#     "                      X  X                        X  X  ",
#     " P                    X                           X     ",
#     "                       X                           X    ",
#     "          F            XX                          XX   ",
#     "XXXX  XXXXXXXXXXXXXX        XXXXXXXXXXXXXXXXXXXX        ",
#     "       XX          XX      X                   XX      X",
#     "   X  XXX            X     X                     X     X",
#     "  XX    X             X  XXX                      XXXXXX",
#     " XXX    X                                               ",
#     "                                                        ",
# ]]
#---------------------------------------
LEVEL_MAPS = [load_pygame("art/tmx/level1.tmx")] #new levels go in here

MAX_LEVEL_NUM = len(LEVEL_MAPS)

TILE_SIZE = 64 #16x12 tile screen

BG = pygame.transform.scale(pygame.image.load("art/bg1.png").convert_alpha(),(SCREEN_WIDTH,SCREEN_HEIGHT))

PLAYER_COLOR = "green"
TILE_COLOR = "blue"
FLAG_COLOR = "yellow"

FLAG_HIT = pygame.event.custom_type()
FELL_DOWN = pygame.event.custom_type()
CHANGE_STATE = pygame.event.custom_type()

TITLE_IMAGE = pygame.transform.scale2x(pygame.image.load("art/title_placeholder.png").convert_alpha())
GAME_OVER_IMAGE = pygame.transform.scale2x(pygame.image.load("art/game_over_placeholder.png").convert_alpha())
GAME_WON_IMAGE = pygame.transform.scale2x(pygame.image.load("art/game_won_placeholder.png").convert_alpha())
LEVEL_SELECT_IMAGE = pygame.transform.scale2x(pygame.image.load("art/level_select_placeholder.png").convert_alpha())

TITLE_SCREEN_START_BUTTON_IMAGE = pygame.transform.scale2x(pygame.image.load("art/start_button_placeholder.png").convert_alpha())
GO_TO_TITLE_BUTTON_IMAGE = pygame.transform.scale2x(pygame.image.load("art/main_menu_button_placeholder.png").convert_alpha())

FPS = 60

CAMERA_BORDERS = {
    "left": 200,
    "right": 400,
    "top": 100,
    "bottom": 150}
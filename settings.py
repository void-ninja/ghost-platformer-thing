import pygame

pygame.init()

LEVEL_MAPS = [[
    "                  X  F  X   ",
    "                   XXXXX    ",
    "                      X  X  ",
    " P                    X     ",
    "XXXX                   X    ",
    "XXX       F            XX   ",
    "        XXXXXXXXXXXX        ",
    "       XX          XX      X",
    "   X XXXX            X     X",
    "  XX    X             XXXXXX",
    " XXX    X                   ",
    "XXXX XXXX                   ",
],[
    "             XXXXXX  F                   XXXXXX  F      ",
    "                   XXXX                        XXXX     ",
    "                      X  X                        X  X  ",
    " P                    X                           X     ",
    "                       X                           X    ",
    "          F            XX                          XX   ",
    "XXXX  XXXXXXXXXXXXXX        XXXXXXXXXXXXXXXXXXXX        ",
    "       XX          XX      X                   XX      X",
    "   X  XXX            X     X                     X     X",
    "  XX    X             X  XXX                      XXXXXX",
    " XXX    X                                               ",
    "                                                        ",
]]

MAX_LEVEL_NUM = len(LEVEL_MAPS)

TILE_SIZE = 64 #16x12 tile screen
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

BG_COLOR = "slategrey"
PLAYER_COLOR = "green"
TILE_COLOR = "blue"
FLAG_COLOR = "yellow"

FLAG_HIT = pygame.event.custom_type()
FELL_DOWN = pygame.event.custom_type()

TITLE_IMAGE = pygame.transform.scale2x(pygame.image.load("art/title_placeholder.png").convert_alpha())
GAME_OVER_IMAGE = pygame.transform.scale2x(pygame.image.load("art/game_over_placeholder.png").convert_alpha())
GAME_WON_IMAGE = pygame.transform.scale2x(pygame.image.load("art/game_won_placeholder.png").convert_alpha())

FPS = 60

CAMERA_BORDERS = {
    "left": 200,
    "right": 400,
    "top": 100,
    "bottom": 150}
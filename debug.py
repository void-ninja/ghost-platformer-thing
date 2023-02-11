import pygame

pygame.init()
font = pygame.font.Font(None, 30)

def debug (info, y=10, x=10):
    displaySurf = pygame.display.get_surface()
    debugSurf = font.render(str(info), True, "white")
    debugRect = debugSurf.get_rect(topleft = (x,y))
    pygame.draw.rect(displaySurf, "Black", debugRect)
    displaySurf.blit(debugSurf, debugRect)
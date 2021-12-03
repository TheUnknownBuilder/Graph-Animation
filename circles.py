import pygame
from graph_data import graph

# constants 
display_width = 800
display_height = 600
radius = 30 # node size

def run():
    pygame.init()

    screen = pygame.display.set_mode((display_width, display_height))

    screen.fill((0,0,0)) # param is color tuple

    # loop to draw cicle at each node center
    for centerxy, _ in graph:
        pygame.draw.circle(screen, # draw need buffer
        (255,255,200), # color of circle
        centerxy, radius) # default is filled circle

    pygame.display.update() # copy screen to display
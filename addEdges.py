# now collect edges into dict, and draw them
import pygame
from graph_data import graph

display_width = 800
display_height = 600
radius = 30

white = (255,255,255)
blue = (50,50,160)

def run():
  global screen, edges

  build_edges()
  pygame.init()

  screen = pygame.display.set_mode((display_width, display_height))
  clock = pygame.time.Clock()

  screen.fill((0,0,0,))

  for n1,n2 in edges:
    pygame.draw.line(screen, white, graph[n1][0], graph[n2][0],2)

  for xy, _ in graph: 
    circle_fill(xy, white, blue, 25, 2)

  pygame.display.update()

  while 1: 
    clock.tick(60)

def circle_fill(xy, line_color, fill_color, radius, thickness):
  global screen
  
  pygame.draw.circle(screen, line_color, xy, radius)
  pygame.draw.circle(screen, fill_color, xy, radius - thickness)
  
def edge_id(n1,n2):
  return tuple(sorted((n1,n2))) 

def build_edges():
  global edges
  edges = {}
  for n1, (_, adjacents) in enumerate(graph):
    for n2 in adjacents:
      eid = edge_id(n1,n2)
      if eid not in edges:
        edges[eid] = (n1,n2)
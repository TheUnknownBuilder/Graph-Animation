import pygame
pygame.init()
back = (192,192,192)
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('A bit Racey')
gameDisplay.fill(back)
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    clock.tick(60)   
pygame.quit()
quit()
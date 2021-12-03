import pygame as pg

display_width=880
display_height=500
# display = (1680, 1050)
radius1=75
radius2=100

def main():
    pg.init()
    
    screen=pg.display.set_mode((display_width,display_height))
    screen.fill((0,0,0))
    pg.draw.circle(screen,(6,57,112),(150,200), radius2)
    pg.draw.circle(screen,(171,219,227),(150,300), radius1 ) #right
    pg.draw.circle(screen,(171,219,227),(250,200), radius1 ) #top
    pg.draw.circle(screen,(171,219,227),(50,200), radius1 ) #left
    clock = pg.time.Clock()
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        pg.display.update()
        clock.tick(60)   
    pg.quit()
    quit()
    

if __name__ == "__main__":
    main()
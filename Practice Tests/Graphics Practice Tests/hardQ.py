from pygame import *
from random import *

screen = display.set_mode((800, 600))


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0,0,0)
CYAN = (0,125,125)
col = (randint(0,255)), (randint(0,255)), (randint(0,255))

screen.fill(GREEN)

running = True
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False

    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    
    screen.fill(GREEN)
    for i in range(10,800,20):
        for j in range(10,600,20):
            distance = (((mx-i)**2)+((my-j)**2))**(1/2)
            draw.circle(screen, (128,128,128), (i,j), distance/50)
    




    
    display.flip()

quit()
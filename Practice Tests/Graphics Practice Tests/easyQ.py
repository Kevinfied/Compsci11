from pygame import *
from random import *

screen = display.set_mode((800, 600))

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0,0,0)
CYAN = (0,125,125)
col = (randint(0,255)), (randint(0,255)), (randint(0,255))


running = True
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False

    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    
    if mb[0]:
        draw.circle(screen, RED, (mx, my), 50, 1)
        draw.line(screen, RED, (mx-50, my), (mx+50, my))
        draw.line(screen, RED, (mx, my+50), (mx, my-50))
        draw.circle(screen, BLACK, (mx, my), 10)




    
    display.flip()

quit()
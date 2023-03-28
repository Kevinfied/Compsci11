from pygame import *
from random import *

screen = display.set_mode((800, 600))

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0,0,0)
CYAN = (0,125,125)
WHITE = (255,255,255)
col = (randint(0,255)), (randint(0,255)), (randint(0,255))


def pattern():
    screen.fill((255, 255, 255))
    for x in range(40):
        draw.rect(screen, cols[x], (x * 20, 300, 21, 21))
        draw.rect(screen, (0, 0, 0), (x * 20, 300, 21, 21), 1)
    else:
        draw.circle(screen, col, (mx, my), 10)
cols = [(255, 255, 255)] * 40

running = True
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False

    mb = mouse.get_pressed()
    mx, my = mouse.get_pos()
    if mb[0] == 1:
         col = (255, 0, 0)
    else:
        if mb[2] == 1:
            col = (0, 255, 0)
        else:
            col = (255, 255, 255)
    cols = [cols[-1]] + cols
    del cols[-1]
    if 300 <= my <= 320:
        pos = mx // 20
        cols[pos] = col
    if mb[0] == 0:
        dark = 255
        pattern()
    
    # screen.fill(WHITE)
    # draw.circle(screen, WHITE, (mx,my), 10)

    # for i in range(1,800,20):
    #     draw.rect(screen, BLACK, (i-1,290,20,20),1)

    # if mb[0]:
    #     draw.circle(screen, RED, (mx, my), 10, )
        

    # if mb[2]:
    #     draw.circle(screen, GREEN, (mx, my), 10)


    
    display.flip()
    time.wait(50)

quit()

from pygame import *

screen = display.set_mode((800,600))



cols = [(255, 255, 255)] * 40


def pattern():
    screen.fill((255, 255, 255))
    for x in range(40):
        draw.rect(screen, cols[x], (x * 20, 300, 21, 21))
        draw.rect(screen, (0, 0, 0), (x * 20, 300, 21, 21), 1)
    else:
        draw.circle(screen, col, (mx, my), 10)

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

    if my < 310 and my > 290:
        e = mx//20
        cols[e] = col
    time.wait(50)
    pattern()

    display.flip()


quit()

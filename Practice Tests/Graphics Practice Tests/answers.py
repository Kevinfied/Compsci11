# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: E:\New folder\gr09_hard_c.py
# Compiled at: 2012-11-28 15:30:16
# Size of source mod 2**32: 1252 bytes
from pygame import *
from random import *

# def done():
#     for evt in event.get():
#         if evt.type == QUIT:
#             return True
#         return False
running = True

def pattern():
    screen.fill((255, 255, 255))
    for x in range(40):
        draw.rect(screen, cols[x], (x * 20, 300, 21, 21))
        draw.rect(screen, (0, 0, 0), (x * 20, 300, 21, 21), 1)
    else:
        draw.circle(screen, col, (mx, my), 10)


cols = [(255, 255, 255)] * 40

screen = display.set_mode((800, 600))
screen.fill((0, 0, 0))
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
    display.flip()
    time.wait(50)

quit()
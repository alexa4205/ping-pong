from pygame import *

back = (200, 255, 255)
width = 600
height = 500
win = display.set_mode((width, height))
win.fill(back)

FPS = 60
game = True
clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()
    clock.tick(FPS)
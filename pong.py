import pygame as py

from paddle import Paddle

py.init()

# variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
clock = py.time.Clock()
FPS = 60

# colors
black = (0, 0, 0)
white = (255, 255, 255)


screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
py.display.set_caption("Pong OOP")

running = True
player_paddle = Paddle(10, 10, 20, 100, (0, 255, 0))

while running:
    clock.tick(FPS)
    screen.fill(black)

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    keys = py.key.get_pressed()
    player_paddle.move(keys, SCREEN_HEIGHT)

    player_paddle.draw(screen)
    py.display.flip()


py.quit()

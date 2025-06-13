import pygame as py

from game_classes.paddle import Paddle
from game_classes.ball import Ball

py.init()

# variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
clock = py.time.Clock()
FPS = 60

# colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
py.display.set_caption("Pong OOP")

running = True
player_paddle = Paddle(30, 10, 20, 100, green)
ball = Ball(50, 50, 20, 20, red, 5)

while running:
    clock.tick(FPS)
    screen.fill(black)

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                running = False

    keys = py.key.get_pressed()

    # player
    player_paddle.move(keys, SCREEN_HEIGHT)
    player_paddle.draw(screen)

    # ball
    ball.draw(screen)
    ball.move(SCREEN_WIDTH, SCREEN_HEIGHT)

    # collisions
    player_paddle_rect = py.Rect(
        player_paddle.x, player_paddle.y, player_paddle.width, player_paddle.height
    )
    ball_rect = py.Rect(ball.x, ball.y, ball.width, ball.height)

    if ball_rect.colliderect(player_paddle_rect):
        ball.speed_x *= -1

    py.display.flip()


py.quit()

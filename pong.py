import pygame as py

from game_classes.paddle import Paddle
from game_classes.ball import Ball

py.init()

# variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
clock = py.time.Clock()
FPS = 60


# screen center

# colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

# fonts
game_font = "Roboto"
small_font = 20
medium_font = 32
big_font = 44

# scores
score = {"player_green": 0, "player_blue": 0}

screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
py.display.set_caption("Pong OOP")

player_paddle = Paddle(50, 10, 20, 100, green, 1)
player_2_paddle = Paddle(SCREEN_WIDTH - 80, 10, 20, 100, blue, 2)
ball = Ball(50, 50, 20, 20, red, 5)

ball.reset(SCREEN_WIDTH, SCREEN_HEIGHT)


def draw_text(font_size, color, message, center=True, position=(0, 0)):
    font = py.font.SysFont(game_font, font_size)
    text = font.render(message, True, color)

    if center:
        centered_pos = (
            SCREEN_WIDTH // 2 - text.get_width() // 2,
            SCREEN_HEIGHT // 2 - text.get_height() // 2,
        )
        screen.blit(
            text,
            centered_pos,
        )
    else:
        screen.blit(text, position)


game_state = "start"
running = True
while running:
    clock.tick(FPS)
    screen.fill(black)

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN:
            game_state = "running"
            if event.key == py.K_ESCAPE:
                running = False

    if game_state == "start":
        draw_text(
            big_font,
            white,
            "Wciśnij ENTER, aby zacząć",
        )

    if game_state == "running":
        draw_text(
            big_font,
            white,
            f"{score['player_green']} | {score['player_blue']}",
            False,
            (SCREEN_WIDTH // 2 - 70, 10),
        )

        keys = py.key.get_pressed()

        # player
        player_paddle.move_keyboard(keys, SCREEN_HEIGHT)
        player_paddle.draw(screen)

        # player2
        player_2_paddle.move_keyboard(keys, SCREEN_HEIGHT)
        player_2_paddle.draw(screen)

        # ball
        ball.draw(screen)
        ball.move(SCREEN_WIDTH, SCREEN_HEIGHT)

        # collisionsw
        player_paddle_rect = py.Rect(
            player_paddle.x, player_paddle.y, player_paddle.width, player_paddle.height
        )
        player_2_paddle_rect = py.Rect(
            player_2_paddle.x,
            player_2_paddle.y,
            player_2_paddle.width,
            player_2_paddle.height,
        )
        ball_rect = py.Rect(ball.x, ball.y, ball.width, ball.height)

        if ball_rect.colliderect(player_paddle_rect) or ball_rect.colliderect(
            player_2_paddle_rect
        ):
            ball.vel_x *= -1

        # get_points
        if ball.x < -50:
            score["player_blue"] += 1
            ball.reset(SCREEN_WIDTH, SCREEN_HEIGHT)
        elif ball.x > SCREEN_WIDTH + 50:
            score["player_green"] += 1
            ball.reset(SCREEN_WIDTH, SCREEN_HEIGHT)

    py.display.flip()


py.quit()

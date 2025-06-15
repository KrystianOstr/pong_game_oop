import pygame as py
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, MAX_POINTS, COLORS, FONT

from game_classes.game_ui import GameUi
from game_classes.paddle import Paddle
from game_classes.ball import Ball
from game_classes.scoreboard import Scoreboard

py.init()
py.mixer.init()


clock = py.time.Clock()

# variables

point_time = 0
last_scorer = None

# ALIASES

# font alias
font_name = FONT["name"]

# color alias
green = COLORS["green"]
blue = COLORS["blue"]
red = COLORS["red"]
white = COLORS["white"]
black = COLORS["black"]


# scores

screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
py.display.set_caption("Pong OOP")

player_paddle_height = 100
player2_paddle_height = 150

player_paddle = Paddle(
    50,
    SCREEN_HEIGHT // 2 - player_paddle_height // 2,
    20,
    player_paddle_height,
    green,
    1,
)
player_2_paddle = Paddle(
    SCREEN_WIDTH - 80,
    SCREEN_HEIGHT // 2 - player2_paddle_height // 2,
    20,
    player2_paddle_height,
    blue,
    2,
)
ball = Ball(50, 50, 20, 20, red, 5)

ball.reset(SCREEN_WIDTH, SCREEN_HEIGHT)


game_ui = GameUi(40, screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT)
scoreboard = Scoreboard(0, 0, white)

game_state = "start"
running = True
while running:
    clock.tick(FPS)
    screen.fill(black)

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN:
            if game_state == "start":
                game_state = "running"
            if event.key == py.K_ESCAPE:
                running = False
            if game_state == "game_over" and event.key == py.K_RETURN:
                point_time = 0
                last_scorer = None
                scoreboard.scoreboard_reset()
                ball.reset(SCREEN_WIDTH, SCREEN_HEIGHT)
                game_state = "running"

    if game_state == "start":
        game_ui.draw_start_screen(screen)

    if game_state == "running":

        keys = py.key.get_pressed()

        scoreboard.draw(screen, SCREEN_WIDTH)

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
            # player2
            scoreboard.add_point(2)
            if scoreboard.player2_score >= MAX_POINTS:
                game_state = "game_over"
                winner = 2
            else:
                point_time = py.time.get_ticks()
                game_state = "point_scored"
                last_scorer = 2
        elif ball.x > SCREEN_WIDTH + 50:
            # player1
            scoreboard.add_point(1)
            if scoreboard.player1_score >= MAX_POINTS:
                game_state = "game_over"
                winner = 1
            else:
                point_time = py.time.get_ticks()
                game_state = "point_scored"
                last_scorer = 1

    if game_state == "point_scored":
        game_ui.draw_point_screen(
            screen, last_scorer, green if last_scorer == 1 else blue
        )
        if py.time.get_ticks() - point_time > 1000:
            ball.reset(SCREEN_WIDTH, SCREEN_HEIGHT)
            game_state = "running"

    if game_state == "game_over":
        game_ui.draw_game_over(screen, winner, green if winner == 1 else blue)
        game_ui.draw_text(
            screen,
            f"{scoreboard.player1_score} : {scoreboard.player2_score}",
            (0, 330),
            center_y=False,
        )
        game_ui.draw_text(screen, "Press ENTER to restart", (0, 500), center_y=False)

    py.display.flip()


py.quit()

import pygame as py


class Scoreboard:
    def __init__(self, player1_score, player2_score, color):
        self.player1_score = player1_score
        self.player2_score = player2_score
        self.color = color
        self.font = py.font.SysFont("Roboto", 48)

    def draw(self, surface, screen_width):
        player1_text = self.font.render(f"{self.player1_score}", True, self.color)
        surface.blit(player1_text, (50, 20))

        player2_text = self.font.render(f"{self.player2_score}", True, self.color)
        surface.blit(player2_text, (screen_width - 100, 20))

    def add_point(self, player_number):
        if player_number == 1:
            self.player1_score += 1
        elif player_number == 2:
            self.player2_score += 1

    def scoreboard_reset(self):
        self.player1_score = 0
        self.player2_score = 0

import pygame as py


class Paddle:
    def __init__(self, x, y, width, height, color, player_number):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = 10
        self.player_number = player_number

    def draw(self, surface):
        py.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def move_keyboard(self, keys, screen_height):
        if self.player_number == 1:
            if keys[py.K_w] and self.y > 0:
                self.y -= self.speed
            if keys[py.K_s] and self.y + self.height < screen_height:
                self.y += self.speed

        if self.player_number == 2:
            if keys[py.K_UP] and self.y > 0:
                self.y -= self.speed
            if keys[py.K_DOWN] and self.y + self.height < screen_height:
                self.y += self.speed

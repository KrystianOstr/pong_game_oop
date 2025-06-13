import pygame as py


class Paddle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = 10

    def draw(self, surface):
        py.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def move(self, keys, screen_height):
        if keys[py.K_w] and self.y > 0:
            self.y -= self.speed
        if keys[py.K_s] and self.y + self.height < screen_height:
            self.y += self.speed

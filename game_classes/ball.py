import pygame as py


class Ball:
    def __init__(self, x, y, width, height, color, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed_x = speed
        self.speed_y = speed

    def draw(self, surface):
        py.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def move(self, screen_width, screen_height):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x <= 0:
            self.speed_x *= -1

        if self.x + self.width >= screen_width:
            self.speed_x *= -1

        if self.y <= 0:
            self.speed_y *= -1

        if self.y + self.height >= screen_height:
            self.speed_y *= -1

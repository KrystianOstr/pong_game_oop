import pygame as py
import random


class Ball:
    def __init__(self, x, y, width, height, color, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vel_x = speed
        self.vel_y = speed
        self.speed = speed

    def draw(self, surface):
        py.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def move(self, screen_width, screen_height):
        self.x += self.vel_x
        self.y += self.vel_y

        # if self.x <= 0:
        #     self.vel_x *= -1

        # if self.x + self.width >= screen_width:
        #     self.vel_x *= -1

        if self.y <= 0:
            self.vel_y *= -1

        if self.y + self.height >= screen_height:
            self.vel_y *= -1

    def reset(self, screen_width, screen_height):
        # py.time.delay(1000)
        self.x = screen_width // 2
        self.y = random.randint(0, screen_height - self.height)
        self.vel_x = random.choice([-1, 1]) * self.speed

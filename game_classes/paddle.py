import pygame as py
import random

from settings import DIFFICULTY_SETTINGS


class Paddle:
    def __init__(self, x, y, width, height, color, player_number, ai_enabled=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = 10
        self.player_number = player_number
        self.ai_enabled = ai_enabled
        self.ai_speed = 0
        self.miss_chance = 0

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

    def move_ai(self, ball_y):
        if random.random() < self.miss_chance:
            return
        if ball_y < self.y + self.height // 2:
            self.y -= self.ai_speed

        if ball_y > self.y + self.height // 2:
            self.y += self.ai_speed

    def set_ai_difficulty(self, level):
        settings = DIFFICULTY_SETTINGS[level]
        self.ai_speed = settings["ai_speed"]
        self.miss_chance = settings["miss_chance"]

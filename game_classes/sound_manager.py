import pygame as py
from settings import resource_path


class SoundManager:
    def __init__(self):
        self.bounce_sound = resource_path("assets/sounds/boing.wav")
        self.point_sound = resource_path("assets/sounds/point.wav")
        self.gameover_sound = resource_path("assets/sounds/game_end.wav")

    def play_bounce(self):
        sound = py.mixer.Sound(self.bounce_sound)
        sound.play()

    def play_point(self):
        sound = py.mixer.Sound(self.point_sound)
        sound.play()

    def play_gameover(self):
        sound = py.mixer.Sound(self.gameover_sound)
        sound.play()

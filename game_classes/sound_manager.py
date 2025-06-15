import pygame as py


class SoundManager:
    def __init__(self):
        self.bounce_sound = "assets/sounds/boing.wav"
        self.point_sound = "assets/sounds/point.wav"
        self.gameover_sound = "assets/sounds/game_end.wav"

    def play_bounce(self):
        sound = py.mixer.Sound(self.bounce_sound)
        sound.play()

    def play_point(self):
        sound = py.mixer.Sound(self.point_sound)
        sound.play()

    def play_gameover(self):
        sound = py.mixer.Sound(self.gameover_sound)
        sound.play()

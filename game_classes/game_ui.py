import pygame as py


class GameUi:
    def __init__(
        self,
        font_size,
        screen_width,
        screen_height,
        font_name="Roboto",
        color=(255, 255, 255),
    ):
        self.font_size = font_size
        self.font_name = font_name
        self.color = color
        self.screen_width = screen_width
        self.screen_height = screen_height

    def _blit_centered(self, surface, text_render):
        x = self.screen_width // 2 - text_render.get_width() // 2
        y = self.screen_height // 2 - text_render.get_height() // 2
        surface.blit(text_render, (x, y))

    def draw_text(self, surface, text, pos=(0, 0), center_x=True, center_y=True):
        text_font = py.font.SysFont(self.font_name, self.font_size)
        text_render = text_font.render(text, True, self.color)

        x, y = pos

        if center_x:
            x = self.screen_width // 2 - text_render.get_width() // 2
        if center_y:
            y = self.screen_height // 2 - text_render.get_height() // 2

        surface.blit(text_render, (x, y))

    def draw_start_screen(
        self,
        surface,
    ):
        text_font = py.font.SysFont(self.font_name, self.font_size)
        text_render = text_font.render("Press ANY key to start", True, self.color)

        self._blit_centered(surface, text_render)

    def draw_point_screen(
        self,
        surface,
        player_number,
        color,
    ):
        text_font = py.font.SysFont(self.font_name, self.font_size)
        text_render = text_font.render(f"Point for player {player_number}", True, color)

        self._blit_centered(surface, text_render)

    def draw_game_over(
        self,
        surface,
        winner,
        color,
    ):
        text_font = py.font.SysFont(self.font_name, self.font_size)
        text_render = text_font.render(f"Player {winner} won!", True, color)

        self._blit_centered(surface, text_render)

from core.Game import Game
from core.Scene import Scene
from ui_objects.Button import Button
from scenes.GameModeMenu import GameModeMenu


class Menu(Scene):
    def __init__(self, game: Game = None):
        super().__init__(game)

    def init_UI(self):
        size = width, height = 200, 100

        position = self.center[0] - width // 2, self.center[1] - height // 2
        self.play_button = Button(position, size, (200, 200, 200), self, "ok, let`s go", font_size=45)

    def connect_buttons(self):
        self.play_button.on_click = self.play_button_on_click

    def play_button_on_click(self):
        game_mode_menu = GameModeMenu(self.game)
        self.game.set_scene_active(game_mode_menu)

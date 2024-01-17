from typing import TYPE_CHECKING

from core.Scene import Scene
from ui_objects.Text import Text, Alignment
from ui_objects.Button import Button
from ui_objects.List import List

if TYPE_CHECKING:
    from core.Game import Game


class WinScene(Scene):
    def __init__(self, game: 'Game', teams: dict):
        self.teams = teams
        self.won_team = max(self.teams, key=lambda a: self.teams[a])

        super(WinScene, self).__init__(game)

    def init_UI(self):
        button_size = button_width, button_height = 200, 100
        position = x, y = self.center[0] - button_width // 2, self.center[1] - button_height // 2

        self.title = Text((0, self.center[1] - button_height // 2), (self.game.width, button_height),
                          self, f'Победила команда: {self.won_team}', font_size=45)

        self.ok_button = Button((x, self.game.height - button_height - 200), button_size, (200, 200, 200), self, 'ГГ!')
        self.ok_button.on_click = self.ok_button_on_click

        self.score = List((0, 200), (self.game.width, 150), (200, 200, 200), self)
        for name, score in self.teams.items():
            label = Text((0, 0), (self.game.width, 65), None, f"{name}: {score}", font_size=75)
            label.alignment = Alignment.LEFT_CENTER
            self.score.add_child(label)

    def ok_button_on_click(self):
        from scenes.GameModeMenu import GameModeMenu

        game_mode_menu = GameModeMenu(self.game)
        self.game.set_scene_active(game_mode_menu)

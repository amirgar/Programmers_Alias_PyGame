from typing import TYPE_CHECKING
from random import randrange

import pygame

from GameMode import GameMode
from Events import WORD_TIMER_EVENT

from core.Scene import Scene
from ui_objects.Button import Button
from ui_objects.Text import Text, Alignment
from ui_objects.List import List
from scenes.WinScene import WinScene

if TYPE_CHECKING:
    from core.Game import Game


class PlayScene(Scene):
    def __init__(self, game_mode: GameMode, teams: dict, game: 'Game' = None):
        self.game_mode = game_mode
        self.teams = teams
        self.time = game_mode.time
        self.not_used_words = game_mode.words

        self.current_team_index = 0
        self.last_word = False

        super().__init__(game)

    @property
    def current_team_index(self):
        return self._current_team_index

    @current_team_index.setter
    def current_team_index(self, value):
        self._current_team_index = value
        if self._current_team_index >= len(self.teams):
            self._current_team_index = 0
        self.current_team = tuple(self.teams.keys())[self._current_team_index]

    def init_UI(self):
        center = center_x, center_y = self._game.width // 2, self._game.height // 2

        button_size = button_width, button_height = 200, 100
        position = x, y = center[0] - button_width // 2, center[1] - button_height // 2

        self.ready_button = Button(position, button_size, (200, 200, 200), self, "Готовы?")

        self.skip_button = Button((20, self.game.height - button_height - 20),
                                  button_size, (200, 200, 200), self, "Скип")
        self.skip_button.is_active = False

        self.ok_button = Button((self.game.width - button_width - 20, self.game.height - button_height - 20),
                                button_size, (200, 200, 200), self, "ЕС!")
        self.ok_button.is_active = False

        self.time_count_label = Text((0, 20), (self.game.width, 75),
                                     self, f"Сейчас команда: {self.current_team}", font_size=65)

        self.score = List((0, 200), (self.game.width, 150), (200, 200, 200), self)
        for name, score in self.teams.items():
            label = Text((0, 0), (self.game.width, 65), None, f"{name}: {score}", font_size=75)
            label.alignment = Alignment.LEFT_CENTER
            self.score.add_child(label)

        self.word_label = Text((0, center_y), (self.game.width, 75), self, "{word}")
        self.word_label.is_active = False

    def refresh_score(self):
        self.score.children.clear()
        for name, score in self.teams.items():
            label = Text((0, 0), (self.game.width, 65), None, f"{name}: {score}", font_size=75)
            label.alignment = Alignment.LEFT_CENTER
            self.score.add_child(label)

    def pick_word(self):
        new_word = tuple(self.not_used_words)[randrange(len(self.not_used_words))]
        self.not_used_words.remove(new_word)
        self.word_label.text = new_word

        if not self.not_used_words:
            self.not_used_words = self.game_mode.words

        if self.last_word:
            if max(self.teams.values()) >= self.game_mode.max_score:
                self.to_win_scene()
            self.reset()

    def connect_buttons(self):
        self.ready_button.on_click = self.ready_button_on_click
        self.skip_button.on_click = self.skip_button_on_click
        self.ok_button.on_click = self.ok_button_on_click

    def ready_button_on_click(self):
        self.ready_button.is_active = False
        self.skip_button.is_active = True
        self.ok_button.is_active = True
        self.time_count_label.is_active = True
        self.word_label.is_active = True
        self.time_count_label.text = f"Осталось секунд: {str(self.time)}"

        self.pick_word()
        pygame.time.set_timer(WORD_TIMER_EVENT, 1000)

    def skip_button_on_click(self):
        self.pick_word()

    def ok_button_on_click(self):
        self.teams[self.current_team] += 1
        self.refresh_score()
        self.pick_word()

    def handle_event(self, event: pygame.event.Event):
        super(PlayScene, self).handle_event(event)

        if event.type == WORD_TIMER_EVENT:
            self.time -= 1
            self.time_count_label.text = f"Осталось секунд: {str(self.time)}"
            if self.time == 0:
                pygame.time.set_timer(WORD_TIMER_EVENT, 0)
                self.last_word = True

    def reset(self):
        self.current_team_index += 1
        self.last_word = False
        self.time = self.game_mode.time
        pygame.time.set_timer(WORD_TIMER_EVENT, 0)

        self.clear()
        self.init_UI()
        self.connect_buttons()

    def to_win_scene(self):
        win_scene = WinScene(self.game, self.teams)
        self.game.set_scene_active(win_scene)

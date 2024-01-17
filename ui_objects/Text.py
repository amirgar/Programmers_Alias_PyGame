from typing import TYPE_CHECKING
from enum import Enum
from math import floor
import pygame

from core.UIObject import UIObject

if TYPE_CHECKING:
    from core.Scene import Scene


class Alignment(Enum):
    CENTER = 1
    LEFT_CENTER = 2


class Text(UIObject):
    def __init__(self, position, size, scene: 'Scene',
                 text='', color=pygame.Color("black"), font=None, font_size=None):
        super().__init__(position, (size[0] - 15, size[1] - 15), color, scene)
        self._text = text
        self.font = font
        self.font_size = font_size

        self.alignment = Alignment.CENTER

        self.size_multiplier = 1
        self.get_size_multiplier()

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self.get_size_multiplier()

    def get_size_multiplier(self):
        self.size_multiplier = 1
        font_surface = self.get_font_surface()
        self.size_multiplier = min(self.width / font_surface.get_width(), self.height / font_surface.get_height())

    def set_text(self, text: str, font=None, font_color=pygame.Color("black")):
        self.text = text
        self.font = font
        self.color = font_color

    def render(self, surface: pygame.Surface):
        if not self._is_active:
            return

        text_surface = self.get_font_surface()

        text_x, text_y = 0, 0
        if self.alignment == Alignment.CENTER:
            text_x = self.center_position[0] - text_surface.get_width() // 2
            text_y = self.center_position[1] - text_surface.get_height() // 2
        elif self.alignment == Alignment.LEFT_CENTER:
            text_x = 0
            text_y = self.center_position[1] - text_surface.get_height() // 2

        surface.blit(text_surface, (text_x, text_y))
        # pygame.draw.rect(surface, (0, 0, 0), self.rect, 1)

    def get_font_surface(self):
        # if self.size_multiplier == 1:
        #     self.get_size_multiplier()

        font_size = self.font_size
        if not font_size:
            # font_size = int(self.width // len(self.text) * 1.3281472327365)
            font_size = floor(self.width * self.size_multiplier)

        font = pygame.font.Font(self.font, font_size)
        text_surface = font.render(self.text, True, self.color)

        return text_surface

    def get_surface(self) -> pygame.Surface:
        surface = pygame.Surface(self.size, pygame.SRCALPHA, 32)
        self.render(surface)

        return surface

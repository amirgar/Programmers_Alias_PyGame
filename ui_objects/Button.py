from typing import TYPE_CHECKING
import pygame

from core.UIObject import UIObject
from ui_objects.Text import Text

if TYPE_CHECKING:
    from core.Scene import Scene


class Button(UIObject):
    hovered_dark_percent = 10
    pressed_dark_percent = 25

    def __init__(self, position, size, color, scene: 'Scene',
                 text='', font=None, font_color=pygame.Color("black"), font_size=None):
        super().__init__(position, size, color, scene)
        self.font_color = font_color
        self.text = Text((0, 0), size, None, text, font_color, font, font_size)

        self.pressed = False
        self.released = False
        self.hovered = False

    @property
    def is_active(self) -> bool:
        return self.is_active

    @is_active.setter
    def is_active(self, value: bool):
        self._is_active = value
        self.text.is_active = value
        self.hovered = False

    def set_text(self, text: str, font: pygame.font.Font = None, font_color=None):
        self.text.set_text(text, font, font_color)

    def render(self, surface: pygame.Surface):
        if not self._is_active:
            return

        surface.blit(self.get_surface(), self.position)

    def get_surface(self) -> pygame.Surface:
        color = pygame.Color(self.color)
        hsva = color.hsva
        surface = pygame.Surface(self.size)

        dark_percent = self.get_dark_percent()
        color.hsva = (hsva[0], hsva[1], max(0.0, hsva[2] - dark_percent), hsva[3])
        surface.fill(color)

        text_surface = self.get_text_surface()
        text_x = self.width // 2 - text_surface.get_width() // 2
        text_y = self.height // 2 - text_surface.get_height() // 2
        surface.blit(text_surface, (text_x, text_y))

        return surface

    def get_text_surface(self) -> pygame.Surface:
        color = pygame.Color(self.font_color)
        hsva = color.hsva

        dark_percent = self.get_dark_percent()
        color.hsva = (hsva[0], hsva[1], max(0.0, hsva[2] - dark_percent), hsva[3])
        self.text.color = color

        return self.text.get_surface()

    def get_dark_percent(self) -> int:
        if self.pressed:
            return self.pressed_dark_percent
        if self.hovered:
            return self.hovered_dark_percent
        return 0

    def release(self):
        self.pressed = False
        if self.released:
            self.on_click()
        self.released = False

    def press(self):
        self.pressed = True

    def handle_event(self, event: pygame.event.Event):
        if not self._is_active:
            return

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_point_in_object(event.pos):
                self.press()

        elif event.type == pygame.MOUSEBUTTONUP:
            if self.pressed:
                if self.is_point_in_object(event.pos):
                    self.released = True
                self.release()

        elif event.type == pygame.MOUSEMOTION:
            if self.is_point_in_object(event.pos):
                self.hovered = True
            else:
                self.hovered = False

    def on_click(self):
        pass

    def __del__(self):
        self.is_active = False
        del self.text
        del self

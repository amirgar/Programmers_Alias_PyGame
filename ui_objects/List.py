from typing import TYPE_CHECKING
import pygame

from core.UIObject import UIObject

if TYPE_CHECKING:
    from core.Scene import Scene


class List(UIObject):
    def __init__(self, position, size, color, scene: 'Scene', children: list[UIObject] = None):
        super().__init__(position, size, color, scene)

        self.children = children
        if not children:
            self.children: list[UIObject] = []

        self.transparent = True

    def add_child(self, ui_object: UIObject):
        self.children.append(ui_object)

    def render(self, surface: pygame.Surface):
        if not self.is_active:
            return

        list_surface = pygame.Surface(self.size, pygame.SRCALPHA)
        if not self.transparent:
            list_surface.fill(self.color)

        y_offset = 0
        x_offset = 10
        for child in self.children:
            list_surface.blit(child.get_surface(), (x_offset, y_offset))
            y_offset += child.height

        cut_list_surface = pygame.Surface((self.width, y_offset), pygame.SRCALPHA)
        if not self.transparent:
            cut_list_surface.fill(self.color)

        cut_list_surface.blit(list_surface, (0, 0))
        surface.blit(cut_list_surface, self.position)

    def handle_event(self, event: pygame.event.Event):
        for child in self.children:
            child.handle_event(event)

    def __del__(self):
        self.is_active = False
        for child in self.children:
            del child
        del self

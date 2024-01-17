from typing import TYPE_CHECKING
import pygame

from core.GameObject import GameObject

if TYPE_CHECKING:
    from core.Scene import Scene


class UIObject(GameObject):
    def __init__(self, position, size, color, scene: 'Scene'):
        self.position = self.x, self.y = position
        self.size = self.width, self.height = size
        self.color = pygame.Color(color)
        self.scene = scene

        if scene:
            scene.add_child(self)

        self._is_active = True
        self.border = True

    def set_view(self, position, size, color):
        self.position = position
        self.size = size
        self.color = pygame.Color(color)

    @property
    def center_position(self):
        return self.x + self.width // 2, self.y + self.height // 2

    def move(self, point):
        self.position = self.x, self.y = point

    def scale(self, size):
        self.size = self.width, self.height = size

    @property
    def rect(self):
        return *self.position, *self.size

    def render(self, surface: pygame.Surface):
        pass

    def handle_event(self, event: pygame.event.Event):
        pass

    def get_surface(self) -> pygame.Surface:
        pass

    def is_point_in_object(self, point) -> bool:
        if point[0] < self.x or point[0] > self.x + self.width:
            return False
        if point[1] < self.y or point[1] > self.y + self.height:
            return False

        return True

from typing import TYPE_CHECKING
import pygame

from core.GameObject import GameObject

if TYPE_CHECKING:
    from Scene import Scene


class Game(GameObject):
    def __init__(self, size: tuple[int, int]):
        pygame.init()
        self.size = self.width, self.height = size

        self.screen = pygame.display.set_mode(size)
        self._background_color = pygame.Color(255, 255, 255)

        self.scenes: list['Scene'] = []
        self._active_scene: 'Scene' = None
        self._is_active = True

    @property
    def active_scene(self) -> 'Scene':
        return self._active_scene

    def add_scene(self, scene: 'Scene'):
        self.scenes.append(scene)
        scene.game = self

    def set_scene_active(self, scene: 'Scene'):
        if scene in self.scenes:
            self._active_scene = None
            for i in self.scenes:
                if i is not scene:
                    i.is_active = False
                else:
                    i.is_active = True
                    self._active_scene = i

    @property
    def background_color(self) -> pygame.Color:
        return self._background_color

    @background_color.setter
    def background_color(self, color):
        self._background_color = pygame.Color(color)

    def render(self, surface: pygame.Surface = None):
        self.screen.fill(self._background_color)
        if self._active_scene:
            self._active_scene.render(self.screen)

    def handle_event(self, event: pygame.event.Event):
        if self._active_scene:
            self._active_scene.handle_event(event)

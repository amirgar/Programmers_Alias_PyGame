import pygame


class GameObject:
    @property
    def is_active(self) -> bool:
        return self._is_active

    @is_active.setter
    def is_active(self, value: bool):
        if isinstance(value, bool):
            self._is_active = value
        else:
            raise ValueError("Scene.is_active принимает только boolean значения")

    def render(self, surface: pygame.Surface):
        pass

    def handle_event(self, event: pygame.event.Event):
        pass

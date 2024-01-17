import pygame
from core.Game import Game
from scenes.Menu import Menu


FPS = 60

if __name__ == "__main__":
    game = Game((600, 1000))

    menu_scene = Menu(game)
    game.set_scene_active(menu_scene)

    clock = pygame.time.Clock()
    running = True
    while running:
        # Обрабатываем ивенты
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game.handle_event(event)

        # Рисуем
        game.render()

        # Конец цикла
        clock.tick(FPS)
        pygame.display.flip()

    pygame.quit()

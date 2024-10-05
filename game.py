import pygame
from tower import Tower
from enviorment import Environment

class Game():
    def __init__(self):
        self.width = 1600
        self.height = 900

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.fps = 60
        self.clock = pygame.time.Clock()

        self.running = True

        self.tower = Tower("img/tower/tower_img.png", (self.width // 2, self.height // 2))
        self.tower_group = pygame.sprite.Group()
        self.tower_group.add(self.tower)

        x = self.width // 2
        y = self.height // 2
        self.bush_group = pygame.sprite.Group()
        self.bush_positions = [(x-600, y-300), (x+650, y+100), (x + 120, y+350),
                               (x-680, y+100), (x-400, y+350), (x + 200, y-350),
                               (x -200, y-350), (x + 600, y-200)]
        for pos in self.bush_positions:
            bush = Environment("img/bushes/bush1.png", pos)
            self.bush_group.add(bush)

    def main_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Получение позиции мыши при клике
                    mouse_pos = pygame.mouse.get_pos()
                    self.tower.shot(mouse_pos)

            self.screen.fill('green')

            self.tower.draw(self.screen)
            self.bush_group.draw(self.screen)

            pygame.display.update()
            self.clock.tick(self.fps)


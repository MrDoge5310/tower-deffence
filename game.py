import pygame
from tower import Tower

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

    def main_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill('green')

            self.tower_group.draw(self.screen)

            pygame.display.update()
            self.clock.tick(self.fps)


import pygame
from tower import Tower
from enviorment import Environment
from enemy import Enemy
import random
pygame.init()


class Game:
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

            self.enemy_group = pygame.sprite.Group()
            self.wave = 1
            self.max_enemies = 5
            self.spawn_enemies()
            self.font = pygame.font.SysFont("Arial", 28, True)

    def spawn_enemies(self):
        if self.wave % 5 == 0:
            self.max_enemies += 5
        quantity = random.randint(3, self.max_enemies + 1)

        for i in range(quantity):
            pos = random.choice(self.bush_positions)
            enemy = Enemy(self.tower.rect.center, (pos[0] + random.randint(10, 50), pos[1] + random.randint(10, 50)), "img/enemies/enemy1.png")
            self.enemy_group.add(enemy)

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

            wave_text = self.font.render(f"Wave: {self.wave}", 1, "white")
            self.screen.blit(wave_text, (10, 10))

            for enemy in self.enemy_group.sprites():
                if enemy.check_death():  # перевірка смерті ворога і видалення його в разі смерті
                    self.enemy_group.remove(enemy)
                    break
            if len(self.enemy_group.sprites()) == 0:
                self.wave += 1
                self.spawn_enemies()

            self.tower.update(self.screen, self.enemy_group)  # дописати параметр self.enemy_group
            self.enemy_group.update(self.screen, self.tower)
            self.bush_group.draw(self.screen)

            pygame.display.update()
            self.clock.tick(self.fps)


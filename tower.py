import pygame
import math


class Tower(pygame.sprite.Sprite):
    def __init__(self, image_name, pos):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.height = 300
        self.width = 300
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.archer_image = pygame.image.load("img/archer.png")
        self.archer_image = pygame.transform.scale(self.archer_image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.archer_pos = (self.rect.centerx - 50, self.rect.centery - 170)
        self.tower_image_pos = (self.rect.x, self.rect.y)
        self.rect.width -= 100
        self.rect.height -= 100
        self.rect.center = pos

        self.health = 1000
        self.attack_speed = 0.5
        self.reload = self.attack_speed * 60
        self.damage = 60
        self.protection = 10  # відсотків
        self.hp_lvl = 1
        self.attack_speed_lvl = 1
        self.damage_lvl = 1
        self.protection_lvl = 1

        self.can_attack = True
        self.cooldown = 60 / self.attack_speed

        self.font = pygame.font.SysFont("Arial", 26)
        self.text_pos = (self.archer_pos[0], self.archer_pos[1] - 20)

        self.projectiles = []

    def update(self, screen, enemy_group):
        self.draw(screen)
        for projectile in self.projectiles:
            projectile.update(screen)
            if projectile.check_hit(enemy_group):
                self.projectiles.remove(projectile)
        if self.reload != 0:
            self.reload -= 1

    def draw(self, screen):
        text = self.font.render(f"{self.health} HP", 1, "white")
        screen.blit(text, self.text_pos)

        screen.blit(self.image, self.tower_image_pos)
        screen.blit(self.archer_image, self.archer_pos)

    def take_damage(self, damage):
        self.health -= damage

    def shot(self, pos):
        if self.reload <= 0:
            self.projectiles.append(Projectile(self.archer_pos, pos, self.damage))
            self.reload = self.attack_speed * 60


class Projectile:
    def __init__(self, start_pos, target_pos, damage):
        self.image = pygame.image.load('img/arrow.png')
        self.width, self.height = 50, 50
        self.image = pygame.transform.scale(self.image, (self.height, self.width))

        self.damage = damage
        self.speed = 5

        self.x, self.y = start_pos
        self.target_x, self.target_y = target_pos

        # Рассчет направления и скорости
        self.angle = math.atan2(self.target_y - self.y, self.target_x - self.x)
        self.vel_x = self.speed * math.cos(self.angle)
        self.vel_y = self.speed * math.sin(self.angle)

        # Рассчет угла для поворота изображения (перевод в градусы)
        self.rotation_angle = -math.degrees(self.angle) - 90  # Угол поворота изображения (в градусах)

        # Повернутое изображение стрелы
        self.image = pygame.transform.rotate(self.image, self.rotation_angle)
        self.rect = self.image.get_rect(center=start_pos)

    def update(self, screen):
        self.x += self.vel_x
        self.y += self.vel_y
        self.rect.x, self.rect.y = (self.x, self.y)
        self.draw(screen)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def check_hit(self, enemy_group):  # додати параметр enemy_group
        if self.rect.x > 1500 or self.rect.x < 0 or self.rect.y > 1000 or self.rect.y < 0:  # оптимізовано(в учнів трішки по іншому буде написано)
            return True
        for enemy in enemy_group.sprites():  # перевірка на дотикання до ворогів
            if self.rect.colliderect(enemy.rect):
                enemy.take_damage(self.damage)  # ворог отримує урон
                return True

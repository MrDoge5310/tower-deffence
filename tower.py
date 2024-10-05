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

        self.health = 1000
        self.attack_speed = 1  # пострілів в секунду
        self.damage = 10
        self.protection = 10  # відсотків
        self.hp_lvl = 1
        self.attack_speed_lvl = 1
        self.damage_lvl = 1
        self.protection_lvl = 1

        self.can_attack = False
        self.cooldown = 60 / self.attack_speed

        self.projectiles = []

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.archer_image, self.archer_pos)

    def take_damage(self):
        pass

    def shot(self):
        if self.can_attack:
            if self.cooldown == self.speed:
                self.projectiles.append(Projectile(self.rect.center, self.damage))
                self.cooldown = 0
            else:
                self.cooldown += 1


class Projectile:
    def __init__(self, start_pos, target_pos, damage):
        self.image = pygame.image.load('img/arrow.png')
        self.width, self.height = 50, 25
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
        self.rotation_angle = -math.degrees(self.angle)  # Угол поворота изображения (в градусах)

        # Повернутое изображение стрелы
        self.image = pygame.transform.rotate(self.image, self.rotation_angle)
        self.rect = self.image.get_rect(center=start_pos)

    def move(self, direction):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, 'yellow', self.rect)

    def check_hit(self):
        pass

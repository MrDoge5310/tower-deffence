import pygame
import math
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, target, pos, image_name):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.height = 64
        self.width = 64
        self.image = pygame.transform.scale(self.image, (self.height, self.width))
        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.target = target
        self.health = 100
        self.protection = 20 / 100
        self.speed = 1
        self.damage = 10
        self.pos = pos

        self.x, self.y = pos
        self.target_x, self.target_y = self.target

        # Рассчет направления и скорости
        self.angle = math.atan2(self.target_y - self.y, self.target_x - self.x)
        self.vel_x = self.speed * math.cos(self.angle)
        self.vel_y = self.speed * math.sin(self.angle)

        # Рассчет угла для поворота изображения (перевод в градусы)
        self.rotation_angle = -math.degrees(self.angle) + 45  # Угол поворота изображения (в градусах)

        # Повернутое изображение стрелы
        self.image = pygame.transform.rotate(self.image, self.rotation_angle)
        self.rect = self.image.get_rect(center=pos)

        self.health_bar_bg = pygame.Rect(self.rect.x, self.rect.y - 50, self.rect.width, 5)
        self.health_bar = pygame.Rect(self.health_bar_bg.x, self.health_bar_bg.y, self.rect.width, 5)

    def calculate_incoming_damage(self):
        pass

    def take_damage(self, damage):
        self.health -= damage

    def check_death(self):
        if self.health <= 0:
            return True

    def update(self, screen):
        self.move(self.target)
        self.draw(screen)

    def draw(self, scr):
        scr.blit(self.image, self.rect)
        pygame.draw.rect(scr, "red", self.health_bar_bg)
        pygame.draw.rect(scr, "white", self.health_bar)


    def move(self, target):
        self.x += self.vel_x
        self.y += self.vel_y
        self.rect.center = (self.x, self.y)

        self.health_bar_bg.center = (self.x, self.y - 50)
        self.health_bar.x, self.health_bar.y = self.health_bar_bg.topleft
        self.health_bar.width = self.health * (self.health_bar_bg.width / 100)
import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, health, damage, protection, speed, pos, image_name):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.height = 32
        self.width = 32
        self.image = pygame.transform.scale(self.image, (self.height, self.width))

        self.health = health
        self.protection = protection / 100
        self.speed = speed
        self.damage = damage
        self.pos = pos

    def calculate_incoming_damage(self):
        pass
    def take_damage(self):
        pass
    def draw(self):
        pass
    def move(self):
        pass
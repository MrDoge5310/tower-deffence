import pygame


class Tower(pygame.sprite.Sprite):
    def __init__(self, image_name, health, speed, damage, protection):
        pygame.sprite.Sprite.__init__(self)
        self.image_name = pygame.image.load(image_name)
        self.height = 32
        self.width = 32
        self.image = pygame.transform.scale(self.image, (self.height, self.width))

        self.health = health
        self.speed = speed
        self.damage = damage
        self.protection = protection
        self.hp_lvl = 0
        self.attack_speed_lvl = 0
        self.damage_lvl = 0
        self.protection_lvl = 0

        self.can_attack = False
        self.cooldown = 0

        def take_damage(self):
            pass

        def attack(self):
            if self.can_attack:
                if self.cooldown == self.speed:
                    pass
                    self.cooldown = 0
                else:
                    self.cooldown += 1


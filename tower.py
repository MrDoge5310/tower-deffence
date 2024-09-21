import pygame


class Tower(pygame.sprite.Sprite):
    def __init__(self, image_name, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_name)
        self.height = 100
        self.width = 50
        self.image = pygame.transform.scale(self.image, (self.height, self.width))

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

        def take_damage(self):
            pass

        def attack(self):
            if self.can_attack:
                if self.cooldown == self.speed:
                    pass
                    self.cooldown = 0
                else:
                    self.cooldown += 1


class Projectile:
    def __init__(self, pos, damage, image_name):
        self.image = pygame.image.load('img/arrow.png')
        self.width, self.height = 50, 25
        self.image = pygame.transform.scale(self.image, (self.height, self.width))

        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.damage = damage
        self.speed = 5
        self.direction = direction

    def move(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, 'yellow', self.rect)

    def launch(self, direction):
        pass

    def check_hit(self):
        pass

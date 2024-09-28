import pygame


class Environment(pygame.sprite.Sprite):
    def __init__(self, filename, pos):
        super().__init__()
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (300, 200))
        self.rect = self.image.get_rect()
        self.rect.center = pos

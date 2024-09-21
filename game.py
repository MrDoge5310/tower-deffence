import pygame
from tower import Tower

class Game():
    def __init__(self):
        self.width = 1600
        self.height = 900

        self.screen = pygame.display.set_mode()
        self.fps = 60
        self.clock = pygame.time.Clock()

        self.running = True

        self.tower = Tower("tower.png")

        def main_loop(self):
            if self.running:
                pass
import pygame
from core.settings import VERDE

class Exit:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = VERDE

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

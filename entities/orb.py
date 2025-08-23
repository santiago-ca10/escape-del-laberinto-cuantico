import pygame
from core.settings import AMARILLO

class Orb:
    def __init__(self, x, y, r=8):
        self.r = r
        self.rect = pygame.Rect(x - r, y - r, 2*r, 2*r)
        self.color = AMARILLO
        self.taken = False

    def try_collect(self, player_rect):
        if not self.taken and self.rect.colliderect(player_rect):
            self.taken = True
            return True
        return False

    def draw(self, surface):
        if not self.taken:
            center = self.rect.center
            pygame.draw.circle(surface, self.color, center, self.r)

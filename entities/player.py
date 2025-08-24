import pygame
from core.settings import AZUL

class Player:
    def __init__(self, x, y, size=15, speed=4):
        self.rect = pygame.Rect(x, y, size, size)
        self.speed = speed
        self.invuln_ms = 0

    def reset_pos(self, x, y):
        self.rect.topleft = (x, y)
        self.invuln_ms = 350

    def update(self, keys, walls, dt_ms):
        vel = self.speed
        dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel
        dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * vel

        self.rect.x += dx
        for w in walls:
            if self.rect.colliderect(w):
                if dx > 0: self.rect.right = w.left
                if dx < 0: self.rect.left = w.right

        self.rect.y += dy
        for w in walls:
            if self.rect.colliderect(w):
                if dy > 0: self.rect.bottom = w.top
                if dy < 0: self.rect.top = w.bottom

        if self.invuln_ms > 0:
            self.invuln_ms = max(0, self.invuln_ms - dt_ms)

    @property
    def invulnerable(self):
        return self.invuln_ms > 0

    def herido(self, dur_ms=800):
        self.invuln_ms = max(self.invuln_ms, dur_ms)

    def draw(self, surface):
        x, y = self.rect.center
        # Cabeza
        pygame.draw.circle(surface, (200,200,255), (x, y-15), 10)
        # Tronco
        pygame.draw.line(surface, AZUL, (x, y-5), (x, y+15), 3)
        # Brazos
        pygame.draw.line(surface, AZUL, (x, y), (x-15, y-5), 3)
        pygame.draw.line(surface, AZUL, (x, y), (x+15, y-5), 3)
        # Piernas
        pygame.draw.line(surface, AZUL, (x, y+15), (x-10, y+30), 3)
        pygame.draw.line(surface, AZUL, (x, y+15), (x+10, y+30), 3)

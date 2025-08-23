import pygame
from core.settings import ROJO, MAGENTA

class Trap:
    """Trampa estática o móvil (vaivén)"""
    def __init__(self, x, y, w, h, move_axis=None, rango=0, speed=0):
        self.rect = pygame.Rect(x, y, w, h)
        self.base_pos = (x, y)
        self.move_axis = move_axis  # 'x' o 'y' o None
        self.rango = rango
        self.speed = speed
        self.t = 0.0  # tiempo para animación

    def update(self, dt_ms):
        if self.move_axis:
            self.t += (dt_ms / 1000.0) * self.speed
            offset = int(self.rango * 0.5 * (1 + pygame.math.Vector2(1,0).rotate_rad(self.t).x))
            x0, y0 = self.base_pos
            if self.move_axis == 'x':
                self.rect.x = x0 - self.rango//2 + offset
                self.rect.y = y0
            elif self.move_axis == 'y':
                self.rect.x = x0
                self.rect.y = y0 - self.rango//2 + int(self.rango * 0.5 * (1 + pygame.math.Vector2(0,1).rotate_rad(self.t).y))

    def draw(self, surface):
        pygame.draw.rect(surface, ROJO if not self.move_axis else MAGENTA, self.rect)

import pygame
from core.settings import ANCHO, ALTO, TILE
from entities.orb import Orb
from entities.trap import Trap
from entities.exit import Exit

class Level2:
    name = "Laberinto Cuántico - Nivel 2"
    time_limit = 45  # más exigente

    def __init__(self):
        self.walls = self._build_walls()
        self.orbs  = self._build_orbs()
        # Trampas móviles
        self.traps = [
            Trap(TILE*10, TILE*8, TILE//2, TILE//2, move_axis='x', rango=TILE*6, speed=3.0),
            Trap(TILE*5,  TILE*11, TILE//2, TILE//2, move_axis='y', rango=TILE*5, speed=2.5),
            Trap(TILE*15, TILE*6, TILE//2, TILE//2),
        ]
        self.exit  = Exit(ANCHO - TILE*2, TILE*2, TILE, TILE)
        self.spawn = (TILE*2, ALTO - TILE*3)

    def _build_walls(self):
        W = []
        # Bordes
        W.append(pygame.Rect(0, 0, ANCHO, TILE))
        W.append(pygame.Rect(0, ALTO - TILE, ANCHO, TILE))
        W.append(pygame.Rect(0, 0, TILE, ALTO))
        W.append(pygame.Rect(ANCHO - TILE, 0, TILE, ALTO))

        # Más laberinto
        for i in range(2, 18):
            if i != 9:
                W.append(pygame.Rect(i*TILE, 5*TILE, TILE, TILE))
        for i in range(3, 14):
            if i not in (7, 10):
                W.append(pygame.Rect(8*TILE, i*TILE, TILE, TILE))
        for i in range(6, 18):
            W.append(pygame.Rect(13*TILE, i*TILE - 3*TILE, TILE, TILE))

        return W

    def _build_orbs(self):
        coords = [
            (TILE*4, TILE*3), (TILE*7, TILE*9), (TILE*9, TILE*12),
            (TILE*12, TILE*7), (TILE*16, TILE*10)
        ]
        return [Orb(x, y) for (x, y) in coords]

    def update(self, dt_ms):
        for t in self.traps:
            t.update(dt_ms)

    def draw(self, surface):
        for w in self.walls:
            pygame.draw.rect(surface, (50,50,50), w)
        for o in self.orbs:
            o.draw(surface)
        for t in self.traps:
            t.draw(surface)
        self.exit.draw(surface)

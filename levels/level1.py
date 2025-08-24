import pygame
from core.settings import ANCHO, ALTO, TILE
from entities.orb import Orb
from entities.trap import Trap
from entities.exit import Exit

class Level1:
    name = "Laberinto Cuántico - Nivel 1"
    time_limit = 50  # segundos

    def __init__(self):
        self.walls = self._build_walls()
        self.orbs  = self._build_orbs()
        self.traps = self._build_traps()
        self.exit  = Exit(ANCHO - TILE*2, ALTO - TILE*2, TILE, TILE)
        self.spawn = (TILE + 6, TILE + 6)

    def _build_walls(self):
        W = []
        # Bordes
        W.append(pygame.Rect(0, 0, ANCHO, TILE))            # arriba
        W.append(pygame.Rect(0, ALTO - TILE, ANCHO, TILE))  # abajo
        W.append(pygame.Rect(0, 0, TILE, ALTO))             # izquierda
        W.append(pygame.Rect(ANCHO - TILE, 0, TILE, ALTO))  # derecha

        # Algunas paredes internas (pasillos)
        for i in range(2, 18):
            W.append(pygame.Rect(i*TILE, 4*TILE, TILE, TILE))
        for i in range(3, 12):
            W.append(pygame.Rect(6*TILE, i*TILE, TILE, TILE))
        for i in range(8, 18):
            W.append(pygame.Rect(12*TILE, i*TILE - 2*TILE, TILE, TILE))
        for i in range(1, 10):
            W.append(pygame.Rect(16*TILE, i*TILE, TILE, TILE))

        return W

    def _build_orbs(self):
        # Orbes en puntos de paso
        coords = [
            (TILE*3, TILE*2), (TILE*8, TILE*3), (TILE*10, TILE*6),
            (TILE*5, TILE*9), (TILE*14, TILE*5), (TILE*16, TILE*9)
        ]
        return [Orb(x, y) for (x, y) in coords]

    def _build_traps(self):
        # Trampas estáticas en pasillos
        Ts = [
            Trap(TILE*7, TILE*7, TILE//2, TILE//2),
            Trap(TILE*11, TILE*4, TILE//2, TILE//2),
        ]
        return Ts

    def update(self, dt_ms):
        for t in self.traps:
            t.update(dt_ms)

    def draw(self, surface):
        for w in self.walls:
            pygame.draw.rect(surface, (40,40,40), w)
        for o in self.orbs:
            o.draw(surface)
        for t in self.traps:
            t.draw(surface)
        self.exit.draw(surface)

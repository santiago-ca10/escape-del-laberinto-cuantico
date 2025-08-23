import pygame
from core.utils import texto
from core.settings import ANCHO, ALTO, AZUL, BLANCO

class StartScreen:
    def draw(self, surface):
        surface.fill((0,0,0))
        texto(surface, "Escape del Laberinto Cuántico", 48, (ANCHO//2, ALTO//2 - 120), AZUL, True)
        texto(surface, "Mueve con Flechas. Recolecta orbes. Evita trampas.", 24, (ANCHO//2, ALTO//2 - 40), BLANCO)
        texto(surface, "Llega a la salida antes de que se acabe el tiempo.", 24, (ANCHO//2, ALTO//2), BLANCO)
        texto(surface, "Presiona ESPACIO para empezar", 28, (ANCHO//2, ALTO//2 + 100), BLANCO)

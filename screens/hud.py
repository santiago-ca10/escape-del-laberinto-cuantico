import pygame
from core.utils import texto_topleft
from core.settings import BLANCO, ROJO

class HUD:
    def draw(self, surface, vidas, puntaje, tiempo_restante):
        texto_topleft(surface, f"Vidas: {vidas}", 24, (16, 12), BLANCO, True)
        texto_topleft(surface, f"Puntos: {puntaje}", 24, (16, 40), BLANCO, True)
        color_tiempo = BLANCO if tiempo_restante > 10 else ROJO
        texto_topleft(surface, f"Tiempo: {int(tiempo_restante)}", 24, (16, 68), color_tiempo, True)

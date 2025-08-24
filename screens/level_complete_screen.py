import pygame
from core.utils import texto
from core.settings import ANCHO, ALTO, VERDE, AZUL, BLANCO
from .start_screen import Button

class LevelCompleteScreen:
    def __init__(self, continue_callback, back_callback):
        font = pygame.font.SysFont("Arial", 28)
        self.font = font
        self.buttons = [
            Button("Continuar", (ANCHO//2-100, ALTO//2, 200, 50), VERDE, AZUL, continue_callback),
            Button("Volver al inicio", (ANCHO//2-100, ALTO//2+70, 200, 50), VERDE, AZUL, back_callback)
        ]

    def draw(self, surface, puntaje):
        surface.fill((0,0,0))
        texto(surface, "¡Nivel completado!", 48, (ANCHO//2, 120), VERDE, True)
        texto(surface, f"Puntaje actual: {puntaje}", 32, (ANCHO//2, 200), BLANCO)
        for b in self.buttons:
            b.draw(surface, self.font)

    def handle_event(self, event):
        for b in self.buttons:
            b.check_click(event)

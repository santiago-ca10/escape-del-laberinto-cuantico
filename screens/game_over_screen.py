from core.utils import texto
from core.settings import ANCHO, ALTO, BLANCO, ROJO, VERDE

class GameOverScreen:
    def __init__(self):
        self.resultado = "DERROTA"
        self.puntaje = 0

    def set(self, resultado, puntaje):
        self.resultado = resultado
        self.puntaje = puntaje

    def draw(self, surface):
        surface.fill((0,0,0))
        color = VERDE if self.resultado == "VICTORIA" else ROJO
        titulo = "¡VICTORIA!" if self.resultado == "VICTORIA" else "GAME OVER"
        texto(surface, titulo, 60, (ANCHO//2, ALTO//2 - 80), color, True)
        texto(surface, f"Puntaje final: {self.puntaje}", 36, (ANCHO//2, ALTO//2), BLANCO)
        texto(surface, "Presiona R para reiniciar", 26, (ANCHO//2, ALTO//2 + 100), BLANCO)

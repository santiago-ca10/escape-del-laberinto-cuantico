import pygame
from core.settings import ANCHO, ALTO, AZUL, VERDE, BLANCO
from core.utils import texto

class Button:
    def __init__(self, text, rect, color, hover_color, action):
        self.text = text
        self.rect = pygame.Rect(rect)
        self.color = color
        self.hover_color = hover_color
        self.action = action

    def draw(self, surface, font):
        mouse_pos = pygame.mouse.get_pos()
        is_hover = self.rect.collidepoint(mouse_pos)
        color = self.hover_color if is_hover else self.color

        pygame.draw.rect(surface, color, self.rect)
        label = font.render(self.text, True, BLANCO)
        label_rect = label.get_rect(center=self.rect.center)
        surface.blit(label, label_rect)

    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.action()

class StartScreen:
    def __init__(self, start_callback, quit_callback):
        font = pygame.font.SysFont("Arial", 28)
        self.font = font
        self.buttons = [
            Button("Iniciar", (ANCHO//2-100, ALTO//2-40, 200, 50), AZUL, VERDE, start_callback),
            Button("Salir", (ANCHO//2-100, ALTO//2+40, 200, 50), AZUL, VERDE, quit_callback)
        ]

    def draw(self, surface):
        surface.fill((0,0,0))
        texto(surface, "Escape del Laberinto Cuántico", 48, (ANCHO//2, 120), AZUL, True)
        for b in self.buttons:
            b.draw(surface, self.font)

    def handle_event(self, event):
        for b in self.buttons:
            b.check_click(event)

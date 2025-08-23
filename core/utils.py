import pygame
from .settings import FUENTE_NOMBRE, BLANCO

def texto(superficie, msg, tamaño, centro, color=BLANCO, negrita=False):
    font = pygame.font.SysFont(FUENTE_NOMBRE, tamaño, bold=negrita)
    surf = font.render(msg, True, color)
    rect = surf.get_rect(center=centro)
    superficie.blit(surf, rect)

def texto_topleft(superficie, msg, tamaño, topleft, color=BLANCO, negrita=False):
    font = pygame.font.SysFont(FUENTE_NOMBRE, tamaño, bold=negrita)
    surf = font.render(msg, True, color)
    rect = surf.get_rect(topleft=topleft)
    superficie.blit(surf, rect)

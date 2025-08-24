import pygame, sys
from core.settings import ANCHO, ALTO, FPS, NEGRO, VIDAS_INICIALES, PUNTOS_ORBE, BONUS_NIVEL
from core.game_state import PANTALLA_INICIO, JUGANDO, LEVEL_COMPLETE, GAME_OVER, ResultadoFinal
from levels import LevelManager
from entities import Player
from screens import StartScreen, GameOverScreen, HUD, LevelCompleteScreen

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Escape del Laberinto Cuántico")
    reloj = pygame.time.Clock()

    # Callbacks
    def start_game():
        nonlocal estado, niveles, nivel, player, vidas, puntaje, inicio_nivel_ms
        estado = JUGANDO
        niveles = LevelManager()
        nivel = niveles.level
        player = Player(*nivel.spawn)
        vidas = VIDAS_INICIALES
        puntaje = 0
        inicio_nivel_ms = pygame.time.get_ticks()

    def quit_game():
        pygame.quit()
        sys.exit()

    start_screen = StartScreen(start_game, quit_game)
    game_over_screen = GameOverScreen()
    hud = HUD()
    level_complete_screen = None

    estado = PANTALLA_INICIO
    niveles = LevelManager()
    nivel = niveles.level
    player = Player(*nivel.spawn)
    vidas = VIDAS_INICIALES
    puntaje = 0
    inicio_nivel_ms = pygame.time.get_ticks()

    corriendo = True
    while corriendo:
        dt_ms = reloj.tick(FPS)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                corriendo = False
            if estado == PANTALLA_INICIO:
                start_screen.handle_event(e)
            elif estado == LEVEL_COMPLETE:
                level_complete_screen.handle_event(e)
            elif estado == GAME_OVER and e.type == pygame.KEYDOWN and e.key == pygame.K_r:
                estado = PANTALLA_INICIO

        pantalla.fill(NEGRO)

        if estado == PANTALLA_INICIO:
            start_screen.draw(pantalla)

        elif estado == JUGANDO:
            keys = pygame.key.get_pressed()
            nivel.update(dt_ms)
            player.update(keys, nivel.walls, dt_ms)

            if not player.invulnerable:
                for t in nivel.traps:
                    if player.rect.colliderect(t.rect):
                        vidas -= 1
                        player.herido()
                        if vidas <= 0:
                            estado = GAME_OVER
                            game_over_screen.set(ResultadoFinal.DERROTA, puntaje)
                        else:
                            nivel = niveles.level
                            player.reset_pos(*nivel.spawn)
                        break

            for o in nivel.orbs:
                if o.try_collect(player.rect):
                    puntaje += PUNTOS_ORBE

            if player.rect.colliderect(nivel.exit.rect):
                puntaje += BONUS_NIVEL
                if not niveles.next_level():
                    estado = GAME_OVER
                    game_over_screen.set(ResultadoFinal.VICTORIA, puntaje)
                else:
                    def continuar():
                        nonlocal estado, nivel, player, inicio_nivel_ms
                        nivel = niveles.level
                        player.reset_pos(*nivel.spawn)
                        inicio_nivel_ms = pygame.time.get_ticks()
                        estado = JUGANDO
                    def volver():
                        nonlocal estado
                        estado = PANTALLA_INICIO
                    level_complete_screen = LevelCompleteScreen(continuar, volver)
                    estado = LEVEL_COMPLETE

            nivel.draw(pantalla)
            player.draw(pantalla)
            hud.draw(pantalla, vidas, puntaje, 30)  # tiempo simple

        elif estado == LEVEL_COMPLETE:
            level_complete_screen.draw(pantalla, puntaje)

        elif estado == GAME_OVER:
            game_over_screen.draw(pantalla)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

import pygame, sys, time
from core.settings import ANCHO, ALTO, FPS, NEGRO, VIDAS_INICIALES, PUNTOS_ORBE, BONUS_NIVEL
from core.game_state import PANTALLA_INICIO, JUGANDO, GAME_OVER, ResultadoFinal
from levels import LevelManager
from entities import Player
from screens import StartScreen, GameOverScreen, HUD

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Escape del Laberinto Cuántico")
    reloj = pygame.time.Clock()

    # Estados / Pantallas
    estado = PANTALLA_INICIO
    start_screen = StartScreen()
    game_over_screen = GameOverScreen()
    hud = HUD()

    # Juego
    niveles = LevelManager()
    nivel = niveles.level
    player = Player(*nivel.spawn)
    vidas = VIDAS_INICIALES
    puntaje = 0

    # Tiempo por nivel
    inicio_nivel_ms = pygame.time.get_ticks()

    def resetear_nivel():
        nonlocal nivel, player, inicio_nivel_ms
        niveles.reload_current()
        nivel = niveles.level
        player.reset_pos(*nivel.spawn)
        inicio_nivel_ms = pygame.time.get_ticks()

    def iniciar_nivel_nuevo():
        nonlocal nivel, player, inicio_nivel_ms
        nivel = niveles.level
        player.reset_pos(*nivel.spawn)
        inicio_nivel_ms = pygame.time.get_ticks()

    corriendo = True
    while corriendo:
        dt_ms = reloj.tick(FPS)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                corriendo = False
            if estado == PANTALLA_INICIO and e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                estado = JUGANDO
                # reiniciar todo por si venimos de antes
                niveles = LevelManager()
                nivel = niveles.level
                player = Player(*nivel.spawn)
                vidas = VIDAS_INICIALES
                puntaje = 0
                inicio_nivel_ms = pygame.time.get_ticks()
            if estado == GAME_OVER and e.type == pygame.KEYDOWN and e.key == pygame.K_r:
                estado = PANTALLA_INICIO

        pantalla.fill(NEGRO)

        if estado == PANTALLA_INICIO:
            start_screen.draw(pantalla)

        elif estado == JUGANDO:
            # Entrada
            keys = pygame.key.get_pressed()

            # Actualizar nivel (trampas móviles)
            nivel.update(dt_ms)

            # Player
            player.update(keys, nivel.walls, dt_ms)

            # Colisiones con trampas
            if not player.invulnerable:
                for t in nivel.traps:
                    if player.rect.colliderect(t.rect):
                        vidas -= 1
                        player.herido()
                        if vidas <= 0:
                            estado = GAME_OVER
                            game_over_screen.set(ResultadoFinal.DERROTA, puntaje)
                        else:
                            resetear_nivel()
                        break

            # Recolecta orbes
            for o in nivel.orbs:
                if o.try_collect(player.rect):
                    puntaje += PUNTOS_ORBE

            # Llegó a la salida (nivel completado si recogió X orbes o simplemente por llegar)
            if player.rect.colliderect(nivel.exit.rect):
                # Bonus por completar
                puntaje += BONUS_NIVEL
                # Siguiente nivel o victoria
                if not niveles.next_level():
                    estado = GAME_OVER
                    game_over_screen.set(ResultadoFinal.VICTORIA, puntaje)
                else:
                    iniciar_nivel_nuevo()

            # Tiempo restante
            elapsed_s = (pygame.time.get_ticks() - inicio_nivel_ms) / 1000.0
            tiempo_restante = max(0.0, nivel.time_limit - elapsed_s)
            if tiempo_restante <= 0:
                vidas -= 1
                if vidas <= 0:
                    estado = GAME_OVER
                    game_over_screen.set(ResultadoFinal.DERROTA, puntaje)
                else:
                    resetear_nivel()

            # Dibujo
            nivel.draw(pantalla)
            player.draw(pantalla)
            hud.draw(pantalla, vidas, puntaje, tiempo_restante)

        elif estado == GAME_OVER:
            game_over_screen.draw(pantalla)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

import pygame
import sys
import random

# Inicializamos Pygame
pygame.init()

# Dimensiones de la ventana del juego
ANCHO = 600
ALTO = 400
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("🐍 Snake Game")

# Definimos colores RGB
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

# Tamaño del bloque (para la serpiente y la comida)
TAM_BLOQUE = 20

# Velocidad del juego (FPS)
velocidad = 10

# Fuente para los textos
fuente = pygame.font.SysFont("Arial", 25)

# Función para mostrar texto en pantalla
def mostrar_mensaje(texto, color, x, y):
    mensaje = fuente.render(texto, True, color)
    VENTANA.blit(mensaje, [x, y])

# Función principal del juego
def juego():
    # Lista que representa la serpiente (cada parte es una [x, y])
    snake = [[100, 50]]
    direccion = 'DERECHA'  # Dirección inicial

    # Genera la comida alineada con el grid
    comida = [random.randint(0, (ANCHO - TAM_BLOQUE) // TAM_BLOQUE) * TAM_BLOQUE,
              random.randint(0, (ALTO - TAM_BLOQUE) // TAM_BLOQUE) * TAM_BLOQUE]

    reloj = pygame.time.Clock()
    puntos = 0
    corriendo = True

    while corriendo:
        # Procesar eventos del teclado y cerrar ventana
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and direccion != 'DERECHA':
                    direccion = 'IZQUIERDA'
                elif evento.key == pygame.K_RIGHT and direccion != 'IZQUIERDA':
                    direccion = 'DERECHA'
                elif evento.key == pygame.K_UP and direccion != 'ABAJO':
                    direccion = 'ARRIBA'
                elif evento.key == pygame.K_DOWN and direccion != 'ARRIBA':
                    direccion = 'ABAJO'

        # Mover la cabeza de la serpiente
        cabeza = list(snake[0])  # Copia la posición actual

        if direccion == 'DERECHA':
            cabeza[0] += TAM_BLOQUE
        elif direccion == 'IZQUIERDA':
            cabeza[0] -= TAM_BLOQUE
        elif direccion == 'ARRIBA':
            cabeza[1] -= TAM_BLOQUE
        elif direccion == 'ABAJO':
            cabeza[1] += TAM_BLOQUE

        # Verificar colisiones (paredes o consigo misma)
        if (cabeza[0] < 0 or cabeza[0] >= ANCHO or
            cabeza[1] < 0 or cabeza[1] >= ALTO or
            cabeza in snake):
            mostrar_mensaje("💀 GAME OVER", ROJO, ANCHO // 2 - 80, ALTO // 2)
            pygame.display.update()
            pygame.time.wait(2000)
            return  # Sale del juego

        # Añadir nueva cabeza
        snake.insert(0, cabeza)

        # Verificar si comió la comida
        if cabeza == comida:
            puntos += 1  # Sumar puntos
            # Generar nueva comida alineada con el grid
            comida = [random.randint(0, (ANCHO - TAM_BLOQUE) // TAM_BLOQUE) * TAM_BLOQUE,
                      random.randint(0, (ALTO - TAM_BLOQUE) // TAM_BLOQUE) * TAM_BLOQUE]
        else:
            # Si no comió, elimina la cola (para simular movimiento)
            snake.pop()

        # Dibujar todo
        VENTANA.fill(NEGRO)  # Fondo negro

        # Dibujar cada parte de la serpiente
        for parte in snake:
            pygame.draw.rect(VENTANA, VERDE, (*parte, TAM_BLOQUE, TAM_BLOQUE))

        # Dibujar la comida
        pygame.draw.rect(VENTANA, ROJO, (*comida, TAM_BLOQUE, TAM_BLOQUE))

        # Mostrar los puntos
        mostrar_mensaje(f"Puntos: {puntos}", VERDE, 10, 10)

        # Actualizar la pantalla
        pygame.display.update()
        reloj.tick(velocidad)

# Ejecutar el juego
juego()
pygame.quit()
sys.exit()

# Importamos las librerías necesarias
import pygame        # Librería para gráficos 2D y eventos
import sys           # Para salir del programa correctamente

# Inicializamos Pygame
pygame.init()

# Configuramos las dimensiones de la ventana (ancho y alto)
ANCHO = 600
ALTO = 400

# Creamos la ventana del juego
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Robot Móvil")  # Título de la ventana

# Definimos algunos colores en formato RGB
BLANCO = (255, 255, 255)     # Color de fondo
AZUL = (0, 100, 255)         # Color del robot

# Configuramos el tamaño del robot (será un cuadrado)
robot_size = 40

# Posición inicial del robot (en el centro de la pantalla)
x = ANCHO // 2
y = ALTO // 2

# Velocidad a la que se moverá el robot en píxeles por fotograma
velocidad = 5

# Reloj para controlar los frames por segundo (FPS)
reloj = pygame.time.Clock()

# Variable para mantener el bucle principal corriendo
corriendo = True

# Comienza el bucle principal del juego
while corriendo:
    reloj.tick(60)  # Limitamos a 60 FPS

    # Revisamos todos los eventos del sistema (teclas, cerrar ventana, etc.)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Si se cierra la ventana
            corriendo = False           # Salimos del bucle

    # Capturamos el estado del teclado
    teclas = pygame.key.get_pressed()

    # Movemos el robot según las teclas presionadas
    if teclas[pygame.K_LEFT]:   # Flecha izquierda
        x -= velocidad
    if teclas[pygame.K_RIGHT]:  # Flecha derecha
        x += velocidad
    if teclas[pygame.K_UP]:     # Flecha arriba
        y -= velocidad
    if teclas[pygame.K_DOWN]:   # Flecha abajo
        y += velocidad

    # Evitamos que el robot se salga de la pantalla
    x = max(0, min(x, ANCHO - robot_size))   # Límite horizontal
    y = max(0, min(y, ALTO - robot_size))    # Límite vertical

    # Dibujamos el fondo de color blanco
    VENTANA.fill(BLANCO)

    # Dibujamos el robot (un rectángulo azul)
    pygame.draw.rect(VENTANA, AZUL, (x, y, robot_size, robot_size))

    # Actualizamos el contenido de la ventana
    pygame.display.update()

# Cerramos Pygame cuando se sale del bucle
pygame.quit()
sys.exit()

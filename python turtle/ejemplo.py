import turtle           # Importa la biblioteca turtle para gráficos mediante dibujo de líneas.
import colorsys         # Importa la biblioteca colorsys para manejar colores en el espacio HSV.

tortuguita = turtle.Turtle()     # Crea un objeto "turtle" llamado 'tortuguita' para dibujar en pantalla.
tortuguita.speed(0)              # Establece la velocidad del turtle al máximo (0 = más rápido posible).
turtle.bgcolor("black") # Cambia el color de fondo de la ventana a negro, para resaltar los colores del dibujo.
h = 0                   # Inicializa una variable 'h' para representar el tono (hue) en HSV (valor entre 0 y 1).

# Bucle que se ejecuta 360 veces para dibujar una espiral colorida
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 1)  # Convierte el color HSV (h, saturación=1, valor=1) a RGB. 
                                      # Esto produce colores vibrantes que recorren el arco iris.
    tortuguita.pencolor(c)                     # Establece el color del lápiz al color RGB generado.
    tortuguita.forward(i)                      # Avanza hacia adelante una distancia creciente (i), lo que forma la espiral.
    tortuguita.right(59)                       # Gira 59 grados a la derecha, creando el patrón circular.
    h += 0.002                        # Aumenta ligeramente el valor de 'h' para el próximo color (desplazamiento en el espectro).

turtle.done()  # Finaliza el dibujo y mantiene la ventana abierta.
#



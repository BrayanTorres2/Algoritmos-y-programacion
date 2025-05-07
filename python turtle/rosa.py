import turtle
import math
import colorsys

# Configuración de pantalla
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Rosa de colores con Turtle")

# Configuración del turtle
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

# Parámetros de la rosa
n_petalos = 6  # número de pétalos (puede cambiarse para otras formas)
radio = 300
pasos = 360

# Generar colores en gradiente con HLS
colores = [colorsys.hsv_to_rgb(i/pasos, 1.0, 1.0) for i in range(pasos)]

# Dibujo de la rosa
for i in range(pasos):
    angulo = math.radians(i)
    r = radio * math.sin(n_petalos * angulo)
    x = r * math.cos(angulo)
    y = r * math.sin(angulo)
    
    # Convertir color a formato RGB 0-255
    color = colores[i]
    t.pencolor((color[0], color[1], color[2]))
    t.goto(x, y)

# Finalizar
turtle.done()

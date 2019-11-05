# -*- coding: utf-8 -*-
"""
@author: Nicolas Rogers, Diego Herrera y Juan Ortiz
"""

import turtle
from PIL import Image

BLOCK_SIZE = 19

im = Image.open('maze.jpg')
pixels = im.load()
width, height = im.size
offset = int(BLOCK_SIZE / 2)


maze = [
  [
    int(pixels[x + offset, y + offset][0] < 125)
    for x in range(0, height, BLOCK_SIZE)
  ]
  for y in range(0, width, BLOCK_SIZE)
]


maze[20][15] = 2
maze[19][20] = 1

colores = ["white","black"]


pantalla = turtle.Screen()
turtle.setup(1920,1080)
dibujaLaberinto = turtle.Turtle() ## Tortuga usada para cualquier funcion que tenga relación con el dibujo del laberinto base.
rT = turtle.Turtle() ## Tortuga usada para resolver los laberintos.

## Para dibujar el laberinto se requiere de una función que dibuje cajas por cada obstaculo representado por 1 en Binario

def caja(tortuga,tamaño):
    tortuga.begin_fill()
    for a in range(3):
        tortuga.forward(tamaño)
        tortuga.right(360/4)
    tortuga.end_fill()
    tortuga.right(90)
    tortuga.forward(tamaño)
    tortuga.left(90)
    tortuga.forward(tamaño)
    tortuga.right(90)

## Se implementa dentro de la función dibujarLaberinto, la función caja, de manera que para los valores de longitud Lista de Laberinto[i] se corra un ciclo for con los valores de la
## sublista, por lo tanto va a cambiar de color basado en el 0 o 1 que se encuentre en la posición y asi se dibuja una caja blanca(no obstaculo) o una caja negra

def dibujarLaberinto(tortuga,laberinto,tamaño):
    p = list(laberinto)
    tortuga.setposition(-300,300)
    for i in range(0, len(p)):
        for j in range(0, len(p[i])):
            if p[i][j] == 0:
                tortuga.color(colores[0])
                caja(tortuga,tamaño)
            elif p[i][j] == 2:
                tortuga.color(colores[0])
                caja(tortuga,tamaño)
            else:
                tortuga.color(colores[1])
                caja(tortuga,tamaño)
        tortuga.penup()
        tortuga.setposition(-300,tortuga.ycor()-tamaño)
        tortuga.pendown()
    tortuga.hideturtle()
    

            
coordsx = []
coordsy = []          

def SolucionBinaria(laberinto,x, y):

    if laberinto[x][y] == 2:
        print("Solucion encontrada")
        return True
    elif laberinto[x][y] == 1:
        print("Pared encontrada",(x,y))
        return False
    elif laberinto[x][y] == 3:
        print("Celda ya visitada",(x,y))
        return False
    

    laberinto[x][y] = 3 ## Marcar la celda como visitada

    if ((x < len(laberinto)-1 and SolucionBinaria(laberinto,x+1, y)) ## Chequear los distintos casos posibles
        or (y > 0 and SolucionBinaria(laberinto,x, y-1))
        or (x > 0 and SolucionBinaria(laberinto,x-1, y))
        or (y < len(laberinto)-1 and SolucionBinaria(laberinto,x, y+1))):
        coordsx.append(-x*30+280)
        coordsy.append(y*30-280)

        return True

    return False

         

pantalla.tracer(0)
dibujarLaberinto(dibujaLaberinto,maze,30)
SolucionBinaria(maze,0,9)

## Realizar la solución binaria por medio de recursión retornando True o  False en los di

coordsx.reverse()
coordsy.reverse()

rT.setposition(-30,320)
rT.color("red")
rT.begin_fill()
for a in range(0,len(coordsx)):
    rT.setposition(coordsy[a],coordsx[a])

pantalla.update()
pantalla.exitonclick()  

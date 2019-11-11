#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:11:05 2019

@author: hipatia
"""


# -*- coding: utf-8 -*-
"""
@author: Nicolas Rogers, Diego Herrera y Juan Ortiz
"""

import turtle
from PIL import Image
import random

BLOCK_SIZE = 19

im = Image.open('/home/hipatia/Desktop/maze.jpg')
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


maze[20][15] = 0 
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
#        elif p[abs(y)][x-1] == 0:
#            rT.setheading(0)
#            rT.left(90)
#            rT.forward(tamaño)
                caja(tortuga,tamaño)
            else:
                tortuga.color(colores[1])
                caja(tortuga,tamaño)
        tortuga.penup()
        tortuga.setposition(-300,tortuga.ycor()-tamaño)
        tortuga.pendown()
    tortuga.hideturtle()
    

        
        
def resolverLaberinto(laberinto,tamaño):
    p = list(laberinto)
    r = p[0]
    l = p[len(p)-1]
    rT.penup()
    if 0 in r:
        m = r.index(0)
    else:
        if 0 in p[1]:
            m = r.index(0)
    rT.setposition(-300+m*tamaño+tamaño/2,290)
    rT.right(90)
    rT.pendown()
    rT.pensize(3)
    rT.color("red")
    if 0 in l:
        xFinal = l.index(0)
    yFinal = len(p)
    
    while (rT.xcor()+300)/tamaño != xFinal  and ((rT.ycor()-290)/tamaño) != yFinal  :
        x = int((rT.xcor()+300)/tamaño)
        y = (int((rT.ycor()-290)/tamaño))
        if p[abs(y)+1][x] == 0: ## Espacio abajo vacio.
            rT.setheading(0)
            rT.right(90)
            rT.forward(tamaño)
        elif p[abs(y)][x+1] == 0: ## Espacio de la derecha vacio
            rT.setheading(0)
            rT.forward(tamaño)
        elif p[abs(y)][x+1] == 0 and p[abs(y)][x-1] == 0:
            NumAleatorio = random.randint(0,1)
            if NumAleatorio == 0:
                rT.setheading(0)
                rT.forward(tamaño)
            else:
                rT.setheading(0)
                rT.left(90)
                rT.forward(tamaño)
#        elif not p[abs(y)][x-1] == 1:
#            rT.setheading(0)
#            rT.left(90)
#            rT.forward(tamaño)
        else:
            break
        print(y)
        print(x)





        
            

pantalla.tracer(0)
dibujarLaberinto(dibujaLaberinto,maze,30)
resolverLaberinto(maze,30)
pantalla.update()
pantalla.exitonclick()  

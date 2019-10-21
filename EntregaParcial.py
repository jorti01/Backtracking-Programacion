# -*- coding: utf-8 -*-
"""
@author: Nicolas Rogers, Diego Herrera y Juan Ortiz
"""

import turtle
import cv2
import numpy as np






img = cv2.imread("D:/maze.jpg",0)
ret, binaryImage = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY)
print(binaryImage)


laberinto=[[1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]]
laberinto.append([1,0,1,1,0,0,0,0,0,1,0,0,0,1,0,1,])
laberinto.append([1,0,0,1,0,1,1,1,0,0,0,1,0,1,0,1,])
laberinto.append([1,1,0,1,0,0,0,1,1,0,1,0,0,1,0,1,])
laberinto.append([1,0,0,0,0,1,0,1,0,0,1,0,1,0,0,1,])
laberinto.append([1,0,1,0,1,0,0,1,1,1,1,1,0,1,0,1,])
laberinto.append([1,0,1,1,1,0,1,1,0,0,0,0,0,0,0,1,])
laberinto.append([1,0,0,0,1,1,1,0,0,1,0,1,0,1,1,1,])
laberinto.append([1,0,1,0,1,0,0,0,1,1,0,1,0,1,0,1,])
laberinto.append([1,0,1,0,1,0,1,1,0,0,1,0,0,0,0,1,])
laberinto.append([1,0,1,0,1,0,0,0,1,0,1,1,0,1,1,1,])
laberinto.append([1,0,1,1,1,1,1,0,0,0,1,0,0,0,0,1,])
laberinto.append([1,0,0,0,0,0,1,1,1,0,1,0,1,1,0,1,])
laberinto.append([1,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1,])
laberinto.append([1,0,0,0,1,0,0,0,0,0,1,0,0,1,0,2,])
laberinto.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,])
p = list(laberinto)
print(p)
dibujaLaberinto = turtle.Turtle() ## Tortuga usada para cualquier funcion que tenga relación con el dibujo del laberinto base.


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

        
def dibujarLaberinto(tortuga,laberinto):
    for a in range(len(p)):
        for b in range(len(p)):
            if p[x][b] == 1:
                caja(tortuga,20)
                
        
        
dibujarLaberinto(dibujaLaberinto,30)
    

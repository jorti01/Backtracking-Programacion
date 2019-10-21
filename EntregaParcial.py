# -*- coding: utf-8 -*-
"""
@author: Nicolas Rogers, Diego Herrera y Juan Ortiz
"""

import turtle
import cv2
import numpy as np





img = cv2.imread("D:/maze.jpg", 0)
print(img)


laberinto = []




dibujaLaberinto = turtle.Turtle() ## Tortuga usada para cualquier funcion que tenga relación con el dibujo del laberinto base.


## Para dibujar el laberinto se requiere de una función que dibuje cajas por cada obstaculo representado por 1 en Binario

def caja(tortuga,tamaño):
    tortuga.begin
    for a in range(5):
        tortuga.forward(tamaño)
        tortuga.right(360/4)

# -*- coding: utf-8 -*-
"""
@author: Nicolas Rogers, Diego Herrera y Juan Ortiz
"""

import turtle

## Para dibujar el laberinto se requiere de una función que dibuje cajas por cada obstaculo representado por 1 en Binario

dibujaLaberinto = turtle.Turtle()
def caja(tortuga,tamaño):
    tortuga.begin
    for a in range(5):
        tortuga.forward(tamaño)
        tortuga.right(360/4)
        
    
        
caja(dibujaLaberinto,40)
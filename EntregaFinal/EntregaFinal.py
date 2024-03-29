
# -*- coding: utf-8 -*-
"""
@author: Nicolas Rogers, Diego Herrera y Juan Ortiz ## Analisis de Imagen: bug 
"""

import turtle
from PIL import Image

BLOQUE = 19 ## Tamaño del bloque para agrupar los pixeles en la imagen, ancho de la imagen / columnas del laberinto, en el ejemplo = 399/21 = 19

im = Image.open('maze.jpg') ## Cargar la imagen en la variable im
pixels = im.load() ## Cargar los pixeles de la imagen contenida en im
width, height = im.size ## Sacar los valores de ancho y alto de la variable im.
offset = int(BLOQUE / 2) ## Valor de offset, calculo de la distancia entre el centro y el borde de la imagen.


maze = [ ## Se crea la lista de listas, en la cual se tendran los distintos valores que van en el rango de y entre 0, la altura y el tamaño Bloque, en x entre 0, ancho, y tamaño bloque
  [
    int(pixels[x + offset, y + offset][0] < 125)
    for x in range(0, height, BLOQUE)
  ]
  for y in range(0, width, BLOQUE)
]


maze[20][13] = 2 ## Omitir. Se creó salida para test laberinto. En caso cambiar imagen test, eliminar linea 27 y 28
maze[19][20] = 1 ## Omitir. Se creó salida para test laberinto.

colores = ["white","black"] ## Los dos colores a usarse, blanco para los 0 y negro para los 1


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

def dibujarLaberinto(tortuga,laberinto):
    tamaño = 30
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
    

            
coordsx = [] ## Lista para coordenadas de x, solución
coordsy = [] ## Lista para coordenadas de y, solución       

def SolucionBinaria(laberinto,x, y):
    if 0 in laberinto[len(laberinto)-1]:
        laberinto[len(laberinto)-1][laberinto.index(0)] = 2
    else:
        pass
    tamaño = 30
    ## Tres posibles casos en terminos binarios.
    if laberinto[x][y] == 2: ## Si se encuentra una celda con el numero 2, esta es la salida. Retornar true.
        print("Solucion encontrada")
        return True
    elif laberinto[x][y] == 1: ## Si se encuentra una celda con el numero 1, esta es una pared. Retornar false.
        print("Pared encontrada",(x,y))
        return False
    elif laberinto[x][y] == 3:  ## Si se encuentra una celda con el numero 3, esta celda ya fue visitada. Retornar false.
        print("Celda ya visitada",(x,y))
        return False
    

    laberinto[x][y] = 3 ## Marcar la celda como visitada

    if ((x < len(laberinto)-1 and SolucionBinaria(laberinto,x+1, y)) ## Chequear los distintos casos posibles, comenzando con la celda de abajo
        or (y > 0 and SolucionBinaria(laberinto,x, y-1)) ## Segundo caso, celda de la izquierda
        or (x > 0 and SolucionBinaria(laberinto,x-1, y)) ## Tercer caso, celda de arriba
        or (y < len(laberinto)-1 and SolucionBinaria(laberinto,x, y+1))): ## Cuarto caso, celda de la derecha
        coordsx.append(-x*tamaño+280) ## Coordenadas de X que cumplen los parametros por lo tanto, soluciones validas
        coordsy.append(y*tamaño-280) ## Coordenadas de Y que cumplen los parametros por lo tanto, soluciones validas

        return True ## Si se encuentra una celda valida, retorna true 
      
    return False ## Celda Invalida, false.

         

pantalla.tracer(0)  ## Acelerar el dibujo.
dibujarLaberinto(dibujaLaberinto,maze) ## Usa funcion caja y en la lista de listas hace uso de los colores blanco y negro para las casillas.
SolucionBinaria(maze,0,9) ## Por medio de recursión y los distintos casos encuentra la salida.

## Revertir las coordenadas dado que estan en el orden de salida, llegada. Por ende se requieren en el orden opuesto.
coordsx.reverse()
coordsy.reverse()
## Definir la posición de la tortuga solución en la casilla que tenga 0 en la primera columna del laberinto
rT.penup()
rT.setposition(coordsy[0],coordsx[0])
rT.pendown()
rT.color("red")
rT.pensize(5)
for a in range(0,len(coordsx)): ## Para las coordenadas dentro de solucionX y solucionY, poner la posición de la tortuga siguiendo el camino entrada/salida
    rT.setposition(coordsy[a],coordsx[a])

pantalla.update() ## Actualizar pantalla
pantalla.exitonclick()  ## Al hacer click, cerrar pantalla
turtle.bye()
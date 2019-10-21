
import turtle
import cv2
import numpy as np






img = cv2.imread("D:/maze.jpg",0)
ret, binaryImage = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY)
print(binaryImage)

colores = ["white","black"]


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

## Se implementa dentro de la función dibujarLaberinto, la función caja, de manera que para los valores de longitud Lista de Laberinto[i] se corra un ciclo for con los valores de la
## sublista, por lo tanto va a cambiar de color basado en el 0 o 1 que se encuentre en la posición y asi se dibuja una caja blanca(no obstaculo) o una caja negra

def dibujarLaberinto(tortuga,laberinto,tamaño):
    tortuga.setposition(0,0)
    for i in range(0, len(p)):
        for j in range(0, len(p[i])):
            if p[i][j] == 0:
                tortuga.color(colores[0])
                caja(tortuga,tamaño)
            else:
                tortuga.color(colores[1])
                caja(tortuga,tamaño)
        tortuga.penup()
        tortuga.setposition(0,tortuga.ycor()-tamaño)
        tortuga.pendown()
dibujaLaberinto.speed(10)
dibujarLaberinto(dibujaLaberinto,p,30)
    

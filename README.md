# Backtracking-Programacion

El programa toma como base una imagen en formato .jpg / .png para luego convertirlo a Binario por medio del modulo Pillow.

Por medio de la lectura y con un valor offset, se convierten los distintos pixeles agrupados a 0 y 1 contenidos en sublistas. Pudiendo así interpretar el laberinto como una matriz con valores x,y usados para llamar la sublista y el valor dentro de esta.

Con los valores dentro de las sublistas se utiliza Backtracking y Recursion para identificar las celdas validas y así guardar las coordenas de estas celdas en otra lista.

Se procede a dibujar el laberinto por medio de un ciclo for que permite inspeccionar valor por valor y dependiendo si es un 0 o un 1 se dibuja una caja transparente o negra. Luego para la solución por medio de las coordenadas del paso anterior se usa la funcion setposition de turtle teniendo así de entrada a salida cada celda de la solución dibujada.



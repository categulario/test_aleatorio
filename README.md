# Test Aleatrio

Comprueba qué tan aleatorio es el algoritmo del profe de variable compleja

## Problema

Hay 6 alumnos en la clase, y se necesita escoger rápidamente y al azar a uno de ellos para que pase al pizarrón a exponer un ejercicio.

## Algoritmo

La propuesta fue tomar la hora, sumar las cantidades (hora, minuto, segundo) y luego reducir hasta que solo quede un dígito, tomar módulo 6 y escoger a uno de nosotros.

## Cuestionamiento

De momento pareciera que dada la forma de tomar los módulos, la distribución de la probabilidad no es uniforme.

## Solución

Consideré el espacio de todas las horas posibles (00:00:00 hasta 23:59:59) apliqué el algoritmo para ver qué sucedía, además consideré la muestra solamente tomando el horario de clases (10-12 am)

## Resultados

![Por día](https://raw.githubusercontent.com/developingo/test_aleatorio/master/img/dia.png "Por día")

![Horario de clases](https://raw.githubusercontent.com/developingo/test_aleatorio/master/img/hora.png "Horario de clases")

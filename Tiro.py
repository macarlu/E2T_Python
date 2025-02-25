import math
angulo = 0
velocidad = 0
gravedad = 9.8

def calculo_tiro():
    velocidad = float(input("Introduzca la velocidad inicial: "))
    angulo = float(input("Introduzca el angulo: "))
    gravedad = float(input("Introduzca el valor de la gravedad: "))
    angulo_rad=math.radians(angulo)
    alcance=(velocidad**2)*math.sin(2*angulo_rad)/gravedad
    distancia = round(alcance,2)
    altura_max = (velocidad**2)*(math.sin(angulo_rad**2)/(2*gravedad))
    altura = round(altura_max,2)
    print(f"La distancia recorrida es de {distancia} con una altura máxima de {altura}")

calculo_tiro()
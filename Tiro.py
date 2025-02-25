import math
angulo_rad=math.radians(angulo)
alcance=(velocidad**2)*math.sin(2*angulo_rad)/gravedad
altura_max = (velocidad**2)*(math.sin(angulo_rad**2)/(2*gravedad))
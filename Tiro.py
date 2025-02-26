import math

'''
Elabora un programa para el cálculo de el lanzamiento de un misil.

Para empezar hay que importar "math" para poder usar las fórmulas que se dan más adelante.

Se creará la clase "Lanzamiento" y tendrá varios métodos:

Método para establecer el ángulo de lanzamiento ("setter")
Método para establecer la velocidad
Para los dos datos anteriores también hacer métodos para consultar el valor ("gettters")
La gravedad es una variable que va en el código (ej. gravedad = 9.81)
Un método que realice el cálculo del alcance y la altura máxima y nos imprima por pantalla los resultados
El código python de las fórmulas del método que realiza los cálculos son:

angulo_rad = math.radians(angulo)   # convierte ángulo de grados a radianes 
alcance = (velocidad**2) * math.sin(2*angulo_rad) / gravedad 
altura_max = (velocidad**2) * (math.sin(angulo_rad)**2) / (2*gravedad) 

Plus de excelencia:

Hacer un menú que tenga las opciones de establecer los datos, consultarlos y realizar el cálculo del lanzamiento.

(se puede mantener el menú siempre corriendo con un "while True" por ejemplo)'''

resultado = 0

class Lanzamiento:

    gravedad = 9.81
    alcance = 0
    altura_max = 0
    

    def __init__(self,angulo,velocidad):
        self.angulo = angulo
        self.velocidad = velocidad  

    def establecer_angulo(self,angulo):
        self.angulo = angulo
        angulo = float(input("Introduzca el ángulo de lanzamiento: "))

    def establecer_velocidad(self,velocidad):
        self.velocidad = velocidad
        velocidad = float(input("Introduzca la velocidad inicial: "))
                 
    def calculo_tiro(self,alcance,altura_max,angulo,velocidad,gravedad):
        self.alcance = alcance
        self.altura_max = altura_max  
        angulo_rad=math.radians(angulo)
        alcance=(velocidad**2)*math.sin(2*angulo_rad)/gravedad
        altura_max = (velocidad**2)*(math.sin(angulo_rad**2)/(2*gravedad))
        
        
        print(f"La distancia recorrida es de {alcance} con una altura máxima de {altura_max}")
    
    resultado = calculo_tiro()
    print(resultado)


    
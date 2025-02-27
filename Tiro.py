import math ; import sys
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


 
class Lanzamiento:
    
    def __init__(self,angulo=0,velocidad=0,gravedad=9.81,alcance=0,altura_max=0):
        self.angulo = angulo
        self.velocidad = float(velocidad)
        self.gravedad = gravedad 
        self.alcance = float(alcance)
        self.altura_maxima = float(altura_max)

    def get_establecer_angulo(self):
        return self.angulo

    def set_establecer_angulo(self,angulo):
        self.angulo = angulo
        
    def get_establecer_velocidad(self):
        return self.velocidad

    def set_establecer_velocidad(self,velocidad):
        self.velocidad = velocidad
        
    def get_calculo_alcance(self):
        return self.alcance
    
    def set_calculo_alcance(self,alcance):
        self.alcance = alcance
        
    def get_calculo_altura(self):
        return self.altura_max
    
    def set_calculo_altura(self,altura_max):
        self.altura_max = altura_max
        
    def calcular_parametros(self):
        angulo_rad = math.radians(self.angulo)
        alcance = round((self.velocidad**2) * math.sin(2*angulo_rad) / self.gravedad,2)
        altura_max = round((self.velocidad**2) * (math.sin(angulo_rad)**2) / (2*self.gravedad),2)

        self.set_calculo_alcance(alcance)
        self.set_calculo_altura(altura_max)
    
    def resultado(self):
        print(f"Para un angulo de {self.angulo}º y una velocidad inicial de {self.velocidad} m/s.\nLa distancia recorrida es de {self.alcance} metros con una altura máxima de {self.altura_max} metros.")

def generar_menu():  
    lanzamiento = Lanzamiento()
    while True:
        print("\nMenú:\n")
        print("1. Angulo de Lanzamiento")
        print("2. Velocidad de Lanzamiento")
        print("3. Calcular Parámetros(alcance y altura)")
        print("4. Generar informe de resultados")
        print("0. Salir")
        seleccion = int(input("Seleccione un número para realizar la acción: "))
        if seleccion == 1:
            angulo = float(input("Introduzca el ángulo de lanzamiento: "))
            lanzamiento.set_establecer_angulo(angulo)
        elif seleccion == 2:
            velocidad = float(input("Introduzca la velocidad inicial: "))
            lanzamiento.set_establecer_velocidad(velocidad)
        elif seleccion == 3:
            lanzamiento.calcular_parametros()
            print("Cálculos realizados satisfactoriamente.")
        elif seleccion == 4:
            lanzamiento.resultado()
        elif seleccion == 0:
            print(f"Saliendo del programa...")
            sys.exit()
        else:
            print( f"El número elegido no es correcto, intentelo de nuevo\n\n")

generar_menu()

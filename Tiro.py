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

angulo = 0
velocidad = 0
gravedad = 9.81
alcance = 0
altura_max = 0
seleccion = 0
 
class Lanzamiento:

    def __init__(self,angulo,velocidad,alcance,altura_max):
        self.angulo = angulo
        self.velocidad = velocidad  
        self.alcance = alcance
        self.altura_maxima = altura_max

    def get_establecer_angulo(self):
        return self.angulo


    def set_establecer_angulo(self,angulo):
        self.angulo = angulo
        
    #get_establecer_angulo()

    def get_establecer_velocidad(self):
        return self.velocidad

    def set_establecer_velocidad(self,velocidad):
        self.velocidad = velocidad
        
    #establecer_velocidad() 

    def calculo_alcance(self):
                
        angulo_rad=math.radians(self.get_establecer_angulo)
        alcance=(self.get_establecer_velocidad**2)*math.sin(2*angulo_rad)/gravedad
        return alcance
        
    def calculo_altura(self):
        
        angulo_rad=math.radians(self.get_establecer_angulo)
        altura_max = (self.get_establecer_velocidad**2)*(math.sin(angulo_rad**2)/(2*gravedad))
        return altura_max
    
    #calculo_altura()

    def resultado():
        print(f"La distancia recorrida es de {alcance} con una altura máxima de {altura_max}")

def generar_menu():  

    while True:
        print("Menú:")
        print("1. Angulo de Lanzamiento")
        print("2. Velocidad de Lanzamiento")
        print("3. Alcance obtenido")
        print("4. Altura máxima alcanzada")
        print("5. Generar informe")
        print("0. Salir")
        seleccion = int(input("Seleccione un número para realizar la acción: "))
                            
                
        if seleccion == 1:
            angulo = float(input("Introduzca el ángulo de lanzamiento: "))
            
        elif seleccion == 2:
            velocidad = float(input("Introduzca la velocidad inicial: "))
            Lanzamiento(angulo,velocidad)
        elif seleccion == 3:
            Lanzamiento.calculo_alcance()
            Lanzamiento.calculo_altura()
            Lanzamiento.resultado()
        elif seleccion == 0:
            print(f"Saliendo del programa...")
            sys.exit()
        
        else:
            return f"El número elegido no es correcto, intentelo de nuevo"
    
generar_menu()


    
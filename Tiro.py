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

alcance = 0
altura_max = 0

class Lanzamiento:

    gravedad = 9.81
    
    def __init__(self,angulo,velocidad,gravedad,alcance,altura_max,,):
        self.angulo = angulo
        self.velocidad = velocidad  
        self.gravedad = gravedad
        self.alcance = alcance
        self.altura_maxima = altura_max

    def establecer_angulo():
        angulo = float(input("Introduzca el ángulo de lanzamiento: "))
        return angulo
    establecer_angulo()
    def establecer_velocidad():
        velocidad = float(input("Introduzca la velocidad inicial: "))
        return velocidad
    establecer_velocidad()            
    def calculo_tiro():
         
        angulo_rad=math.radians(angulo)
        alcance=(velocidad**2)*math.sin(2*angulo_rad)/gravedad
        altura_max = (velocidad**2)*(math.sin(angulo_rad**2)/(2*gravedad))
        return alcance,altura_max
    calculo_tiro()
    def generar_menu():
        
        while True:
            seleccion=(int(input("Seleccione un número para realizar la acción: ")))
            print("Menú:")
            print("1. Angulo de Lanzamiento")
            print("2. Velocidad de Lanzamiento")
            print("3. Alcance y Altura máxima alcanzada")
            print("0. Salir")
            
            return seleccion
            if  0 < seleccion > 3:
                print("El número seleccionado no es correcto, vuelva a intentarlo")
                

    def menu_funcional(self,seleccion,establecer_angulo,establecer_velocidad):
        self.seleccion = seleccion
        self.establecer_angulo = establecer_angulo
        self.establecer_velocidad = establecer_velocidad
        
        if seleccion == 1:
            establecer_angulo()
        
        elif seleccion == 2:
            establecer_velocidad()
        
        elif seleccion == 3:
            print(f"La distancia recorrida es de {alcance} con una altura máxima de {altura_max}")
    
#generar_menu()


    
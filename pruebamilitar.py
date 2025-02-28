'''
Crea una clase "Alumno" en la que todos tengan:
    - Nombre
    - Apellidos
    - Edad
Crea los setter y getter de esos atributos.
Crea un metodo que me diga se el alumno es mayor de edad.'''

class Alumno:
    
    def __init__(self):
        self.nombre = " " #Tambien se le puede pedir al usuario aqui con un input 
        self.apellidos = " "#Tambien se le puede pedir al usuario aqui con un input 
        self.edad = int()#Tambien se le puede pedir al usuario aqui con un input 

    def set_nombre(self,nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_apellidos(self,apellidos):
        self.apellidos = apellidos
    
    def get_apellidos(self):
        return self.edad
    
    def set_edad(self,edad):
        self.edad = edad

    def comprobar_edad(self):
        if self.edad >= 18:
            print(f"El alumno es mayor de edad porque tiene {self.edad}")

alumno1 = Alumno()
alumno1.set_nombre("Juan") #Si no lo he pedido lo tengo que añadir de esta forma
alumno1.set_apellidos("Garcia") #Si no lo he pedido lo tengo que añadir de esta forma
alumno1.set_edad(22) #Si no lo he pedido lo tengo que añadir de esta forma

alumno1.comprobar_edad()


    



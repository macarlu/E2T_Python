import random
'''
Crea la clase Profesor.
Va a tener:
    - Nombre ----> getter
    - Asignatura ----> setter y getter
    - Salario ----> es el nº de horas de clase por X€/h
    - '''

class Profesor:
    
    def __init__(self):
        self.nombre = " "
        self.asignatura = " "
        self.salario = float()

    def get_nombre(self):
        return self.nombre
        
    def set_asignatura(self, asignatura):
        self.asignatura = asignatura

    def get_asignatura(self):
        return self.asignatura
    
    def set_salario(self,salario):
        self.salario = salario
        
    def get_salario(self):
        return self.salario

    def calcular_sueldo():
        num_horas = int(input("Introduzca las horas de clases que ha impartido este mes: "))
        valor_horas = 50
        salario = num_horas * valor_horas
        print(f"su sueldo este mes es de: {salario}€")

profesor1 = Profesor()
profesor1.nombre = "Pepe"
Profesor.calcular_sueldo()

    


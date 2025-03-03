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
    
def calcular_sueldo():
    
    num_horas = random.randint(18,40)
    valor_horas = 67
    


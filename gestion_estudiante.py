import random
import json
import os
'''
Ejercicio 5: Gestión de estudiantes
Crea una clase Estudiante con atributos para nombre, edad y calificación.
Implementa métodos getter y setter, y un método que determine si el estudiante aprobó (calificación mayor o igual a 6).
'''

class Estudiante:

    def __init__(self, archivo ="estudiantes.json"):
        self.archivo = archivo
        self.lista_alumnos = ["Maria Lopez", "Juan Garcia", "Antonio Mora", "Jesus Lemos",
                            "Ana Rodriguez", "Raul Mira", "Carla Alejo", "Martina Besada",
                            "Javier Vazquez", "Mara Cano"]
        self.alumnos = self.cargar_archivo()
        self.aprobados = []

    def cargar_archivo(self):
     
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, "r") as f:
                    return json.load(f)
            else:
                return []
        except Exception as e:
            print(f"Se ha producido el error: {e} al cargar los datos del programa.")
            return []
        
    def set_agregar_alumnos(self,nombre):#Genera un alumno aleatorio y lo añade a la lista.
        
        self.edad = random.randint(18, 35)
        self.calificacion = random.randint(2, 10)

        self.alumno = {"nombre": nombre, "edad": self.edad, "calificacion": self.calificacion}
        self.alumnos.append(self.alumno)

    def get_agregar_alumnos(self):
        return self.alumnos
        
    def set_cargar_alumnos(self, cantidad=10):#Carga una cantidad de alumnos sin repetir nombres.
        nombres_disponibles = list(set(self.lista_alumnos) - {alumno["nombre"] for alumno in self.alumnos})
    
        if not nombres_disponibles:
            print("No hay más nombres disponibles para agregar.")
            return

        cantidad = min(cantidad, len(nombres_disponibles))  # Evita pedir más nombres de los disponibles

        for nombre in random.sample(nombres_disponibles, cantidad):
            self.set_agregar_alumnos(nombre)


    def guardar_archivo(self):#Guarda en un archivo JSON.
        with open(self.archivo, "w") as f:
            json.dump(self.alumnos, f, indent=4)
            print(f"Archivo guardado correctamente\n")

    def mostrar_archivo(self):
        if self.alumnos:
            for alumno in self.alumnos:
                print(f"Nombre y Apellido: {alumno['nombre']}, Edad: {alumno['edad']}, Calificación: {alumno['calificacion']}\n")
        else:
            print("El archivo está vacio")

    def set_aprobado(self):
        self.aprobados = [alumno for alumno in self.alumnos if alumno["calificacion"] >= 5]

    def get_aprobado(self):
        if not self.aprobados:# Verificamos si la lista está vacía
            print("No hay alumnos aprobados.")
        else:
            print("Alumnos aprobados:\n")
            for alumno in self.aprobados:
                print(f"Nombre: {alumno['nombre']}, Calificación: {alumno['calificacion']}\n")


clase1 = Estudiante()
clase1.set_cargar_alumnos()
clase1.guardar_archivo()
clase1.mostrar_archivo()
clase1.set_aprobado()
clase1.get_aprobado()
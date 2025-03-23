import random

lista_alumnos = ["Maria Lopez", "Juan Garcia", "Antonio Mora", "Jesus Lemos","Ana Rodriguez",
                 "Raul Mira", "Carla Alejo", "Martina Besada", "Javier Vazquez", "Mara Cano"]
alumnos = []

def set_agregar_alumnos():#Genera un alumno aleatorio y lo añade a la lista.
        nombre = random.choice(lista_alumnos)
        edad = random.randint(18, 35)
        calificacion = random.randint(0, 10)

        alumno = {"nombre": nombre, "edad": edad, "calificacion": calificacion}
        alumnos.append(alumno)
        print(alumnos)  

def set_cargar_alumnos(cantidad = 10):
        for cantidad in alumnos:
                set_agregar_alumnos()
                
           

set_agregar_alumnos()
set_cargar_alumnos()  
    
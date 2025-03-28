import json
import os
'''
Ejercicio 15: Crea un programa que gestione una lista de tareas.
Define una clase Tarea con atributos titulo, descripcion y completada.
Implementa métodos para añadir, eliminar, marcar como completada y listar todas las tareas. Guarda la 
lista de tareas en un archivo JSON y permite cargarla al iniciar el programa. Usa la librería os para 
gestionar los archivos y directorios necesarios'''

class Tarea:
    
    def __init__(self,title = "recursos/tareas.json"):
        self.archivo = title
        self.tareas = self.cargar_tareas()
    
    def cargar_tareas(self):
        if os.path.exists(self.archivo):
            with open(self.archivo,"r") as f:
                return json.loads(f)
        else:
            return {}
        
    def anadir_tarea(self):
        self.titulo = input("Introduzca el nombre de la tarea: ")
        self.descripcion = input("Introduzca las descripcion de la tarea: ")
        self.completada = "No completada"  
        self.tareas = {
            "Description" : self.descripcion,
            "Estado" : self.completada
        }
        
    def eliminar_tarea(self):
        self.delete = input("Introduzca la tarea que quiere borrar: ")
        self.tareas.pop(self.delete)
    
    def marcar_como_completada(self):
        self.marcar = input("Introduzca la tarea que quiere marcar como completada: ")
        self.tareas[self.marcar]['Estado'] = "Tarea completada"

    def listar_tareas(self):
        if self.tareas:
            for nombre, info in self.tareas.items:
                print(f"El nombre de la tarea es: {self.titulo}")
                print(f"Su descripcion es: {self.descripcion}")
                print(f"Se encuentra en: {self.completada}")
        else:
            print("No hay tareas registradas")
    
    def menu():
        while True:
            print("\n_________Menú________\n")
            print("1. ")

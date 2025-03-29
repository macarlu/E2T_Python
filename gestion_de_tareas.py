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
            try:
                with open(self.archivo,"r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return {}  # Si hay un error, devuelve un diccionario vacío
            else:
                return {}
        
    def anadir_tarea(self):
        self.titulo.capitalize() = input("Introduzca el nombre de la tarea: ")
        self.descripcion.capitalize() = input("Introduzca las descripcion de la tarea: ")
        self.descripcion = self.descripcion
        self.completada = "No completada"  
        self.tareas[self.titulo] = {
            "Description" : self.descripcion,
            "Estado" : self.completada
        }
        self.guardar_tareas()  # Guarda automáticamente después de añadir

    def eliminar_tarea(self):
        self.delete.capitalize() = input("Introduzca la tarea que quiere borrar: ")
        if self.delete in self.tareas:
            self.tareas.pop(self.delete)
            print(f"Tarea {self.delete} eliminada correctamente")
        else:
            print(f"La tarea {self.delete} no existe")
    
    def marcar_como_completada(self):
        self.marcar = input("Introduzca la tarea que quiere marcar como completada: ")
        if self.marcar in self.tareas:
            self.tareas[self.marcar]['Estado'] = "Tarea completada"
            print(f"Tarea {self.marcar} marcada como completada")
        else:
            print(f"La tarea {self.marcar} no existe")

    def listar_tareas(self):
        try:
            if self.tareas:
                for clave, valor in self.tareas.items():
                    print(f"El nombre de la tarea es: {clave}")
                    print(f"Su descripcion es: {valor['Description']}")
                    print(f"Se encuentra en: {valor['Estado']}")
                else:
                    print("No hay tareas registradas")
        except AttributeError:
            print(f"Primero haga las modificaciones")
            menu()
        
        except KeyError:
            print("no se ha encontrado esa tarea, pruebe de nuevo")
            menu()

    def guardar_tareas(self):#Guarda las tareas en un archivo JSON.
        with open(self.archivo, "w") as f:
            json.dump(self.tareas, f, indent=4)
            return f"Tareas guardadas correctamente"
    
def menu():
    while True:
        print("\n_________Menú________\n")
        print("1. Añadir tarea")
        print("2. Eliminar tarea")
        print("3. Marcar tarea como completada")
        print("4. Listar tarea")
        print("0. Salir")
        opcion = input("Introduzca la opcion elegida: ")
        if opcion == "1":
            tarea1.anadir_tarea()
        if opcion == "2":
            tarea1.eliminar_tarea()
        if opcion == "3":
            tarea1.marcar_como_completada()
        if opcion == "4":
            tarea1.listar_tareas()
        if opcion == "0":
            print("Saliendo del programa...")
            tarea1.guardar_tareas()
            break

tarea1 = Tarea()
menu()
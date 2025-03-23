import random
'''
Ejercicio 9: Promedio de notas
Crea una clase Notas con una lista de calificaciones como atributo.
Implementa un método que calcule el promedio y otro que devuelva la nota más alta. Añade manejo de excepciones para evitar notas inferiores a 0 o superiores a 10.
'''

class Notas:

    def __init__(self):
        self.lista_notas = []

    def asignar_notas(self):
        for _ in range(20):
            self.lista_notas.append(round(random.uniform(0, 10),2) )
        print(f"Estas son las notas obtenidas: {self.lista_notas}")

    def promedio(self):
        media = sum(self.lista_notas) / len(self.lista_notas)
        print(f"Esta es la media de las notas: {round(media,2)}")

    def nota_mas_alta(self):
        self.lista_ordenada = sorted(self.lista_notas) 
        print(f"La nota mas alta es: {self.lista_ordenada[-1]}")
        


promedio1 = Notas()
promedio1.asignar_notas()
promedio1.promedio()
promedio1.nota_mas_alta()


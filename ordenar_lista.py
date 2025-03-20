import random
'''
Ejercicio 6: Ordenar una lista
Escribe una función que reciba una lista de números y la ordene de menor a mayor sin usar sort().
Luego, intégrala como método en una clase Ordenador.
'''

class Ordenador:
    
    def __init__(self):
        self.lista = [68, 12, 32, 47, 52, 100, 54, 61, 63, 21, 77, 82, 44, 98]
       
        
    def ordenar_lista(self):
        for recorrido in range(1,len(self.lista)):
            for puesto in range(len(self.lista) - recorrido):
                if self.lista[puesto] > self.lista[puesto + 1]:
                    temp = self.lista[puesto]
                    self.lista[puesto] = self.lista[puesto + 1]
                    self.lista[puesto + 1] = temp

    def mostrar_lista(self):
        print(self.lista)
                
                
orden1 = Ordenador()            

orden1.ordenar_lista()

orden1.mostrar_lista()

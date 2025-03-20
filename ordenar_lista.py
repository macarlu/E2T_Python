import random
'''
Ejercicio 6: Ordenar una lista
Escribe una función que reciba una lista de números y la ordene de menor a mayor sin usar sort().
Luego, intégrala como método en una clase Ordenador.
'''

class Ordenador:
    
    def __init__(self):
        self.lista = [68, 12, 32, 47, 52, 100, 54, 61, 63, 21, 77, 82, 44, 98]
        self.lista_ordenada = []
        
    def ordenar_lista(self):
        for i in self.lista:
            if i > i - 1:
                
                
orden1 = Ordenador()    

orden1.ordenar_lista()

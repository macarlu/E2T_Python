import random
'''
Ejercicio 3: Lista de números pares
Crea una clase Numeros con un atributo que sea una lista de enteros.
Incluye un método que devuelva solo los números pares de esa lista.
'''


class Numeros:
    lista = [12,15,21,26,29,34,37,41,43,46,58,62,74,79,86]
    def __init__(self):
       pass
        
    def pares(self):
       
        for n in self.lista:
            if n % 2 == 0:
                print(n)
       
numero_par = Numeros()

numero_par.pares()
    
    
   
import random

'''Ejercicio 14: Juego de adivinanza
Crea una clase Adivinanza que genere un número aleatorio entre 1 y 100 (usa random).
Incluye un método que permita al usuario adivinar y devuelva pistas ("más alto" o "más bajo") hasta que 
acierte.'''

class Adivinanza:
    
    def __init__(self):
        self.numero = 0
        self.generar_numero()
    
    def generar_numero(self):
        self.numero = random.randint(1, 100)
                
    def generar_pista(self):
        
            if self.num > self.numero:
                print("más bajo...")
                self.probar_suerte()
            elif self.num < self.numero:
                print("más alto...")
                self.probar_suerte()
            elif self.num == self.numero:
                print("¡¡Bien, has acertado el número secreto!!")
                
    def probar_suerte(self):
        try:
            self.num = int(input("Introduce tu número: "))
            self.generar_pista()
        except ValueError:
            print("¡Debes introducir numeros")
        
intento1 = Adivinanza()       
intento1.probar_suerte()        
            
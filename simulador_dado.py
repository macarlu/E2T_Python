import random
'''
Ejercicio 10: Simulador de dado
Escribe una clase Dado que simule tirar un dado de 6 caras (usando random).
Incluye un método para tirar el dado y otro para mostrar el resultado.
EXTRA: Añade un selector de tipos de dados (d2, d4, d6, d8, d10, d12, d20)
'''
class Dado:
    
    tirada = []
    
    def ___init__(self):
        pass
    
    def tirar_dado(self):
        n = 0
        n += 1
        while n < self.tipo_tirada:
            self.puntuacion = random.randint(1,6)
            self.tirada.append(self.puntuacion)
            
            print(self.tirada)
            
    
    def mostrar_resultado(self):
        
        resultado = 0
        for num in self.tirada:
            resutado += num
            
            print(f"El valor obtenido ha sido de: {resultado}")
        
            
    def selector_dados(self):
        self.tipo_tirada = int(input("Elige el número de dados a tirar 2, 4, 6, 8, 10, 12, 20: "))
        dado1.tirar_dado()
    
dado1 = Dado()
dado1.selector_dados()
dado1.mostrar_resultado()
        
    
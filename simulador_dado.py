import random
'''
Ejercicio 10: Simulador de dado
Escribe una clase Dado que simule tirar un dado de 6 caras (usando random).
Incluye un método para tirar el dado y otro para mostrar el resultado.
EXTRA: Añade un selector de tipos de dados (d2, d4, d6, d8, d10, d12, d20)
'''
class Dado:
    
    ronda=[]
    def ___init__(self):
        pass

    def tirar_dado(self):

        while self.tipo > 0:
            self.tipo -= 1
            self.puntuacion = random.randint(1,6)
            self.ronda.append(self.puntuacion)
        print(self.ronda)
            
    def mostrar_resultado(self):
        
        print(f"El valor obtenido ha sido de: {sum(self.ronda)}")
        
            
    def selector_dados(self):

        try:
            self.tipo = int(input("Elige el número de dados a tirar 2, 4, 6, 8, 10, 12, 20: "))
            dado1.tirar_dado()
        except ValueError:
            print("Debe introducir un número entero")
            dado1.selector_dados()
            if self.tipo > 20 or self.tipo < 2:
                print("El número introducido no está entre los números dados.")
                dado1.selector_dados()

    
dado1 = Dado()
dado1.selector_dados()
dado1.mostrar_resultado()
        
    
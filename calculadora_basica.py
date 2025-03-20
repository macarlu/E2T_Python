"""
Ejercicio1. Calculadora básica con clases
Crea una clase Calculadora que tenga métodos para sumar, restar, multiplicar y dividir dos números
Incluye un constructor que inicialice los dos números como atributos.
"""
    
class Calculadora:
   
    def __init__(self, = None, b = None):
        pass
        self.a = a
        self.b = b
        
    def suma(self):
        return (self.a + self.b)
        
    def resta(self):
        return (self.a - self.b)
    
    def multiplicacion(self):
        return round((self.a * self.b),2)
    
    def division(self):
        return round((self.a / self.b),2)

calculo1 = Calculadora()   

'''def calcular():

    operacion = input("Introduce la operacion a realizar: ")

    if operacion == "suma":
        print(calculo1.suma())
    elif operacion == "resta":
        print(calculo1.resta())
    elif operacion == "multiplicacion":
        print(calculo1.multiplicacion())
    elif operacion == "division":
        print(calculo1.division())

 
       
calcular()'''

if __name__ == "__main__":
    Calculadora()
    #calcular()
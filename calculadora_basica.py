"""
Calculadora básica con clases
Crea una clase Calculadora que tenga métodos para sumar, restar, multiplicar y dividir dos números
Incluye un constructor que inicialice los dos números como atributos.
"""
    
class Calculadora:
    
    def __init__(self):
        self.a = float(input("Intoduce el primer número: "))
        self.b = float(input("Intoduce el segundo número: "))
        
    def suma(self):
        return (self.a + self.b)
        
    def resta(self):
        return(self.a - self.b)
    
    def multiplicacion(self):
        return(self.a * self.b)
    
    def division(self):
        return(self.a / self.b)

calculo1 = Calculadora()

def calcular():
    
    operacion = input("Introduce la operacion a realizar: ")
    
    if operacion == "suma":
        print(calculo1.suma())
    elif operacion == "resta":
        print(calculo1.resta())
    elif operacion == "multiplicacion":
        print(calculo1.multiplicacion())
    elif operacion == "division":
        print(calculo1.division())
       
calcular()

if __name__ == "__main__":
    calcular()
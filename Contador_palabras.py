'''
Ejercicio 2: Contador de palabras
Escribe una función que reciba una cadena de texto y devuelva cuántas palabras contiene.
Luego, crea una clase Texto que use esa función como método y almacene el texto como atributo.
'''

class Texto:

    def __init__(self):
        pass
        
    def cuentapalabras(self, palabra = None):
        self.palabra = palabra
        palabra = input("Introduce la palabra o frase a contar: ")
        numero_palabra = len(palabra.split())
        print(numero_palabra)

def contar():
    palabra1.cuentapalabras()

palabra1 = Texto()

contar()



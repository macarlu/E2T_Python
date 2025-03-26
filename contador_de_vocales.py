'''
Ejercicio 12: Contador de vocales
Diseña una clase AnalizadorTexto con un atributo para una cadena de texto.
Implementa un método que cuente cuántas vocales (a, e, i, o, u) hay en el texto.
'''
class AnalizadorTexto:
    
    def __init__(self):
        pass
    
    def separapalabras(self, texto):
        self.texto = input("Introduce el texto donde se quiere buscar: ")
        self.separador_palabras = texto.split()
        
    def separaletras(self):
        self.separador_letras = self.separador_palabras.split()
        
        
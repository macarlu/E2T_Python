'''
Ejercicio 12: Contador de vocales
Diseña una clase AnalizadorTexto con un atributo para una cadena de texto.
Implementa un método que cuente cuántas vocales (a, e, i, o, u) hay en el texto.
'''
class AnalizadorTexto:
    
    def __init__(self):
        self.vocales_encontradas = []
    
    def contar_vocales(self):
        self.texto = input("Introduce el texto donde se quiere buscar: ")
        self.vocales = ("A", "a", "E", "e", "I", "i", "O", "o", "U", "u")
        for vocal in self.texto:
            if vocal == "A" or vocal == "a":
                self.vocales_encontradas.append(vocal)
                       
            elif vocal == "E" or vocal == "e":
                self.vocales_encontradas.append(vocal)
                        
            elif vocal == "I" or vocal =="i":
                self.vocales_encontradas.append(vocal)
                
            elif vocal == "O" or vocal == "o":
                self.vocales_encontradas.append(vocal)
                
            elif vocal == "U" or vocal == "u":
                self.vocales_encontradas.append(vocal)
                            
    def mostrar_resultado(self):
        self.contar_vocales()
        resultado = len(self.vocales_encontradas)
        print(self.vocales_encontradas)
        print(f"El total de vocales encontradas es de: {resultado}")
            
texto1 = AnalizadorTexto()
texto1.mostrar_resultado()
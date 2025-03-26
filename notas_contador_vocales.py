separador_palabras = ""
def separapalabras():
    texto = input("Introduce el texto donde se quiere buscar: ")
    separador_palabras = texto.split()
    return separador_palabras
    
    
def separaletras():
    separador_letras = separador_palabras.split()
    print(separador_letras)
        
separapalabras()
separaletras()
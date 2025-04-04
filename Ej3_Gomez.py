'''Crea una aplicación que calcule el Índice de Masa Corporal (IMC) de una persona.

La aplicación debe pedir al usuario su peso en kilogramos y su altura en metros, y luego calcular el IMC usando la fórmula: IMC=PESOALTURA2

Debe mostrar el IMC con dos decimales.'''

def imc():
    
    try:
    
        peso = float(input("Introduzca su peso en kilogramos: "))
    
        altura = float(input("Introduzca su altura en metros: "))
    
        resultado = round(peso / altura ** 2,2)
    
        print(f"Su IMC es de {resultado}")
        
    except ValueError:
        print("Debe introducir solo números")
imc()
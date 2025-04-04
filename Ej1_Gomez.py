'''Crea una aplicación que calcule el impuesto sobre la renta de una persona. La aplicación debe pedir al usuario su ingreso anual y calcular el impuesto basado en las siguientes tasas:

Hasta 10,000€: 10%
De 10,001€ a 20,000€: 15%
De 20,001€ a 30,000€: 20%
Más de 30,000€: 25%
La aplicación puede manejar excepciones para validar la entrada del usuario.

Debe mostrar el impuesto total a pagar.'''

def impuestos():
    
    try:
        
        ingreso = float(input("Introduzca el total de ingresos: "))

        if ingreso < 10000:
            impuesto =  round((10 * ingreso) / 100,2)
            print(f"El impuesto que debe pagar es de: {impuesto}€")

        elif 10000 < ingreso < 20000:
            impuesto =  round((15 * ingreso) / 100,2)
            print(f"El impuesto que debe pagar es de: {impuesto}€")

        elif 20000 < ingreso < 30000:
            impuesto =  round((20 * ingreso) / 100,2)
            print(f"El impuesto que debe pagar es de: {impuesto}€")

        else:
            impuesto =  (25 * ingreso) / 100
            print(f"El impuesto que debe pagar es de: {impuesto}€")
            
    except ValueError:
        print("Debe introducir números")
        impuestos()
        
impuestos()
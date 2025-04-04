import random
import sys
'''
Tenemos una empresa de gestión de residuos, que cobra por metro cúbico de basura.
Los precios cobrados son los siguientes:
Madera: 10€ m3
Plástico: 20€ m3
Hospitalarios: 40€ m3
Otros: 30€ m3
Además, el transporte cobrará a razón de 1€ por kilómetro recorrido al ir a buscar los desechos, y 1€ por m3 y kilómetro recorrido a la vuelta.
Realice una aplicación, que pregunte la cantidad de desechos de cada tipo a recoger, además de los Kilómetros y genere un presupuesto.
'''

class EmpresaResiduos:
    
    def __init__(self):
        self.madera = 10
        self.plastico = 20
        self.hospitalario = 40
        self.otros = 30
        self.desechos = float()
        self.distancia = int()
    
    def calcular_cantidad(self):
        self.desechos = float(input("Introduzca la cantidad en m3 de desechos aprox. a recoger : "))
        return self.desechos
        
    def calcular_distancia(self):
        self.distancia = random.randint(1,50)
        print(f"La distancia a recorrer es de {self.distancia} Kilometros")
        return self.distancia
            
    def generar_presupuesto(self):
        if not hasattr(self, "opcion"):  # Asegurar que la opción esté definida
            print("Primero seleccione un tipo de residuo antes de calcular el presupuesto.")
            return
        
        precios = {
            "1": self.madera,
            "2": self.plastico,
            "3": self.hospitalario,
            "4": self.otros
        }
        
        if self.opcion in precios:
            costo_residuos = self.desechos * precios[self.opcion]
            costo_transporte = self.distancia + (self.distancia * self.desechos)
            presupuesto = costo_residuos + costo_transporte
            print(f"La recogida asciende a un montante de: {presupuesto}€")
        else:
            print("Opción inválida. Seleccione un tipo de residuo primero.")
        
    def menu(self):
        while True:
            print("\n***************************\n**EMPRESA DE RESIDUOS S.A**\n***************************\n")
            print("Rellene los datos del Material a Recoger:\n-----------------------------------------")
            print("1. Recogida de Madera")
            print("2. Recogida de Plastico")
            print("3. Recogida de Desechos Hospitalarios")
            print("4. Recogida de Otros Residuos")
            print("5. Distancia a Recorrer")
            print("6. Generar Presupuesto")
            print("0. Salir del Programa\n")
            self.opcion = input("Seleccione una opción: ")

            if self.opcion in ["1","2","3","4"]:
                self.calcular_cantidad()
            elif self.opcion == "5":
                self.calcular_distancia()
            elif self.opcion == "6":
                self.generar_presupuesto()
            elif self.opcion == "0":
                print("Saliendo del programa...")
                sys.exit()
                   
recogida1 = EmpresaResiduos()               
recogida1.menu()
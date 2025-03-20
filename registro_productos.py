'''
Ejercicio 7: Registro de productos
Crea una clase Producto con atributos para nombre, precio y cantidad en stock.
Añade un método que calcule el valor total del inventario (precio × cantidad).
'''

class Producto:

    def __init__(self):
        self.nombre = "camisolas"
        self.precio = 44.99
        self.cantidad = 1250

    def inventario(self):
        self.total = round((self.precio * self.cantidad),2)
        print(f"El valor total de inventario de {self.nombre} es de {self.total} €.")

calculo_producto1 = Producto()

calculo_producto1.inventario()



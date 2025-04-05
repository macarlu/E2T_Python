class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre # default public, se pueden modificar
        self._categoria = categoria #protected, también se pueden modificar, pero solo en la clase
        self.__precio = precio # private, no se puede modificar en el código

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Categoría: {self._categoria}, Precio: {self.__precio}€")

# GETTERS y SETTERS - GET = obtiene un valor, SET = agrega un valor

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

restaurant = Restaurant("Pizzeria Mexico", "Comida Italiana", 50)
#restaurant.__precio = 80 #no será posible modificarlo con Private __
restaurant.mostrar_informacion()
restaurant.set_precio(80)
precio = restaurant.get_precio()
print(precio)

restaurant2 = Restaurant("Hamburguesas Python", "Comida casual", 20)
restaurant2.mostrar_informacion()
restaurant2.set_precio(40)
precio = restaurant2.get_precio()
print(precio)

# Crear una claswe hijo de Restaurant
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio):
        super().__init__(nombre, categoria, precio)
hotel = Hotel("Hotel POO", "5 estrellas", 200)
hotel.mostrar_informacion()
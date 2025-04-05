class Restaurant:

    def agregar_restaurant(self, nombre): # Metodo
        self.nombre = nombre # Atributo de la clase (da forma a los datos)

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")


# Instanciar la clase (llamarla)
restaurant = Restaurant()
restaurant.agregar_restaurant("Pizzeria Mexico")
restaurant.mostrar_informacion()

restaurant2 = Restaurant()
restaurant2.agregar_restaurant("Hamburguesas Python")
restaurant2.mostrar_informacion()

# Mostrar la informacion
print(f"Nombre Restaurant: {restaurant.nombre}")
print(f"Nombre Restaurant: {restaurant2.nombre}")
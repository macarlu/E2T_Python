class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, new_nombre):
        self._new_nombre = new_nombre

dalto = Persona("Lucas", 21)
nombre = dalto.get_nombre()


print(nombre)


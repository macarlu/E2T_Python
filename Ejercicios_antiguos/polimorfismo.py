class Gato():
    def sonido(self):
        return "Miau"

class Perro():
    def sonido(self):
        return "Guau"

def hacer_sonido(animal):
    print(animal.sonido())

gato = Gato()
perro = Perro()

hacer_sonido(gato)#El mismo metodo funciona diferente para distintos argumentos

print(perro.sonido())#El mismo metodo funciona diferente para distintos objetos


def recorrer(elemento):
    for item in elemento:
        print(f"El elemento actual es: {item}")

lista1 =  [1,2,3,4,5]
lista2 = ["maquina","como","andas"]
lista3 = "estomago"

recorrer(lista3)

#echarle un ojo a:
# DUCK TYPING
#ENLACES DINAMICOS
#ENLACES ESTATICOS
#TIPO REAL
#TIPO DECLARADO

# Escribe tu código aquí :-)
def calificaciones():
    lista_notas = []
    entrada_notas = input("Ingrese las nota obtenida: ")
    pregunta = input("¿Desea añadir otra nota? ")
    lista_notas.append(entrada_notas)

    while True:
        if pregunta == "s" or pregunta == "S":
            entrada_notas = input("Ingrese las nota obtenida: ")
            pregunta = input("¿Desea añadir otra nota? ")
            lista_notas.append(entrada_notas)
        else:
            break

    lista_inicial = sorted(lista_notas)
    lista_inicial.pop(0)

    for i in range(lista_inicial):
        lista_final.append(float(lista_inicial)

    nota_final = sum(lista_final) / len(lista_final)

    print(nota_final)

calificaciones()

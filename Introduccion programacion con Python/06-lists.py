# las listas son como los arrays de otros lenguajes
lenguajes =["Python", "Kotlin", "Java", "Javascript"]
print(lenguajes)

# las listas comienzan en la posición 0
print(lenguajes[0])
print(lenguajes[1])
print(lenguajes[2])
print(lenguajes[3])

# existen una serie de métodos para trabajar con listas

#ordenar listas
lenguajes.sort()# los ordena por orden alfabetico
print(lenguajes)

# acceder a un elemento dentro de un texto
aprendiendo = f"Estoy aprendiendo {lenguajes[3]}"
print(aprendiendo)

# modificando valores dentro de una listas
lenguajes[2] = "PHP"
print(lenguajes)

# agregar elementos a una lista
lenguajes.append("Ruby")
print(lenguajes)

# eliminar elementos de una lista
del lenguajes[1]# por posición
print(lenguajes)

lenguajes.pop()# elimina el ultimo elemento
print(lenguajes)

lenguajes.pop(0)# elimina el elemento pasado como parametro
print(lenguajes)

lenguajes.remove("PHP")# elimina por nombre
print(lenguajes)
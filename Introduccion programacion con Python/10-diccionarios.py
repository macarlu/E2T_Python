# Creando un diccionario simple

cancion = {
    "artista" : "Metallica", # llave (key) y valor
    "cancion" : "Enter Sandman",
    "lanzamiento" : 1992,
    "likes" : 3000
}
print(cancion)

# Acceder a los elementos de los diccionarios
print(cancion["artista"])
print(cancion["lanzamiento"])

# Mezclar con un string
artista = {cancion["artista"]}
print(f"Estoy escuchando a {artista}")
print(cancion)

# Agregar nuevos valores
cancion["playlist"] = "Heavy Metal"
print(cancion)

# Reemplazar valor existente
cancion["cancion"] = "Seek & Destroy"
print(cancion)

# Eliminar un valor
del cancion["lanzamiento"]
print(cancion)
print("----------------------------------------------------------------------------------------------")

# Iniciar un diccionario vacio
jugador = {}
print(jugador)

# Se une un jugador
jugador["nombre"] = "Juanma"
jugador["puntaje"] = "0"
print(jugador)

# Incrementando el puntaje
jugador["puntaje"] = "100"
print(jugador)

# Acceder a un valor
print(jugador.get("consola"))
print(jugador.get("consola", "No existe ese valor"))

# Iterar en el diccionario
for llave, valor in jugador.items():
    print(llave)
    print(valor)

# Eliminar jugador y puntaje
del jugador["nombre"]
del jugador["puntaje"]
print(jugador)
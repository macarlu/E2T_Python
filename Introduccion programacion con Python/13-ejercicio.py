playlist = {} # Diccionario vacio
playlist["canciones"] = [] # lista vacia de canciones
# ponemos las variables fuera de la funcion porque va aser llamada desde varios sitios
# función principal
def app():
    # Agregar_playlist, es como si fuera la bandera de salida del código

    agregar_playlist = True

    while agregar_playlist:
        nombre_playlist = input("¿Cómo deseas llamar a tu playlist?\r\n")
        if nombre_playlist:
            playlist["nombre"] = nombre_playlist
            # Si ya tenemos un nombre desactivar el True
            agregar_playlist = False

            # Mandar llamar a la función agregar_canciones
            agregar_canciones()

def agregar_canciones():
    #bandera para agregar canciones
    agregar_cancion = True
    while agregar_cancion:
        #preguntar al usuario que canción desea agregar
        nombre_playlist = playlist["nombre"]
        pregunta = f"\r\nAgrega canciones para la playlist {nombre_playlist}:\r\n"
        pregunta += "Escribe 'x' para dejar de agregar canciones\r\n"

        cancion = input(pregunta)

        if cancion == "x":
            # Dejar de agregar canciones
            agregar_cancion = False
            # Mostrar resumen de la playlist
            mostrar_resumen()
        else:
            # Agregar canciones a la playlist
            playlist["canciones"].append(cancion)

def mostrar_resumen():
    nombre_playlist = playlist["nombre"]
    print(f"Playlist: {nombre_playlist}\r\n")
    print("Canciones : ")
    for cancion in playlist["canciones"]:
        print(cancion)

app()

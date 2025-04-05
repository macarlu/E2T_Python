def app():
    # Crear el archivo
    archivo = open("archivo.txt", "w") # w es escritura, si no existe lo crea

    # Generar números en archivo
    for i in range(0, 20):
        archivo.write("Esta linea " + str(i) + "\r\n")

    # Cerrar el archivo
    archivo.close()


app()
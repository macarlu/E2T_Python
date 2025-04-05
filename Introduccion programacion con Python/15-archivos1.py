def app():

    with open("archivo.txt") as archivo:# con with open no hace falta cerrar el archivo
        for contenido in archivo:
            print(contenido.rstrip())# rstrip elimina los espacios entre lineas







app()
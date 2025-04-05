import os

CARPETA = "contactos/" # carpeta de contactos
EXTENSION = ".txt"

# contactos
class Contacto:
    def __init__(self, nombre, telefono, categoria):

        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    # revisa si la carpeta existe o no
    crear_directorio()

    # muestra el menú de opciones
    mostrar_menu()

    # preguntar al usuario la acción a realizar
    preguntar = True
    while preguntar:
        opcion = int(input("Seleccione una opción: \r\n"))

        # ejecutando las opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print("Opción no válida, intentelo de nuevo")

def eliminar_contacto():
    nombre = input("\r\nSeleccion el nombre del contacto que desea eliminar: \r\n")
    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print("\r\nEliminado Correctamente")
    except NameError:
        print("No existe ese contacto")

    # reiniciando la app
    app()

def buscar_contacto():
    nombre = input("Seleccion el nombre del contacto que desea buscar: \r\n")

    # intentamos abrir el archivo
    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print("\r\nInformación del contacto: \r\n")
            for linea in contacto:
                print(linea.rstrip())
            print("\r\n")

    # si por lo que nos da un error se ejecuta
    except IOError:
        print("El archivo no existe")
        print(IOError)
        print("\r\n")

    # reiniciando la app
    app()

def mostrar_contactos():
    archivos = os.listdir(CARPETA) # listamos la carpeta de contactos

    # para asegurarnos de mostrar los .ext
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    # recorremos la carpeta
    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                # imprime los contenidos
                print(linea.rstrip())
            # imprime el separador entre contactos
            print("\r\n")

def editar_contacto():
    print("Escribe el nombre del contacto a editar")
    nombre_anterior = input("Nombre del contacto que desea editar: \r\n")

    # revisando si el contacto ya existe antes de editarlo
    existe = existe_contacto(nombre_anterior)

    if existe:# abrimos el archivo y volvemos a reescribir los datos de los campos
        with open(CARPETA + nombre_anterior + EXTENSION, "w") as archivo:
            nombre_contacto = input("Agrega el nuevo nombre del Contacto: \r\n")
            telefono_contacto = input("Agrega el nuevo número de teléfono del Contacto: \r\n")
            categoria_contacto = input("Agrega la nueva categoría del Contacto: \r\n")

            #instanciamos la clase

            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            # escribimos en el archivo
            archivo.write("Nombre: " + contacto.nombre + "\r\n")
            archivo.write("Teléfono: " + contacto.telefono + "\r\n")
            archivo.write("Categoría: " + contacto.categoria + "\r\n")

            # renombramos el archivo
            os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

            # mostrando un msg de éxito
            print("\r\nContacto editado correctamente \r\n")

    else:
        print("Ese contacto no existe")

    # reiniciando la app
    app()

def agregar_contacto():
    print("Escribe los datos para agregar el nuevo Contacto")
    nombre_contacto = input("Nombre del Contacto: \r\n")

    # revisando si el contacto ya existe antes de crearlo
    existe = existe_contacto(nombre_contacto)

    if not existe:

        with open(CARPETA + nombre_contacto + EXTENSION, "w") as archivo:

        # añadiendo resto de campos
            telefono_contacto = input("Número de teléfono del Contacto: \r\n")
            categoria_contacto = input("Categoría del Contacto: \r\n")

        # instanciamos la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

        # escribiendo en el archivo
            archivo.write("Nombre: " + contacto.nombre + "\r\n")
            archivo.write("Teléfono: " + contacto.telefono + "\r\n")
            archivo.write("Categoría: " + contacto.categoria + "\r\n")

        # mostrando un msg de éxito
            print("\r\nContacto creado correctamente \r\n")
    else:
        print("Ese contacto ya existe \r\n")

    # reiniciando la app
    app()


def mostrar_menu():
    print("Seleccione del Menú lo que desea hacer")
    print("1) Agregar un nuevo Contacto")
    print("2) Editar Contacto")
    print("3) Ver Contactos")
    print("4) Buscar Contacto")
    print("5) Eliminar Contacto")

def crear_directorio():

    if not os.path.exists(CARPETA):
        # creando la carpeta
        os.makedirs(CARPETA)

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)


app()
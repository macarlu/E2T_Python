# funciones

def informacion():
    print("Soy Juan")

informacion()
informacion()
informacion()

#funciones mas inteligentes

# estos son lo parametros, y este es llamado parametros por default, y se aplica cuando no esta el argumento.

def informacion_con_parametros(nombre, puesto = "desconocido"):
    print(f"Soy {nombre} y soy {puesto}")#Cuando se mezclan cadenas con parametros hay que usar la 'f' al principio.

# estos son los argumentos
informacion_con_parametros("Pedro", "Programador")
informacion_con_parametros("Itzel", "Diseñadora")
informacion_con_parametros("Juanma")

# funciones que retornan un valor

def informacion_retorna_valor(nombre):
    return nombre

empleado = informacion_retorna_valor("Juanma")
print(empleado)

# funciones y metodos

nombre1 = "Pedro"

def mostrar_nombre(nombre1):
    print(f"Hola {nombre1}")

mostrar_nombre(nombre1)

# aplicando metodos
print(nombre1.upper())
print(nombre1.lower())

# Reto

def bienvenida(nombres,actividad):
    print(f"Bienvenido {nombres} a esta tu comunidad, donde podrás {actividad}")

bienvenida("Paco", "programar")


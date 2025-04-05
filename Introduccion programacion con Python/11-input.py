nombre = input("¿Cual es tu nombre?: \n")

print(f"Hola {nombre}")

# Leer datos que serán números
# todas las entradas de datos las entiende como string
edad = input("¿Cual es tu edad? ")

# convertir edad a entero

edad = int(edad)  # esto se podria poner en la misma linea delante de input

if edad >= 18:
    print("Ya puedes votar")
else:
    print("Aún no puedes votar")

def examen():
    respuestas = {
    "respuesta1" : "dos",
    "respuesta2" : "dos",
    "respuesta3" : "Hoya fria"
                }
    calificacion = 0

    print("pregunta1 \n¿Con cuantos satélites trabajamos en el SCTM?")
    respuesta1 = input()
    print("pregunta 2 \n¿Cuantas estaciones de anclaje existen?")
    respuesta2 = input()
    print("pregunta 3 \n¿Como se llama la estación de emergencia?")
    respuesta3 = input()

    for clave, valor in respuestas.items():

        if respuesta1 == "dos":
            print("respuesta correcta")
            calificacion += 1
        elif respuesta2 == "dos":
            print("respuesta correcta")
            calificacion += 1
        elif respuesta3 == "Hoya fria":
            print("respuesta correcta")
            calificacion += 1
        else:
            print("respuesta incorrecta")



    print(calificacion)

examen()

pregunta = "Agrega un numero y te diré si es par o impar\r\n"
pregunta += "(Escribe 'cerrar' para salir de la aplicación)\r\n"
preguntar = True

while preguntar:

    numero = input(pregunta)

    if numero == "cerrar":
        preguntar = False
    else:
        numero = int(numero)

        if numero % 2 == 0:
            print(f"El número {numero} es par")
        else:
            print(f"El número {numero} es impar")



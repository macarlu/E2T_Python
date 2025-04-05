# Revisa si una condición es mayor a >
# Revisa si una condición es menor a <
# Revisa si una condición es igual a ==
# Revisa si una condición es distinto a !=
# Revisa si una condición es mayor o igual a >=
# Revisa si una condición es menor o igual a <=

balance = 4500

if balance > 0:
    print("Puedes pagar")
else:
    print("No tienes saldo")


# Likes

likes = 200

if likes == 200:
    print("Excelente, 200 Likes")
else:
    print("Casi llegas a los 200")

# if con texto

lenguaje = "Python"

if lenguaje == "Python":
    print("Excelente decisión")

if not lenguaje == "PHP":# aquí la condición la niega if not
    print("Me alegro")

# Evaluar un Boolean

usuario_autenticado = True

if usuario_autenticado == True:# en booleans podemos poner if usuario_autenticado: se supone el True
    print("Acceso al sistema")
else:
    print("Debes iniciar sesión")

# Evaluar un elemento de una lista

lenguajes =["Python", "Kotlin", "Java", "Javascript", "PHP", "Ruby", "Go"]

if "Cobol" in lenguajes:
    print("Cobol si existe")
else:
    print("No, Cobol no esta en la lista")

# if anidados

usuario_autenticado = True
usuario_admin = True

if usuario_autenticado:

    if usuario_admin:
        print("ACCESO TOTAL")
    else:
        print("Acceso al sistema")
else:
    print("Debes iniciar sesión")

# Ejemplo con elif
# Se usa cuando necesitamos decidir sobre varias condiciones

ocupacion = "Jardinero"

if ocupacion == "Estudiante":
    print("Tienes un 50% de Descuento")
elif ocupacion == "Jubilado":
    print("Tienes un 75% de Descuento")
elif ocupacion == "Desempleado":
    print("Tienes un 10% de Descuento")
else:
    print("Tienes que pagar la entrada completa")

# Operadores and y or
# and revisa que las dos condiciones sean verdaderas
# or en cambio con que un sea verdadera le vale

usuario_logueado = True
usuario_admin = False

if usuario_logueado and usuario_admin:
    print("Administrador")
elif usuario_logueado:
    print("Acceso al sistema")
else:
    print("Debes iniciar sesión")
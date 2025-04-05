lenguajes =["Python", "Kotlin", "Java", "Javascript", "PHP", "Ruby", "Go"]
lenguajes.sort()

# iterador

for lenguaje in lenguajes:
    print(lenguaje)
    print(f"Estoy aprendiendo {lenguaje}")

# al correr los dos print observamos como va recorriendo a la vez la lista

# for que escriba números
for numero in range(0, 20, 3):# los parametros son desde donde empieza a contar, hasta donde y el incremento en la cuenta.
    print(numero)
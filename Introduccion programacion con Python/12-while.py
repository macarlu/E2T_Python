numero = 0
'''
while numero <= 10:
    print(numero)
    numero +=1 # Para evitar un loop infinito
'''
# if dentro del while

while numero <= 10:
    if numero == 5:
        print("¡¡¡Cincoooo!!!")
        # si en vez de esto pusieramos un 'break' finalizaría el loop
        # si pusieramos 'continue' lo saltaría
        # si pusieramos 'pass' haría que ignorase la condición, ejecutando el código normalmente
    else:
        print(numero)
    numero +=1
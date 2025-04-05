def reverso(n):
    reverso = 0 #inicializamos la variable
    num = n #Le asignamos un valor
    while num != 0:#añadimos la condicion al bucle mientras el num no sea 0
        cifra = num % 10#creamos una variable donde asignar el resto de
        #dividir num entre 10
        reverso = reverso * 10 + cifra
        num = num // 10
    return print(reverso)

reverso(2398976534)
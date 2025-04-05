
def TMB():

    peso = float(input("Introduce tu peso en kilogramos: "))
    altura = float(input("Introduce tu altura en centímetros: "))
    edad = int(input("Introduce tu edad: "))
    genero = input("Introduce tu género entre masculino o femenino: ")
    hombre = "masculino"
    mujer = "femenino"
    resultado = 0

    tmb_hombres = (10 * peso) + (6.25 * altura) - (5 * edad) + 5
    tmb_mujeres = (10 * peso) + (6.25 * altura) - (5 * edad) - 161

    resultado = tmb_hombres
    resultado = tmb_mujeres

    if genero == hombre:
        print("tu Tasa Metabólica es: ", tmb_hombres)
    else:
        print("tu Tasa Metabólica es: ", tmb_mujeres)

    #actividad_fisica = {poco : TMB * 1.2, ligero : TMB * 1.37,moderado : TMB * 1.55, intenso : TMB * 1.73}
    poco = "nada o poco"
    ligero = "dos o tres veces por semana"
    moderado = "cuatro o cinco veces por semana"
    intenso = "seis o siete dias por semana"
    deporte = input("introduce tu activida física entre, poco, ligero, moderado o intenso: ")

    if deporte == poco:
        print(resultado * 1.2)
    elif deporte == ligero:
        print(resultado * 1.37)
    elif deporte == moderado:
        print(resultado * 1.55)
    else:
        print(resultado * 1.73)

    volumen = "Ganancia de músculo"
    definicion = "Perdida de grasa"
    entrenamiento = input("Elige tu tipo de entrenamiento entre volumen o definicion: ")

    if entrenamiento == volumen:
        print("En volumen debes comer:  55 % de hidratos, 25% de proteinas, 20% de grasa.")
    else:
        print("En definición debes comer: 40 % de hidratos, 35% de proteinas, 25% de grasa.")

TMB()
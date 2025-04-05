hora = int(input("Ingresa una hora entre(0...23): "))
minuto = int(input("Ingresa una cifra de minutos entre(0...59): "))
duracion = int(input("Ingresa una cifra de minutos entre: "))

hora_inicio= f"{hora}:{minuto}"
print(hora_inicio)

minuto_fin = minuto + duracion
minuto_final = minuto_fin % 60
hora_fin = hora + (minuto_fin // 60)
hora_final = hora_fin % 24

resultado =f"{hora_final}:{minuto_final}"

print(resultado)
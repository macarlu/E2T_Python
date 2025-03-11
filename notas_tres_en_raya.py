import tabulate as tb
from random import random


#def tres_en_raya():
jugador = "X"
maquina = "O"
tablero = 0
while True:
    movimientos = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
                ]
    tablero = tb.tabulate(movimientos, tablefmt="grid")
    for lista in movimientos:
        arriba_izquierda = movimientos[0,0]
        arriba_centro = movimientos[0,1]
        arriba_derecha = movimientos[0,2]
        centro_izquierda = movimientos[1,0]
        centro_centro = movimientos[1,1]
        centro_derecha = movimientos[1,2]
        abajo_izquierda = movimientos[2,0]
        abajo_centro = movimientos[2,1]
        abajo_derecha = movimientos[2,2]
    print(tablero)
    break

#tres_en_raya()
        
    





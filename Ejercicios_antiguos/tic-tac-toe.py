from random import randrange

def display_board(board):

    print("+-------" * 3, sep = "")

    for row in range(3):
        print("|       " * 3, sep = "")

        for col in range(3):
            print("|  " + str(board[row][col] + " ", end = ""))
        print("|")
        print("|       " * 3, "|", sep = "")
        print("+-------" * 3, "+", sep = "")

def enter_move(board):

    ok = False#suposición falsa, la necesitamos para entrar en el bucle

    while not ok:
        move = input("Ingresa tu movimiento: ")
        #¿es válido lo que ingresóp el usuario?
        ok = len(move) == 1 and move >= "1" and move <= "9"
        if not ok:
            print("Movimiento erróneo, ingrésalo nuevamente")
            continue
        move = int(move) - 1 #número de la celda, del 0 al 8
        row = move // 3 #fila de la celda
        col = move % 3 #columna de la celda
        sign = board[row][col] #marca el cuadro elegido
        ok = sign not in ["O", "X"]
        if not ok: #esta ocupado, ingresa una posición nuevamente
            print("¡Cuadro ocupado, ingresa nuevamente")
            continue
    board[row][col] = "O" #colocar "O" al cuadro seleccionado

def make_list_of_free_fields(board):
    free = []
    for row in range(3): #itera a traves de las filas
        for col in range(3): #itera a traves de las columnas
            if board[row][col] not in ["O", "X"]: #¿está la celda libre?
                #si, agrega una nueva tupla a la lista
                free.append((row,col))
    return free

def victory_for(board,sgn):
    if sgn == "X": #¿estamos buscando X?
        who = "me" #si, es la maquina
    elif sgn == "O": #¿0 estamos buscando O?
        who = "you" #si, es el usuario
    else:
        who = None #¡no debemos de caer aquí!
    cross1 = cross2 = True #para las diagonales
    for rc in range(3):
        #check row rc
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:
            return who
        #check column rc
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:
            return who
        if board[rc][rc] != sgn: #revisar la primera diagonal
            cross1 = False
        if board[2 - rc][2 - rc] != sgn: #revisar la segunda diagonal
            cross2 = False
        if cross1 or cross2:
            return who
        return None
def draw_move(board):
    #crea una lista de los cuadros vacios o libres
    free = make_list_of_free_fields(board)
    cnt = len(free)
    #si la lista no está vacía, elegir un lugar para "X" y colocarla
    if cnt > 0:
        this = randrange(cnt)
        row, col = free[this]
        board[row][col] = "X"
#crear un tablero vacio
board =[[3 * j + i + 1 for i in range(3)] for j in range(3)]
board[1][1] = "X" #colocar la primera "X" en el centro
free = make_list_of_free_fields(board)
human_turn = True #¿de quien es turno ahora?
while len(free):
    display_board(board)
    if human_turn:
        enter_move(board)
        victor = victory_for(board, "O")
    else:
        draw_move(board)
        victor = victory_for(board, "X")
    if victor != None:
        break
    human_turn = not human_turn
    free = make_list_of_free_fields(board)

display_board(board)
if victor == "you":
    print("¡Has ganado!")
elif victor == "me":
    print("¡He ganado!")
else:
    print("¡Empate!")



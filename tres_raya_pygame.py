import pygame
import sys
import random

# Inicialización de pygame
pygame.init()

# Dimensiones de la ventana
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 6
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS

CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 6
CROSS_WIDTH = 6
SPACE = SQUARE_SIZE // 4

# Colores
BG_COLOR = (255, 255, 255)  # Fondo blanco
LINE_COLOR = (50, 50, 50)   # Líneas en gris oscuro
CIRCLE_COLOR = (0, 0, 255)  # Azul para la O
CROSS_COLOR = (255, 0, 0)   # Rojo para la X

# Configurar ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tres en Raya - IA Difícil")
screen.fill(BG_COLOR)

# Estado del tablero: una matriz 3x3 inicializada con None
board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
player = "X"  # El jugador humano comienza

def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == "O":
                center = (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2)
                pygame.draw.circle(screen, CIRCLE_COLOR, center, CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == "X":
                start_desc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE)
                end_desc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)

                start_asc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                end_asc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE)
                pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] is None

def is_board_full():
    return all(board[row][col] is not None for row in range(BOARD_ROWS) for col in range(BOARD_COLS))

def check_win(player):
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def restart():
    global board, player
    board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    player = "X"
    screen.fill(BG_COLOR)
    draw_lines()

def best_move():
    """ IA usa Minimax para encontrar la mejor jugada """
    best_score = -float("inf")
    move = None

    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if available_square(row, col):
                board[row][col] = "O"
                score = minimax(board, 0, False)
                board[row][col] = None
                if score > best_score:
                    best_score = score
                    move = (row, col)
    
    if move:
        mark_square(move[0], move[1], "O")

def minimax(board, depth, is_maximizing):
    """ Algoritmo Minimax para evaluar las jugadas """
    if check_win("X"):
        return -1
    if check_win("O"):
        return 1
    if is_board_full():
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if available_square(row, col):
                    board[row][col] = "O"
                    score = minimax(board, depth + 1, False)
                    board[row][col] = None
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if available_square(row, col):
                    board[row][col] = "X"
                    score = minimax(board, depth + 1, True)
                    board[row][col] = None
                    best_score = min(score, best_score)
        return best_score

draw_lines()
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over and player == "X":
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, "X")
                if check_win("X"):
                    game_over = True
                    print("¡Has ganado!")
                else:
                    player = "O"

        if player == "O" and not game_over:
            best_move()
            if check_win("O"):
                game_over = True
                print("¡La máquina ha ganado!")
            else:
                player = "X"
            draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False

    draw_figures()
    pygame.display.update()

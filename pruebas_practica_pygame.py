import pygame
import sys

class Primerjuego:
    def __init__(self):
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        pygame.mixer.music.load("Tubular_Bells.mp3")
        pygame.mixer.music.play()
        self.ancho = 500
        self.alto = 400
        self.pantalla = pygame.display.set_mode((self.ancho, self.alto))

        pygame.display.set_caption("Juego con Pygame")
   
        self.rojo = (255,0, 0)
        self.blanco = (255, 255, 255)
        self.velocidad =  5
        self.x = self.ancho // 2
        self.y = self.alto // 2
       
    def movimientos(self):
        self.moviendo_abajo = False
        self.moviendo_arriba = False
        self.moviendo_derecha = False
        self.moviendo_izquierda = False

    def play(self):
        while True:
            pygame.time.delay(30)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    sys.exit()

                elif evento.type == pygame.KEYDOWN:
                    if evento[pygame.K_LEFT]: self.x -= self.velocidad
                self.moviendo_izquierda = True
                if teclas[pygame.K_RIGHT]: self.x += self.velocidad
                self.moviendo_derecha = True
                if teclas[pygame.K_UP]: self.y -= self.velocidad
                self.moviendo_arriba = True
                if teclas[pygame.K_DOWN]: self.y += self.velocidad
                self.moviendo_abajo = True

                teclas = pygame.KEYUP()
                if teclas[pygame.K_LEFT]: self.x -= self.velocidad
                self.moviendo_izquierda = False
                if teclas[pygame.K_RIGHT]: self.x += self.velocidad
                self.moviendo_derecha = False
                if teclas[pygame.K_UP]: self.y -= self.velocidad
                self.moviendo_arriba = False
                if teclas[pygame.K_DOWN]: self.y += self.velocidad
                self.moviendo_abajo = False

                self.pantalla.fill(self.blanco)
                pygame.draw.rect(self.pantalla, self.rojo, (self.x, self.y, 40, 40))
                pygame.display.update()
    
primero = Primerjuego()    
primero.play()
Primerjuego()
pygame.quit()
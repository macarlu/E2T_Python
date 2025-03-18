import pygame
import sys

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.mixer.music.load("Tubular_Bells.mp3")
pygame.mixer.music.play()

ancho, alto = 500, 400
pantalla = pygame.display.set_mode((ancho, alto))

pygame.display.set_caption("Juego con Pygame")

rojo = (255,0, 0)
blanco = (255, 255, 255)

x, y = ancho // 2, alto // 2
velocidad = 5

jugando = True
while jugando:
    pygame.time.delay(30)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]: x -= velocidad
        if teclas[pygame.K_RIGHT]: x += velocidad
        if teclas[pygame.K_UP]: y -= velocidad
        if teclas[pygame.K_DOWN]: y += velocidad

        pantalla.fill(blanco)
        pygame.draw.rect(pantalla, rojo, (x, y, 40, 40))
        pygame.display.update()

pygame.quit()
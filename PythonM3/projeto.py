import pygame
pygame.mixer.init()
musica=input('nome da musica:')
pygame.mixer.music.load(musica)
pygame.mixer.music.play()

print('digite p para pausar')
opção=input().upper()

if opção=='P':
    pygame.mixer.music.stop()
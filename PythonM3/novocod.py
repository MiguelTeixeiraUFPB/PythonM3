import pygame

def pausamusica():
    pygame.mixer.music.pause()

def trocamusica(musica):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play()

def retomarmusica():
    pygame.mixer.music.unpause()


#PROGRAMA PRINCIPAl
print('='*30)
print("Inicio do Player de Músicas")
print("="*30)
pygame.mixer.init()
musica=input('nome da musica:')
pygame.mixer.music.load(musica)
pygame.mixer.music.play()

while True:
    print('digite 1 para pausar')
    print('digite 2 para trocar a música')
    print('digite 3 para sair')
    print('digite 4 para obter a Playlist disponíveis')
    print('digite 5 para retomar  a música')
    print('digite 6 para obter autor da música tocada')
    print('digite 7 para se inscrever na Playlist')
    opção=int(input('...'))
    if opção==1:
        pausamusica()
    elif opção==2:
        musica=input('nome da musica')
        trocamusica(musica)
    elif opção==3:
        pygame.mixer.music.stop()
        break
    elif opção==5:
        retomarmusica()

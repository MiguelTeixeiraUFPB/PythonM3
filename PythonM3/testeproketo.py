import pygame

def lePlaylistDeArquivo(NomeArq):
    arquivo = open(NomeArq, 'r')
    linhas = []
    for linha in arquivo:
        linhaLida = linha.strip().split('#')
        linhas.append(linhaLida)
        arquivo.close
    return linhas


def listar_playlist(playlist):
    for lista in playlist:
        print(f'Banda: {lista [0]} Música: {lista[1]} Gênero: {lista[2]}')



def pesquisa_musica_por_genero(genero_pesq):
    for msc in playlist:
        if (msc[2] == genero_pesq):
            print(f'{msc [1]}')


def tocar_musica_playlist(musica_tocar):
    pygame.mixer.music.load(musica_tocar)
    pygame.mixer.music.play(musica_tocar)

print('='*30)
print("Inicio do Player de Músicas")
print("="*30)
pygame.mixer.init()
musica=input('nome da musica:')
nomealterado=musica+'.mp3'
pygame.mixer.music.load(nomealterado)
pygame.mixer.music.play()

while True:
    opcoes_playlist = int(input('Digite uma opção:\n1.Aperte para pausar\n2.Aperte para retomar\n3.Aperte para trocar a música\n4.Aperte para sair'))
    if (opcoes_playlist == 1):
        pygame.mixer.music.pause()
    elif (opcoes_playlist == 2):
        pygame.mixer.music.unpause()
    elif (opcoes_playlist == 3):
        msc_tocar = input('Digite o nome da música')
        pygame.mixer.music.stop()
        pygame.mixer.music.load(nomealterado)
        pygame.mixer.music.play()
    elif(opcoes_playlist == 4):
        print('fim')
        break

#PROGRAMA PRINCIPAL
playlist = lePlaylistDeArquivo('playlistMusicas.txt')
numColunas = len(playlist[0])
numLinhas = len(playlist) 
print(numColunas)
acabou = False
while (acabou == False):
    opcao = int(input(f'Digite uma opção:\n1.Listar músicas da playlist\n2.Pesquisar música por gênero\n3.Cadastrar música\n4.Tocar uma música\n'))
    if (opcao == 1):
        listar_playlist(playlist)
    elif (opcao == 2):
        genero_pesq = input('Qual o gênero a pesquisar?')
        pesquisa_musica_por_genero(genero_pesq)
    elif (opcao == 3):
        banda = input('Digite o nome da banda\n')
        msc = input('Digite o nome da música\n')
        genero = input('Digite o gênero da música')
        lista = [banda, msc, genero]
        playlist.append(lista)
    elif (opcao ==4):
        play1 = input('Digite o nome da música que você deseja ouvir')
        play2=play1+'.mp3'
        tocar_musica_playlist(play2)
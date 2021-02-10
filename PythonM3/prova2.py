def eleitor_votou(num_titulo,listatitulos):
    for t in listatitulos:
        if t==num_titulo:
            return True
        else:
            return False

def conta_votos(num_candidato,lista_votos):
    candidatox=0
    for voto in lista_votos:
        if voto==num_candidato:
            candidatox=candidatox+1
    if candidatox>=1:
            return candidatox
    else:
        return 'zero'


def imprime_votantes(listadetitulos):
    for titulo in listadetitulos:
        print(titulo)

#PROGRAMA PRINCIPAL
continuar = True
lista_eleitores = []
lista_votos = []
print("SISTEMA DE ELEIÇÕES")
while (continuar):
    numero_titulo = int(input("Qual o número do seu título?"))
    if (eleitor_votou(numero_titulo, lista_eleitores) == True):
        print("Eleitor já votou anteriormente.")
    else:
        print("Qual o número do candidato em que quer votar?")
        voto = int(input())
        lista_eleitores.append(numero_titulo)
        lista_votos.append(voto)
        print("Voto registrado com sucesso")
    respContinuar = input("Deseja continuar? Sim(S) ou Não (N)")
    if (respContinuar != "S"):
        continuar = False
        print("VOTAÇÃO ENCERRADA")
print("Qual o número do candidato a pesquisar?")
numero = int(input())
num_votos = conta_votos(numero, lista_votos)
print('eleitores:')
imprime_votantes(lista_eleitores)

print("Este candidato obteve ", num_votos, " votos")
print("FIM DO PROGRAMA")
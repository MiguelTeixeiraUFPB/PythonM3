def eleitor_votou(titulo, lista_Votaram):
    for n in lista_Votaram:
        if (n==titulo):
            return True
        else:
            return False

def conta_votos(voto_Candidato, todos_Votos):
    num_candidato = 0
    for n in todos_Votos:
        if (n==voto_Candidato):
            num_candidato+=1
        return num_candidato


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
        print("Qual o nome do candidato em quem você quer votar?")
        voto = int(input())
        lista_eleitores.append(numero_titulo)
        lista_votos.append(voto)
        print("Voto registrado com sucesso")
    respContinuar = input("Deseja Continuar? Sim(S) ou Não(N)")
    if (respContinuar != "S"):
        continuar = False
        print("VOTAÇÃO ENCERRADA")
print("Qual o número do candidato a pesquisar?")
numero = int(input())
num_votos = conta_votos(numero, lista_votos)
print("Esse candidato obteve", num_votos, "votos")
print("FIM DO PROGRAMA")
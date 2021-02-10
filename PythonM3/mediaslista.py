def media(notas):
    soma=0
    for k in notas:
        soma=soma+k
    media = soma/len(notas)
    return media

def maior_notas(notas):
    maior=0
    for k in notas:
        if k>=maior:
            maior=k
    return maior

def calc_nota_final(media):
    nota=(5-0.6*media)/0.4
    return nota
    

while True:
    print("CALCULADORA DE NOTAS")
    nome = input("Qual seu nome?")
    notas = []
    quantNotas=int(input('quantas provas você fez?'))
    if (quantNotas >= 0):
        for k in range(quantNotas):
            nota = float(input("Digite uma nota"))
            notas.append(nota)
        print("Sua média é:",media(notas))
        print("Sua maior nota foi:",maior_notas(notas))
        media_notas=media(notas)
        if media_notas>=4 and media_notas<7:
            print('se lascou,a nota que deve tirar na final é :', calc_nota_final(media_notas))
    else:
        print("A quantidade de notas deveria ser maior ou igual a 0")
    respContinuar = input("Deseja continuar? Sim(S) ou Não (N)").upper()
    if (respContinuar != "S"):
        break
print( "FIM DO PROGRAMA")
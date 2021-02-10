continuar = True
while (continuar):
    print("CALCULADORA DE NOTAS")
    nome = input("Qual seu nome?")
    notas = []
    print("Quantas provas você fez,",nome,"?")
    quantNotas = int(input())
    if (quantNotas >= 0):
        for k in range(quantNotas):
            nota = float(input("Digite uma nota"))
            notas.append(nota)
        print("Sua média é:%.1f" %media(notas))
        print("Sua maior nota foi:",maior(notas))
    else:
        print("A quantidade de notas deveria ser maior ou igual a 0")
    respContinuar = input("Deseja continuar? Sim(S) ou Não (N)")
    if (respContinuar != "S"):
        continuar = False
print( "FIM DO PROGRAMA")   
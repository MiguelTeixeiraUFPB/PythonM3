def ehMesValido(mes):
    if (mes>0 and mes<=12):
        return True
    else:
        return False
def ehAnoBissexto(ano):
#se é divisível por 400 ou é divisível por 4 e não é por 100
    if (ano%400 == 0) or (ano%4==0 and ano%100 !=0):
        return True
    else:
        return False
def ano_bissexto(lista):
    print('anos bissexto',lista)
    


n = int(input("Quantas datas você quer digitar?"))
listaAnos = []
listaanobissexto = []
for k in range(n):
    numeros = input("Digite uma data no formato dd/mm/aaaa").split("/")
    print(numeros)
    dia = int(numeros[0])
    mes = int(numeros[1])
    ano = int(numeros[2])
    listaAnos.append(ano)
    if (ehMesValido(mes) == False):
        print("O mês da data, que é ", mes, " não é válido")
    if (ehAnoBissexto(ano)):
        print(ano, "eh ano Bissexto")
        listaanobissexto.append(ano)
    else:
        print(ano, "não é ano Bissexto")
if len(listaanobissexto)>=1:
    ano_bissexto(listaanobissexto)
else:
    print('nenhum dos anos é bissexto')
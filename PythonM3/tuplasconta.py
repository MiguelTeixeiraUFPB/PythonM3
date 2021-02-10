numeros=('zero','um','dois','três','quatro','cinco')

while True:
    n1=int(input('digite um número de 0 a 5: '))
    if n1>5:
        print('número inválido')
    else:
        print(numeros[n1])
    resp=str(input('quer continuar? ')).upper()
    if resp=='NÃO':
        print('fim')
        break
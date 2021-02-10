#escrever nome por extenso de 0 a 10 usando tuplas
cont=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez')

while True:
    num=int(input('digite um número entre 0 e 10: '))
    if num<=10 and num>=0:
        print(f'o número que você digitou é {cont[num]}')
    else: 
        print('tente novamente.',end=' ')
    continuar=str(input('voce quer continuar: ')).upper()
    if continuar=='NÃO':
        break
print('fim')




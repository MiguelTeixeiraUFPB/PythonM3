def numeros_por_extenso(num):
    numeros_extenso=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez')
    transforma=numeros_extenso[n1]
    return transforma


n1=int(input('digite um número de 0 a 10: '))
print(numeros_por_extenso(n1))
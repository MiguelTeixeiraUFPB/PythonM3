numeros=[]
par=impar=positivo=negativo=0

for c in range(6):
    novonumero=int(input('digite um núemro: '))
    numeros.append(novonumero)
    if novonumero%2==0:
        par=par+1
    else:
        impar=impar+1
    if novonumero>0:
        positivo=positivo+1
    else:
        negativo=negativo+1

print(f'quantidade de par {par}, quantidade de impares: {impar}')
print(f'os números digitados foram: {numeros}')
print(f'o número de positivos é: {positivo}')
print(f'o número de negativos é: {negativo}')
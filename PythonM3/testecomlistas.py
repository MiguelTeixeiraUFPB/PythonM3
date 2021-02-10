numeros=[]
numeros.append(1)
numeros.append(2)
numeros.append(3)
numeros.append(4)
print(numeros)
for c, n in enumerate(numeros):
    print(f'na posição {c} temos o valor {n}')

#podemos fazer assim
listanum=[]
for k in range(5):
    listanum.append(int(input('digite um valor')))
print('lista de números do input',listanum)
for p,n in enumerate(listanum):
    print(f'na posição {p} temos o número{n}')


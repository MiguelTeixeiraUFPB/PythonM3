listanum = list()
listapares = list()
listaimpares = list()

for k in range(7):
    n=int(input('digite um número: '))
    listanum.append(n)
for num in listanum:
    if num%2==0:
        listapares.append(num)
    else:
        listaimpares.append(num)
listaimpares.sort()
listapares.sort()
print(f'os números pares são {listapares}')
print(f'os números impares são {listaimpares}')
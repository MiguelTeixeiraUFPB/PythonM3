lista=[]
listaf=[]
pessoas=[['miguel',18],['teresa',65],['emerson',33]]
print(pessoas[0][0])
print(pessoas[0])
galera=list()
galera.append(pessoas[:])
print(galera)
print(galera[0][0][1])
for p in  pessoas:
    print(f'o nome da pessoa  é {p[0]} e sua idade é {p[1]}')

for k in range(2):
    nome=input('digite um nome:')
    idade=int(input('digite a idade:'))
    lista.append(nome)
    lista.append(idade)
listaf.append(lista[:])
for pessoa in listaf:
    if pessoa[1]>=18:
        print(f'{pessoa[0]}  maior de idade')

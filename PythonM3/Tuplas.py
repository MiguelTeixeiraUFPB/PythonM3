lanche='hamburguer','pizza','coca'
print(len(lanche))#quantidades de itens na tupla
print(lanche[0])#hamburguer
print(lanche[1])#pizza
print(lanche[2])#coca
print(lanche[0:3])#do promeiro elemento até o último
for c in lanche:
    print(f'você pode escolher entre {c}')
for c in range(0,len(lanche)):
    print(lanche[c])

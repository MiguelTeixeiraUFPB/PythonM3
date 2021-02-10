pares=conta=0
nomes=('um ',' próximo','outro', 'último')
n2=[]
numpares=[]
for k in range (4):
    n1=int(input(f'digite {nomes[k]} número: '))
    conta+=1
    n2.append(n1)
    if n1%2==0:
        pares+=1
        numpares.append(n1)
    
print(f'o valor 9 apareceu {n2.count(9)}')   
print(f'quantidade de pares são: {pares}')
print(f'quantidade de números são :{conta}')
if 3 in n2:
    print(f'o número 3 apareceu na posição: {n2.index(3)+1}')
else:
    print('sem valor 3')
print(f'os pares são {numpares}')
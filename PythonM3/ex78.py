lista=[]
maior=menor=0

for k in range(5):
    n=int(input('digite um número: '))
    lista.append(n)
    if n>=maior:
        maior=n
    if k==0:
        menor=n
    else:
        if n<=menor:
            menor=n
print(f'o maior número é: {maior} {lista.index(maior)}')
print(f'o menor número é: {menor} {lista.index(menor)}')
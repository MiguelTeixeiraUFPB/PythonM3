lista=[]
maior=0
menor=0
for k in range(5):
    num=int(input(f'digite um número para a posição {k} :'))
    lista.append(num)
    if num>maior:
        maior=num
    if len(lista)==0:
        menor=num
    else:
        if menor<=num:
            menor=num
    
    

print('os números digitados foram',lista)
print(f'o maior número é {maior} e ele esta na posição {lista.index(maior)}')
print(f'o menor número é {menor} e ele está na posição {lista.index(menor)}')
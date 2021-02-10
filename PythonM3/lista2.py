valores=input().split(' ')
cod=int(valores[0])
quantidade=int(valores[1])

if cod==1:
    print(f'o valor é {4.00*quantidade}')
elif cod==2:
    print(f'o valor é {4.50*quantidade}')
elif cod==3:
    print(f'o valor é {5.00*quantidade}')
elif cod==4:
    print(f'o valor é {2.00*quantidade}')
else:
    print(f'o valor é {1.50*quantidade}')




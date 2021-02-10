print('mercado')
qnttipos=int(input('qnts tipos de produtos? '))
k=1
totalfeira=0
while k<=qnttipos:
    tipo=input(f'nome do produto {k}')
    preco=int(input('preço'))
    quantidade=int(input('qnt produto'))
    total=preco*quantidade
    print(f'o valor a ser pago é{total}')
    totalfeira=totalfeira+total
    k+=1
print(f'total {totalfeira}')

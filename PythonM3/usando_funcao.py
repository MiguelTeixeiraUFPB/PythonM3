def mostra_linha(msg):
    print('-'*50)
    print(msg)
    print('-'*50)
    

mostra_linha('miguel')

def soma(n1,n2):
    print(f'{n1}+{n2}={n1+n2}')

soma(2,2)

def numeros(*num):
    print(f'quantidade de números são: {len(num)} e os números são: {num}')

numeros(1,2,3,4,5)
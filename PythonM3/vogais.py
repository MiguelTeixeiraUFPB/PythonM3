lista=('melancia','linguagem','casa','carro')

for palavras in lista:
    print(f'\nna palavra {palavras} temos as vogais:',end=' ')
    for letra in palavras:
        if letra.upper() in 'AEIOU':
            print(f'{letra}',end=' ')
    
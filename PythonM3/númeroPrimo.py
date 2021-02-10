def primo(num):
    for k in range(2,num):
        if num%k==0:
            return print(f'o número {numero} não é primo')
    return print(f'o número {numero} é primo')



numero=int(input('digite um número para saber se ele é primo: '))
print(primo(numero))

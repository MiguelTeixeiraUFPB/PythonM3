def fatorial(n):
    resultado=0
    if n<=1:
        return 1
    else:
        resultado=n*fatorial(n-1)
        return resultado
num=int(input('digite um número para obter o fatorial: '))
print(fatorial(num))
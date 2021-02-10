def somatorio (x):
    soma = 0
    for k in range(1,x+1):
        soma += k
    return soma

print(somatorio(3))
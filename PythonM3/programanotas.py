def conta_notas_baixas (notas):
    nota_baixa = 0
    for nota in notas:
        if(nota < 7):
            nota_baixa+=1
    return nota_baixa

print(conta_notas_baixas([3.7, 9.9, 6.0]))
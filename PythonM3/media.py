def media(*notas):
    soma=0
    tam=len(notas)
    for nota in notas:
        soma=soma+nota
    print('A média de notas é ',soma/(len(notas)))
    print(f'A quantidade de notas é {tam}')

media(5,5,5)

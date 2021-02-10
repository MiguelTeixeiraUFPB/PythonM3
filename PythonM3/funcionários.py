quantidadefuncionarios=int(input('Quantidade de funcionários: '))
totalgasto=0
maiorsalario=0
nomemaiorsalario=''

for k in range(quantidadefuncionarios):
    nome=input(f'Nome do funcionário {k+1}: ')
    valorporhora=int(input(f'valor por hora  {k+1}: '))
    quantidadehora=int(input('quantidade de horas trabalhada: '))
    salario=valorporhora*quantidadehora
    totalgasto=totalgasto+salario
    if salario>maiorsalario:
        maiorsalario=salario
        nomemaiorsalario=nome
print(f'O maior salário é {maiorsalario} e o nome do maior salário é {nomemaiorsalario}')
print(f'O valor total gasto com salário é {totalgasto} ')

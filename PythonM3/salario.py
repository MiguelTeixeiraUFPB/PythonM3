print('\033[4;31;40m=X'*5,'SISTEMA DE CONTROLE DE NOTAS','=X'*5,'\033[m')
medturma=somanotas=notabaixa=notaboa=0
menor=10
quantAlunos=int(input('Quantidade de alunos :'))

for c in range(quantAlunos):
    nomealuno=str(input('Digite o nome do aluno: '))
    notaAluno=float(input(f'Digite a nota obtida por {nomealuno}: '))
    somanotas=somanotas+notaAluno
    if notaAluno<7:
        notabaixa+=1
    else:
        notaboa+=1
    if notaAluno<menor:
        menor=notaAluno
medturma=somanotas/quantAlunos
print(medturma)

print(f'notas baixa: {notabaixa}')
print(f'notas boa: {notaboa}')




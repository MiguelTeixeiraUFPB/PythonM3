
print("SISTEMA DE CONTROLE DE NOTAS") 
somaNotas = 0
quantNotasBaixas = 0 
quantNotasNaMedia = 0
n = int(input("Quantos alunos há na turma?")) 
for k in range(n):
    nome = input("Qual o nome do aluno?")
    nota = float(input("Qual a nota do aluno?")) 
    somaNotas = somaNotas + nota
    if (nota < 7):
        quantNotasBaixas = quantNotasBaixas + 1
        print(nome, " tirou nota baixa") 
    else:
        quantNotasNaMedia = quantNotasNaMedia + 1
        print(nome, " tirou nota boa") 
media = somaNotas/n
print("Média da Turma: %.1f " %media)
print("Quantidade de notas baixas: %d " %quantNotasBaixas) 
print("Quantidade de notas na média: %d " %quantNotasNaMedia)
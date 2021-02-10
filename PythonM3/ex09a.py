def existeClienteComCPF(cpfProcurado, listaCPFs):
 for cpf in listaCPFs:
 if (cpf == cpfProcurado):
 return True
 return False
def pesquisaNomeDoClienteDeCpf(cpf, listaCPFs, listaNomes):
 for k in range(len(listaCPFs)):
 if (listaCPFs[k]==cpf):
 return listaNomes[k]
 return "CPF não encontrado"

#PROGRAMA PRINCIPAL
n = int(input("Quantos clientes você quer cadastrar?"))
listaCPFs = []
listaNomes = []
for k in range(n):
 cpf = input("Digite o CPF do cliente")
 listaCPFs.append(cpf)
 nome = input("Digite o nome do cliente")
 listaNomes.append(nome)
print("LISTA DOS CLIENTES:")
for nome in listaNomes:
 print(nome)
cpfLido = input("Digite um CPF para pesquisar")
nomeEncontrado = pesquisaNomeDoClienteDeCpf(cpfLido, listaCPFs, listaNomes)
print("Nome:", nomeEncontrado)
def existeclientecomcpf(cpfprocurado,listacpf):
    for cpf in listacpf:
        if cpf==cpfprocurado:
            return True
        else: 
            return False

def pesquisanomedoclientedecpf(listanome,cpf,listacpf):
    for k in range(len(listacpf)):
        if listacpf[k]==cpf:
            return listanome[k]
        else:
            return'CPF INVÁLIDO'

def contaQuantidadeDeClientesComNome(lista,nome):
    quantidadenome=0
    for n in lista:
        if n==nome:
            quantidadenome=quantidadenome+1
    if quantidadenome>=1:
        return(quantidadenome)
    else:
        return'Não existe o nome na lista'

def imprimeClientes(listanomes,listacpf):
    for k in range(len(listacpf)):
        print(f'nome: {listanomes[k]} CPF:{listacpf[k]}')


n=int(input('digite quantidade de nomes: '))
listadecpf=[]
listadenome=[]
for k in range(n):
    cpf=int(input('digite o número do cpf'))
    listadecpf.append(cpf)
    nome=input('digite o nome')
    listadenome.append(nome)
print('lista de clientes')

for n in listadenome:
    print(n)

cpflido=int(input('digite o número do CPF para pesquisar'))
nomeprocurado=input('digite o nome a ser procurado')
print(pesquisanomedoclientedecpf(listadenome,cpflido,listadecpf))
print(contaQuantidadeDeClientesComNome(listadenome,nomeprocurado))
imprimeClientes(listadenome,listadecpf)




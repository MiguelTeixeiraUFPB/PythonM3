def listadenomes(qntnomes):
    nome1=[]
    for k in range(qntnomes):
        nome=input('digite um nome')
        nome1.append(nome)
    return nome1
quantidade= int(input('quantidade de nomes: '))
print(listadenomes(quantidade)) 
    

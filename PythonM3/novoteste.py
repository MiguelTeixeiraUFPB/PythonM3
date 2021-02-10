def lecontatosdearquivo(nomearquivo):
    arquivo=open(nomearquivo,'r')
    linhas=[]
    for linha in arquivo:
        linhalida=linha.split('#')
        linhas.append(linhalida)
    arquivo.close()
    return(linhas)

contatos=lecontatosdearquivo('agendariotinto.txt')
for linha in contatos:
    print(linha)
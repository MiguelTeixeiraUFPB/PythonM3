def leContatosDeArquivo(nomeArquivo):
    arquivo = open(nomeArquivo, 'r')
  # pega todos as linhas do arquivo
  # como uma lista de listas
    linhas = []
    for linha in arquivo:
        linhaLida = linha.strip().split("#")
        linhas.append(linhaLida)
    arquivo.close()
    return linhas

def gravaContatosEmArquivo(contatos, nomeArquivo):
  arquivo = open(nomeArquivo,'w')
  for nome, telefone, bairro, dia, mes in contatos:
      linha = nome + "#" + telefone + "#" + bairro + "#" + dia + "#"+ mes + "\n"
      arquivo.write(linha)
  arquivo.close()

def listaContatos(contatos):
    for linha in contatos:
        print(f'nome: {linha[0]} telefone: {linha[1]} bairro: {linha[2]} aniversário: {linha[3]} mês: {linha[4]}')

def pesquisanome(nomePesq, contatos):
    for n in contatos:
        if contatos[0]==nomePesq:
            print(f'{contatos[4]}/ {contatos[5]}')


def Pesquisarcontatosdobairro(bairroPesq,contatos):
    for b in contatos:
        if contatos[2]==bairroPesq:
            print(f'{contatos[0]}')

def listaContatosIniciadosCom(letra, contatos):
    print("CONTATOS COM PREFIXO:",letra)
    for nome, telefone, bairro, dia, mes in contatos:
        if (nome.upper()[0]== letra.upper()):
            print(f'Nome:{nome}, telefone:{telefone}, Bairro: {bairro}, Aniversário: {dia}/{mes}')

def pesquisaAniversarioDe(mesPesq, contatos):
    for m in contatos:
        if contatos[4]==mesPesq:
            print(f'{contatos[0]}')


#programa principal
contatos = leContatosDeArquivo("dados.txt")
numColunas = len(contatos[0])
numLinhas = len(contatos) 

print("Número de contatos lidos:",numLinhas)
print("Número de dados de cada contato:", numColunas)

acabou = False
while (not acabou):
    opcao = int(input("Digite uma opção:\n1.Listar contatos\n2.Pesquisar aniversario de...\n3.Pesquisar contatos do bairro\n4.Pesquisar aniversariantes do mês\n5.Cadastrar Contato\n6.Salvar dados\n7.Listar contatos com letra...\n8.Sair\n"))
    if (opcao == 1):
        listaContatos(contatos)
    elif (opcao == 2):
        nomePesq = input("Qual o nome a pesquisar?")
        pesquisanome(nomePesq, contatos)
    elif opcao==3:
        bairroPesq=input('bairro a pesquisar')
        Pesquisarcontatosdobairro(bairroPesq,contatos)
    elif opcao==4:
        mesPesq=input('data a pesquisar')
        pesquisaAniversarioDe(mesPesq, contatos)
    elif (opcao == 5):
        nome = input("Digite o nome da pessoa\n")
        telefone = input("Digite o telefone\n")
        bairro = input("Digite o bairro em que mora\n")
        diaAniversario = input("Digite o dia do aniversário\n")
        mesAniversario = input("Digite o mês do aniversário\n")
        contato = [nome, telefone, bairro, diaAniversario, mesAniversario]
        contatos.append(contato)
    elif (opcao ==6):
        gravaContatosEmArquivo(contatos, "AgendaRioTinto.txt")
    elif (opcao == 7):
        letra = input("Qual a letra a pesquisar?")
        listaContatosIniciadosCom(letra, contatos)
    elif (opcao ==8):
        acabou = True
print("FIM DO PROGRAMA. ATÉ MAIS")

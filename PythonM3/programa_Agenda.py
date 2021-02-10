def lecontatosdearquivo(nomearquivo):
    arquivo=open(nomearquivo,'r')
    linhas=[]
    for linha in arquivo:
        linhalida=linha.strip().split('#')
        linhas.append(linhalida)
    return(linhas)

def listacontatos(contatos):
    for linha in contatos:
        print(f'nome: {linha[0]}, telefone:{linha[1]} bairro::{linha[2]}aniversário: {linha[3]} mês: {linha[4]}')

def pesquisarAniversarioP_Nome(nomepessoa,contatos):
    for nome,telefone,bairro,aniversário,mes in contatos:
        if nomepessoa==nome:
            print(f'{aniversário}/{mes}')
        

def pesquisarPessoasDobairro(contatosbairro,contatos):
    for nome,telefone,bairro,aniversário,mes in contatos:
        if bairro==contatosbairro:
            print(nome)

def pesquisarAniversariantedoMes(mesaniversariante,contatos):
    for nome,telefone,bairro,aniversário,mes in contatos:
        if mes==mesaniversariante:
            print(f'{nome}')


def gravaContatos(contatos, nomeArquivo):
    arquivo = open(nomeArquivo,'w')
    for nome, telefone, bairro, dia, mes in contatos:
        linha = nome + "#" + telefone + "#" + bairro + "#" + dia + "#"+ mes + "\n"
        arquivo.write(linha)
    arquivo.close()

def listaContatosIniciadosCom(letra, contatos):
    print("CONTATOS COM PREFIXO:",letra)
    for nome, telefone, bairro, dia, mes in contatos:
        if (nome.upper()[0]== letra.upper()):
            print("Nome:", nome, ", Telefone:", telefone, ", Bairro:", bairro, ", Aniversário:", dia,"/",mes)
#PROGRAMA PRINCIPAL
contatos=lecontatosdearquivo('agendariotinto.txt')
numcolunas=len(contatos[0])
numlinhas=len(contatos)
while True:
    escolha=int(input('digite uma opção \n 1) Listar contatos\n 2) pesquisar aniversariante de ... \n 3) pesquisar contatos do bairro \n 4) pesquisar aniversariantes do mês \n 5) cadastrar um contato\n 6) salvar dados\n 7) listar contatos com letra\n 8) sair'))
    if escolha==1:
        listacontatos(contatos)
    elif escolha==2:
        nomepessoa=str(input('nome da pessoa'))
        pesquisarAniversarioP_Nome(nomepessoa,contatos)
    elif escolha==3 :
        contatosbairro=str(input('contatos do Bairro: '))
        pesquisarPessoasDobairro(contatosbairro,contatos)
    elif escolha==4:
        mesaniversariante=str(input('aniversariante do mês'))
        pesquisarAniversariantedoMes(mesaniversariante,contatos)
    elif escolha ==5:
        nomepessoa=input('nome para cadastro')
        telefone=int(input('telefone para cadastro'))
        bairropessoa=input('bairro para cadastro ')
        dia=int(input('dia para cadastro'))
        mes=input('mês para cadastro')    
        contatonovo=[nomepessoa,telefone,bairropessoa,dia,mes]
        contatos.append(contatonovo)
    elif escolha==6:
        gravaContatos(contatos,'agendariotinto.txt')
    elif escolha==7:
        letra=str(input('letra ')).upper()
        listaContatosIniciadosCom(letra,contatos)
    elif escolha==8:
        break
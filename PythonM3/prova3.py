def existe_animal_do_tipo(tipo_animal,listadeanimais):
    for codigo,tipo,nome,idade in listadeanimais:
        if tipo==tipo_animal:
            return True
        return False

def conta_animais_com_idade_maior_que(idade_pesq, lista_animais):
    for codigo,tipo,nome,idade in lista_animais:
        qntanimais=0
        if idade>=idade_pesq:
            qntanimais+=1
    return qntanimais


def imprime_animais_do_tipo(lista_animais,tipoanimal):
    nomeanimais=[]
    for codigo,tipo,nome,idade in lista_animais:
        if tipoanimal==tipo:
            nomeanimais.append(nome)
    lista = []
    for a in nomeanimais:
        if a not in lista:
            lista.append(a)
    print(lista)



            

continuar = True
lista_animais = []
print("SISTEMA DE GERÊNCIA DOS ANIMAIS DO ZOOLÓGICO")
while (continuar):
    codigo = input("Qual o código do animal a cadastrar?")
    tipo = input("Qual o tipo do animal?")
    nome = input("Qual o nome do animal?")
    idade = int(input("Qual a idade do animal?"))
    novo_animal = [codigo, tipo, nome, idade]
    lista_animais.append(novo_animal)
    print("Animal cadastrado com sucesso")
    respContinuar = input("Deseja continuar? Sim(S) ou Não (N)")
    if (respContinuar != "S"):
        continuar = False
        print("CADASTRO ENCERRADO")
print("Qual a idade a pesquisar?")
idade_pesq = int(input())
num_animais = conta_animais_com_idade_maior_que(idade_pesq, lista_animais)
linha=len(lista_animais)
coluna=len(lista_animais[0])
print("Existem ", num_animais, " com mais de ", idade_pesq, " anos")
tipo_pesq = input("Qual o tipo de animal a pesquisar?")
if (existe_animal_do_tipo(tipo_pesq, lista_animais)):
    print("Existe")
else:
    print("Não existe")
print("FIM DO PROGRAMA")
tipoanimal=input('tipo animal')
imprime_animais_do_tipo(lista_animais,tipoanimal))
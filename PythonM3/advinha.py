from random import randint

num=randint(1,10)
pontuacao=5

while True:
    teste=int(input('tente acertar o número de 1 a 10: '))
    if num==teste:
        print('você acertou!')
        break
    elif teste<num:
        pontuacao-=1
        print('Dica: o número pensado é maior!')
    else :
        pontuacao-=1
        print('Dica: o número pensado é menor!')
    if pontuacao==0:
        print('Você zerou a pontuação')
        break
print(f'a pontuação é de {pontuacao}')

def getQuantidadeMaximaDeDiasDoMes():
    trintaeumdia=[1,3,5,7,8,10,12]
    while True:
        meses=int(input('digite mês de 1 a 12'))
        if meses<1 and meses>12:
            print('mês fora do padrão')
        elif meses in trintaeumdia:
            print(f'o mês {meses} tem 31 dias')
        elif meses==2:
            print(f'o mês {meses} tem 28 ou 29 dias')
        else:
            print(f'o mês {meses} não tem 31 dias')
        continue1=input('quer continuar?').upper()
        if continue1=='NÃO' or 'NAO':
            print('fim')
            break

getQuantidadeMaximaDeDiasDoMes()

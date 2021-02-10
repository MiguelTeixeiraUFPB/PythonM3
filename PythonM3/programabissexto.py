def eh_ano_bissexto(ano):
    if (ano%400 == 0) or (ano%4==0 and ano%100!=0):
        return True
    else:
        return False


def eh_data_valida(dia,mes,ano):
    if (mes in [1,3, 5, 7, 8, 10, 12]):
        if (dia>=1 and dia<=31):
            return True
    elif (mes in [4,6,9,11]):
        if (dia>=1 and dia<=30):
            return True
    elif (mes == 2):
        if (eh_ano_bissexto(ano)):
            if (dia>=1 and dia<=29):
                return True
        else:
            if (dia>=1 and dia<=28):
                return True
    return False


#PROGRAMA PRINCIPAL
data = input("Digite uma data no formato dd/mm/aaaa\n").split("/")
dia = int(data[0])
mes = int(data[1])
ano = int(data[2])
if(eh_data_valida(dia,mes,ano) == True):
    print("Data válida")
else:
    print("Data inválida")
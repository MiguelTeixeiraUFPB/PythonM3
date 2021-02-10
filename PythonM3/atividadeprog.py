def verifica_ano_bissexto(ano):
    if(ano%400==0) or (ano%4==0 and ano%100!=0):
        return "Bissexto"
    else:
        return "Não Bissexto"

def verifica_data (dia,mes,ano):
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        max_dias=31
    elif mes == 2:
        if verifica_ano_bissexto(ano)=="Bissexto":
            max_dias=29
        else:
            max_dias=28
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        max_dias=30
    else:
        return "Data Inválida"
    if dia>=1 and dia<=max_dias:
        return "Data Válida"
    else:
        return "Data Inválida"

data=input("Digite a data: ")
dia,mes,ano=data.split("/")
dia=int(dia)
mes=int(mes)
ano=int(ano)
print(verifica_data(dia,mes,ano))
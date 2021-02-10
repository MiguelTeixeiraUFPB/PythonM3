ListaNomeIdade=list()
dados=list()
maispesado=maisleve=quantidade=0

while True:
    nome=str(input('digite o nome '))
    peso=int(input('digite o peso'))
    dados.append(nome)
    dados.append(peso)ListaNomeIdade.append(dados[:])
    dados.clear()
    continuar=input('quer continuar?').upper()
    if continuar!='SIM':
        break

print(ListaNomeIdade)

for c i ListaNomeIdade:
    print(f'{c[0]} pesa {c[1]}')

print(f'pessoas cadastradas {len(ListaNomeIdade)}')

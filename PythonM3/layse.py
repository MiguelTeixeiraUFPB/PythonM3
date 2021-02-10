lstano1827=[]
listaano=[]
somador=maisvalioso=itemvalioso=anovalioso=0
for k in range(2):
    descricao=str(input('descrição: '))
    valor=int(input('valor: '))
    ano=int(input('ano'))
    listaano.append(ano)
    somador=somador+valor
    if ano <=1827:
        lstano1827.append(ano)
    if valor>=maisvalioso:
        maisvalioso=valor
        itemvalioso=descricao
        anovalioso=ano
media=somador/len(listaano)
print(f'itens produzidos antes de  1827--->{ len(lstano1827)}')
print(f' valor médio dos itens---> {media:.2f}')
print(f'dados do objeto mais valioso---> {itemvalioso},{anovalioso}')
    
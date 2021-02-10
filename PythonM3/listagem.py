suplementos=('Whey', 76.99,
        'Creatina', 40.00,
        'Hipercalórico', 70.00,
        'Multivitaminico', 29.00,
        'Maltodextrina', 25.00,
        'Dilatafil',40,
        'Macaperuana',42)
print(f'LISTAGEM DE PREÇOS')

for item in range(0,len(suplementos)):
    if item%2==0 :
        print(f'{suplementos[item]:.<30}',end=' ')
    else:
        print(f'R${suplementos[item]:.2f}')


    
  
    
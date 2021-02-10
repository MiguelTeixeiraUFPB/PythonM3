times=('Corinthians','São paulo', 'Flamengo','Cruzeiro', 'ATLÉTICO MINEIRO','Inter',
        'Grêmio','Santos','Palmeiras','Goias','Curitiba')
print("=x"*10)
print('TABELA')
print("=x"*10)

for t in times:
    print(t)

print("=x"*10)
print('4 PRIMEIROS ')
print("=x"*10)

for t in times[0:4]:
    print(t)

print("=x"*10)
print('4 ÚLTIMOS ')
print("=x"*10)
print(times[-4:])
print("=x"*10)
print(f' {sorted(times)}')


time=str(input('digite o time q deseja obter a posição: '))

print(times.index(time)+1)

timeposição=int(input('digite a posição para obter o time: '))
timeposiçãomenos=timeposição-1
print(times[timeposiçãomenos])

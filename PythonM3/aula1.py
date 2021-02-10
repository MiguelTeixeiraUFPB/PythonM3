lanche='hambúrger','suco','pizza','podim'
#tuplas são imutáveis

for c in(lanche):
    if c==lanche[1]:
        print(f'eu vou beber {c}')
    else:
        print(f'eu vou comer {c}')
print(len(lanche))

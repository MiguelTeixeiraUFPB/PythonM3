lista=['hamburguer','coca','pizza','pão']
lista.append('pepsi')#adiciona um elemnento na última posição
print(lista)
lista.insert(0,'água')
print(lista)
del lista[2]# deletar elementos da lista
print(lista)
print(lista[2])#mostrar um elemento da lista
lista.remove('pão')

print(lista)
if 'pizza' in lista:# se tiver elemento na lista 
    lista.remove('pizza')#remove o elemento
    print(lista)
else:
    print('não tem pizza nessa lista')
valores100=list(range(0,101))#cria uma lista do 0 até o 100 

valores100.sort(reverse=True)# inverte a ordem da lista
print(valores100)
print(len(valores100))#quantidade de elementos na lista

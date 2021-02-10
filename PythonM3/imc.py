peso = int(input("qual seu peso? "))
altura = float(input("Qual a sua altura em (m)?"))

#Menor que 18,5 - Abaixo do peso
#Entre 18,5 e menor que 25 - Peso normal
#Entre 25 e menor que 30 - Sobrepeso (acima do peso desejado)
#Igual ou acima de 30 - Obesidade

imc = peso/(altura*altura)

if imc<18.5:
    print('humm, se bater um vento o frango voa, abaixo do peso.')
elif imc>=18.5 and imc<25 :
    print('Arnold fica feliz, peso normal.')
elif imc>25 and imc<30:
    print('hummm, vamos maneirar no carboidrato')
print()
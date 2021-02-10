import turtle

opcaoCor = input("Qual a cor de fundo do jogo? \n1. Branco\n2.Verde\n")
janela = turtle.Screen()
if (opcaoCor == "1"):
    janela.bgcolor("white")  # muda a cor do background da janela p/ branca
elif (opcaoCor == "2"):
    janela.bgcolor("lightgreen")   # muda a cor do background da janela p/verde
else:
    print("Opção inválida. Cor rosa será usada")
    janela.bgcolor("pink")
alex = turtle.Turtle()         # cria  a tartaruga alex
alex.shape("turtle")
alex.color("blue")             # muda a cor da tartaruga
alex.speed(1)                  # muda a velocidade da tartaruga [0-10]


alex.forward(80)               # manda alex andar 80 unidades pra frente
alex.left(90)                     # manda alex virar 90 graus para esquerda
alex.forward(80)
alex.left(90)
alex.forward(80)
alex.left(90)
alex.forward(80)
alex.left(90)

alex.color("gray")        # muda a cor de alex

for k in range(4):             # repita 4 vezes o código abaixo
    alex.forward(80)          # manda alex andar 80 unidades pra frente
    alex.left(90)             # manda alex virar 90 graus para a esquerda


janela.exitonclick()
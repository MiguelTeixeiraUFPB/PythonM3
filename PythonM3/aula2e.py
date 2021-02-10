import turtle

opcaoCor = input("Qual a cor de fundo do jogo? \nRed \nGreen\n").upper().strip()
janela = turtle.Screen()
if (opcaoCor == 'RED'):
    janela.bgcolor('red')  # muda a cor do background da janela p/ red
elif (opcaoCor == "GREEN"):
    janela.bgcolor("green")   # muda a cor do background da janela p/verde
else:
    print("Opção inválida. Cor rosa será usada")
    janela.bgcolor("pink")
alex = turtle.Turtle()         # cria  a tartaruga alex
alex.shape("turtle")
alex.color("blue")             # muda a cor da tartaruga
alex.speed(3)                  # muda a velocidade da tartaruga [0-10]
alex.color("blue")        # muda a cor de alex

for k in range(2):             # repita 4 vezes o código abaixo
    alex.forward(100)          # manda alex andar 100 unidades pra frente
    alex.right(120)
alex.left(120)
for k in range(2):
    alex.forward(100)          # manda alex andar 100 unidades pra frente
    alex.left(120)
janela.exitonclick()
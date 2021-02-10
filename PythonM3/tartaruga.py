import turtle

janela=turtle.Screen()# abre a janela
janela.bgcolor('red')
miguel=turtle.Turtle()
miguel.shape('turtle') #muda o shape para tartaruga

miguel.forward(100)     
miguel.right(90)        
miguel.forward(100)
miguel.right(90)
miguel.forward(100)
miguel.right(90)#vira a direita em um angulo de 90 
miguel.forward(100)#anda para frente 

miguel.speed(1) #indica velocidade de movimentação (0-10)

miguel.color('black')
janela.bgcolor('red')
janela.exitonclick()
import random

print("*********************************")
print("Passeio aleatório em 2D")
print("Iremos começar do valor (0,0)")
print("Em seguida vamos sortear uma posição, cima, baixo, esquerda ou direita e combinações")
print("Assim sussessivamente")
print("*********************************")

n = float(input('Informe a quantidade de passeios : '))
k = 0
x = 0
y = 0
possi = ['1', '2', '3', '4', '5', '6', '7', '8']

while (k < n):
    moeda = float((random.choice(possi)))

    if (moeda == 1):
        print("Direita")
        x = x + 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y)=(",x,",",y,")")
        

    if (moeda == 2):
        print("Esquerda")
        x = x - 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y)=(",x,",",y,")")
        

    if (moeda == 3):
        print("Cima")
        y = y + 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y)=(",x,",",y,")")
        

    if (moeda == 4):
        print("Baixo")
        y = y - 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y)=(",x,",",y,")")
        

    if (moeda == 5):
        print("Cima + Direita")
        y = y + 1
        x = x + 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y)=(",x,",",y,")")


    if (moeda == 6):
        print("Cima + Esquerda")
        y = y + 1
        x = x - 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y)=(",x,",",y,")")
        

    if (moeda == 7):
        print("Baixo + Direita")
        y = y - 1
        x = x + 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y)=(",x,",",y,")")
        

    if (moeda == 8):
        print("Baixo + Esquerda")
        y = y - 1
        x = x - 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y)=(",x,",",y,")")
        

        
    

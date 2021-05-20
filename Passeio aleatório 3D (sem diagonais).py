import random

print("*********************************")
print("Passeio aleatório em 2D")
print("Iremos começar do valor (0,0,0)")
print("Em seguida vamos sortear uma posição, cima, baixo, esquerda, direita, frente ou atrás")
print("Assim sussessivamente")
print("*********************************")

n = float(input('Informe a quantidade de passeios : '))
k = 0
x = 0
y = 0
z = 0
possi = ['1', '2', '3', '4', '5', '6']

while (k < n):
    moeda = float((random.choice(possi)))

    if (moeda == 1):
        print("Frente")
        x = x + 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y,z)=(",x,",",y,",",z,")")
        

    if (moeda == 2):
        print("Atrás")
        x = x - 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y,z)=(",x,",",y,",",z,")")
        

    if (moeda == 3):
        print("Cima")
        z = z + 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y,z)=(",x,",",y,",",z,")")
        

    if (moeda == 4):
        print("Baixo")
        z = z - 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y,z)=(",x,",",y,",",z,")")
        

    if (moeda == 5):
        print("Direita")
        y = y + 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y,z)=(",x,",",y,",",z,")")
        

    if (moeda == 6):
        print("Esquerda")
        y = y - 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y,z)=(",x,",",y,",",z,")")
        


        
    

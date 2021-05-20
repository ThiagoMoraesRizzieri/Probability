import random

print("*********************************")
print("Passeio aleatório em 2D")
print("Iremos começar do valor (0,0,0)")
print("Em seguida vamos sortear uma posição, cima, baixo, esquerda, direita, frente ou atrás e suas combinações!")
print("Assim sussessivamente")
print("*********************************")

n = float(input('Informe a quantidade de passeios : '))
k = 0
x = 0
y = 0
z = 0
possi = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']

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

    if (moeda == 7):
        print("Frente + Cima")
        x = x + 1
        z = z + 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y,z)=(",x,",",y,",",z,")")

    if (moeda == 8):
        print("Frente + Baixo")
        x = x + 1
        z = z - 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y,z)=(",x,",",y,",",z,")")

    if (moeda == 9):
        print("Atrás + Cima")
        x = x - 1
        z = z - 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y,z)=(",x,",",y,",",z,")")

    if (moeda == 10):
        print("Atrás + Baixo")
        x = x - 1
        z = z - 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y,z)=(",x,",",y,",",z,")")

    if (moeda == 11):
        print("Frente + Direita")
        x = x + 1
        y = y + 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y,z)=(",x,",",y,",",z,")")

    if (moeda == 12):
        print("Frente + Esquerda")
        x = x + 1
        y = y - 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y,z)=(",x,",",y,",",z,")")

    if (moeda == 13):
        print("Atrás + Direita")
        x = x - 1
        y = y + 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y,z)=(",x,",",y,",",z,")")

    if (moeda == 14):
        print("Atrás + Esquerda")
        x = x - 1
        y = y - 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y,z)=(",x,",",y,",",z,")")

    if (moeda == 15):
        print("Direita + Cima")
        y = y + 1
        z = z + 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y,z)=(",x,",",y,",",z,")")

    if (moeda == 16):
        print("Direita + Baixo")
        y = y + 1
        z = z - 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y,z)=(",x,",",y,",",z,")")

    if (moeda == 17):
        print("Esquerda + Cima")
        y = y - 1
        z = z + 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y,z)=(",x,",",y,",",z,")")

    if (moeda == 18):
        print("Esquerda + Baixo")
        y = y - 1
        z = z - 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y,z)=(",x,",",y,",",z,")")

    if (moeda == 19):
        print("Frente + Direita + Cima")
        x = x + 1
        y = y + 1
        z = z + 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y,z)=(",x,",",y,",",z,")")

    if (moeda == 20):
        print("Frente + Direita + Baixo")
        x = x + 1
        y = y + 1
        z = z - 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y,z)=(",x,",",y,",",z,")")
        
    if (moeda == 21):
        print("Frente + Esquerda + Cima")
        x = x + 1
        y = y - 1
        z = z + 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y,z)=(",x,",",y,",",z,")")

    if (moeda == 22):
        print("Frente + Esquerda + Baixo")
        x = x + 1
        y = y - 1
        z = z - 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y,z)=(",x,",",y,",",z,")")

    if (moeda == 23):
        print("Atrás + Direita + Cima")
        x = x - 1
        y = y + 1
        z = z + 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y,z)=(",x,",",y,",",z,")")

    if (moeda == 24):
        print("Atrás + Direita + Baixo")
        x = x - 1
        y = y + 1
        z = z - 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y,z)=(",x,",",y,",",z,")")

    if (moeda == 25):
        print("Atrás + Esquerda + Cima")
        x = x - 1
        y = y - 1
        z = z + 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y,z)=(",x,",",y,",",z,")")

    if (moeda == 26):
        print("Atrás + Esquerda + Baixo")
        x = x - 1
        y = y - 1
        z = z - 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print("(x,y,z)=(",x,",",y,",",z,")")

        

        
        


        
    

import random

print("*********************************")
print("Passeio aleatório nos valores inteiros")
print("Iremos começar do valor 0")
print("EM seguida jogamos uma moeda, se der cara somamos 1 se der coroa retiramos 1")
print("Assim sussessivamente")
print("*********************************")

n = float(input('Informe a quantidade de passeios : '))
k = 0
x = 0

possi = ['1', '2']

while (k < n):
    moeda = float((random.choice(possi)))

    if (moeda == 1):
        print("Saiu cara")
        x = x + 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print(x)
        

    if (moeda == 2):
        print("Saiu coroa")
        x = x - 1
        k = k + 1
        print("Na", k,"º jogada temos o valor:")
        print(x)
        
    

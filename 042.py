# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, 
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

reta_1 = float(input("Insira o valor da primeira reta: "))
reta_2 = float(input("Insira o valor da segunda reta: "))
reta_3 =float(input("Insira o valor da terceira reta: "))

if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2:
    print("PODEM formar um triângulo!!")

    if reta_1 == reta_2 == reta_3:
        print("Triângulo EQUILÁTERO")

    elif reta_1 == reta_2 != reta_3 or reta_2 == reta_3 != reta_1:
        print("Triângulo ISÓSCELES")

    else:
        print("Triângulo ESCALENO")

else:
    print("NÃO podem formar um triângulo.")

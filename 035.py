# Exercício Python #035 - Analisando Triângulo v1.0  #????

# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

reta_1 = float(input("Insira o valor da primeira reta: "))
reta_2 = float(input("Insira o valor da segunda reta: "))
reta_3 =float(input("Insira o valor da terceira reta: "))

if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2:
    print("PODEM formar um triângulo!!")
else:
    print("NÃO podem formar um triângulo.")

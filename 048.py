# Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três 
# e que se encontram no intervalo de 1 até 500.

soma = cont = 0
for c in range(1, 501, 2): #imprimiu de 1 até 500
    if c % 3 == 0: #pegou os multiplos de 3
        cont = cont + 1
        soma = soma + c #somou qnts mult tem
print(f"A soma de todos os {cont} valores solicitados é {soma}")

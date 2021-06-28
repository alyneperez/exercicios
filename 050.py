# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o.

soma = cont = 0
for i in range(1,7):
    num = int(input(f"Digite o {i}º valor:"))
    if num % 2 == 0:
        soma = soma + num        #soma += num  #somar os pares
        cont = cont + 1          # contar qnts tem
print(f"Você informou {cont} números PARES e a soma entre eles foi {soma}")

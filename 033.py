# Exercício Python #033 - Maior e menor valores 
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
# Verificando quem é o menor entre eles:
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando qual é o maior:
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f"O MENOR valor entre eles é {menor}.")
print(f"E o MAIOR é: {maior}.")

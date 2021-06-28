# Exercício Python #030 - Par ou Ímpar: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input("Digite um número inteiro para descobrir se ele é PAR ou ÍMPAR: "))
if num % 2 == 0:
    print("O número digitado é PAR.")
else:
    print("O número digitado é ÍMPAR.")

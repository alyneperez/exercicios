# Exercício Python #023 – Separando dígitos de um número

#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex: Digite um número:1834
# unidade:4
# dezena:3
# centena:8
# milhar:1

num = int(input("Informe um número de 0 a 9999: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f"Analisando o número {num}...")
print(f"Sua unidade é: {u}")
print(f"Sua dezena é: {d}")
print(f"Sua centena é: {c}")
print(f"Seu milhar é: {m}")

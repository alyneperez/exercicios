# Exercício Python #017 – Catetos e Hipotenusa

# Faça um programa que leia o comprimento de um cateto oposto e do cateto adjacente de um triangulo retangulo, 
# calcule e mostre o comprimento da hipotenusa. (modulo)

#forma matematica

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f"A hipotenusa vai medir: {hi:.2f}")

# Outra solução utilizando a biblioteca math

# from math import hypot
# co = float(input("Comprimento do cateto oposto: "))
# ca = float(input("Comprimento do cateto adjacente: "))
# hi = hypot(co, ca)
# print(f"A hipotenusa vai medir: {hi:.2f}")

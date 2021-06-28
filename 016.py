# Exercício Python #016 – Quebrando um número

# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.

num = float(input("Digite um número: "))
print(f"O valor digitado foi {num} e sua porção inteira é {int(num)}")


#Outra Solução:

# import math
# num = float(input("Digite um número real para obter sua porção inteira: "))
# print(f"{num:.2f} == {math.trunc(num):.0f}")

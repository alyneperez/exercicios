# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

#primo é divisivel por 1 e por ele mesmo

num = int(input("Digite um número: "))
contador = 0
for c in range(1, num + 1):
    if num % c == 0:
        contador += 1
print(f"O número {num} foi divisível {contador} vezes!")
if contador == 2:
    print("O número é PRIMO")
else:
    print("O número NÃO é primo")

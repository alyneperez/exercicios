# Exercício Python #028: Jogo da advinhação v.1.0

# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

print("=*="*6)
print("JOGO DA ADVINHAÇÃO")
print("=*="*6)

print("Vou escolher um número de 0 a 5... tente advinhar!")
print("pensando....")

computador = random.randint(1,5)
print("Qual número eu escolhi?")
jogador = int(input("Digite sua escolha: "))
print(f"Você acha que eu escolhi o número {jogador}.")

if computador == jogador:
    print("ACERTOU!!")
else:
    print(f"ERROU! eu pensei no número {computador}")

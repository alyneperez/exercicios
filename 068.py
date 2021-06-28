# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.


import random

vitorias = 0
while True:
    print("=*="*6)
    print("PAR OU ÍMPAR")
    print("=*="*6)

    lista = ["PAR" , "ÍMPAR"]
    sorteio = random.choice(lista)

    print(f"Eu escolho {sorteio}")

    jogador = int(input("Digite um número de 0 a 5: "))
    computador = random.randint(0,5)

    print(f"JOGADOR {jogador} x {computador} COMPUTADOR ")

    total = jogador + computador

    if total % 2 == 0 and sorteio == "ÍMPAR":
        print("Você ganhou, o total deu PAR!")
        print("Vamos jogar novamente...")
        vitorias += 1
    elif total % 2 == 1 and sorteio == "PAR":
        print("Você ganhou, o total deu ÍMPAR!")
        print("Vamos jogar novamente...")
        vitorias += 1
    elif total % 2 == 0 and sorteio == "PAR":
        print("Eu ganhei, o total deu PAR!")
        break
    elif total % 2 == 1 and sorteio == "ÍMPAR":
        print("Eu ganhei, o total deu ÍMPAR!")
        break
print(f"GAME OVER!! Você obteve {vitorias} vitória(s) consecutiva(s)...")

#Outra Solução:

# from random import randint
# vitorias = 0
# while True:
#     jogador = int(input("Insira um valor: "))
#     computador = randint(0, 10)
#     total = jogador + computador
#     tipo = " "
#     while tipo not in "PI":
#         tipo = input("Par ou Impar? [P/I] ").strip().upper()[0]
#     print(f"Você escolheu {jogador} e o computador {computador}. Total de {total}")
#     print("DEU PAR" if total % 2 == 0 else "DEU IMPAR")
#     if tipo == "P":
#         if total % 2 == 0:
#             print("Você VENCEU!!")
#             vitorias += 1
#         else:
#             print("Você PERDEU!!")
#             break
#     elif tipo == "I":
#         if total % 2 == 1:
#             print("Você VENCEU!!")
#             vitorias += 1
#         else:
#             print("Você PERDEU!!")
#             break
#     print("Vamos jogar novamente...")
# print(f"GAME OVER! Você venceu {vitorias} vezes.")

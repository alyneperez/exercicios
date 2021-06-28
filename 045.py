# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

print("=-=" * 8)
print ("PEDRA, PAPEL OU TESOURA")
print("=-=" * 8)

print(""" Escolha... 
    [ 0 ]  PEDRA
    [ 1 ]  PAPEL
    [ 2 ]  TESOURA """)

itens = ("PEDRA", "PAPEL", "TESOURA")

jogador = int(input("Digite a opção: "))

sleep(1)
print("JO")
sleep(1.5)
print("KEN")
sleep(1.5)
print("PO...")

computador = randint(0,2)

print(f"Você escolheu {(itens[jogador])}")
print(f"Computador escolheu {(itens[computador])}")

if (jogador == 0 and computador == 0) or (jogador == 1 and computador == 1) or (jogador == 2 and computador == 2):
    print("EMPATE")

elif (jogador == 0 and computador == 1) or (computador == 0 and jogador == 1):
    print("PAPEL ganha!!")

elif (jogador == 1 and computador == 2) or (computador == 1 and jogador == 2):
    print("TESOURA ganha!!")

elif (jogador == 0 and computador == 2) or (computador == 0 and jogador == 2):
    print("PEDRA ganha!!")

else:
    print("Opção inválida. Tente novamente.")

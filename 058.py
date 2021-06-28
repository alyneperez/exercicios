# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint

tent = 0

computador = randint(0 , 10)
print("Vou pensar em um número de 0 a 10. Tente advinhar...")
jogador = -1

while jogador != computador:
    jogador = int(input("Em que número eu pensei? "))
    tent = tent + 1

    if jogador < computador:
        print("MAISSSS...")
    elif jogador > computador:
        print("MENOSSSS...")
    else:
        print("PARABÉNS!! Você conseguiu me vencer!")
        print(f"Com {tent} tentativa(s).")

 #Outra Solução:
      
# from random import randint
# computador = randint(1,10)
# print("Sou seu computador... Acabei de pensar em um número entre 0 e 10")
# print("Será que vc consegue advinhar qual foi?")
# acertou = False
# palpites = 0
# while not acertou:
#     jogador = int(input("Qual é seu palpite? "))
#     palpites += 1
#     if jogador == computador:
#         acertou = True
#     else:
#         if jogador < computador:
#             print("mais... tente novamente.")
#         elif jogador > computador:
#             print("menos... tente novamente.")
# print(f"Acertou com {palpites} tentativas. PARABÉNS!!")

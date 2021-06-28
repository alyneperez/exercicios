# Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer 
# e peça para o usuário escolher qual será a base de conversão: 
# 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input("Digite um número inteiro: "))
escolha = int(input("Escolha o tipo de conversão: 1-BINÁRIO 2-OCTAL 3-HEXADECIMAL "))
if escolha == 1:
    print(f"Número {num} convertido para BINÁRIO:{bin(num)[2:]} ")
elif escolha == 2:
    print(f"Número {num} convertido para OCTAL:{oct(num)[2:]} ")
elif escolha == 3:
    print(f"Número {num} convertido para HEXADECIMAL:{hex(num)[2:]} ")
else:
    print("Você escolheu uma opção inválida, por gentileza, tente novamente.")

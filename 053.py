# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. 
# Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = input("Digite uma frase para verificar se é um palíndromo: ").strip()
invertida = (frase[::-1])

print(f"""Você digitou a frase: {frase}.
Ao contrário seria: {invertida}""")

if frase == invertida:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")

#Outra Solução:

# frase = str(input("Digite uma frase: ")).strip().upper()
# f = frase.split()
# j = "".join(f)
# if j == j[::-1]:
#     print(f"A frase {j} ao contrário é {(j[::-1])} \n > A frase é um palídromo!")
# else:
#     print(f"A frase {j} ao contrário é {(j[::-1])} \n > A frase não é um palídromo!")

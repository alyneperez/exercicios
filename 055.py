# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. 
# No final, mostre qual foi o maior e o menor peso lidos.

pesos = [float(input("Digite os pesos: KG ")) for peso in range(0,5)]
print(f"Os pesos digitados foram: {pesos}")
print(f"O maior peso é: {max(pesos)} e o menor é {min(pesos)}")

#Outra Solução

# maior = 0
# menor = 0
# for p in range(1,6):
#     peso = float(input(f"Peso da {p}ª pessoa: "))
#     if p == 1:
#         maior = peso
#         menor = peso
#     else:
#         if peso > maior:
#             maior = peso
#         if peso < menor:
#             menor = peso
# print(f"O maior peso lido foi de {maior:.1f}kg")
# print(f"O menor peso lido foi de {menor:.1f}kg")

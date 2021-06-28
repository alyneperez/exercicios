# Exercício Python #032 - Ano Bissexto - Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input("Digite um ano para descobrir se o mesmo é bissexto ou não: "))
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano de {ano} é um ano BISSEXTO.")
else:
    print(f"O ano de {ano} NÃO é um ano bissexto.")

#Outra Solução:

# from datetime import date
# ano = int(input("Que ano quer analisar? Coloque 0 para analisar o ano atual: "))
# if ano == 0:
#     ano = date.today().year
# if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#     print(f"O número {ano} é BISSEXTO")
# else:
#     print(f"O número {ano} é NÃO É BISSEXTO")  

# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import datetime
# import ipdb

#lê a entrada de anos e transforma em lista de str
anos_nasc = input("Digite os anos de nascimento: [insira na mesma linha separando por espaço] ").split(' ') 

#pegando o ano atual
ano_atual = datetime.date.today().year

#utilizando list comprehensions, transforma a string em inteiro, verifica se é maior de idade e soma os booleanos
# ipdb.set_trace()
maior_de_idade = sum([(ano_atual - int(ano)) >= 18 for ano in anos_nasc])

#calcula a diferença entre a quantidade de pessoas e a quantidade de maiores de idade
menor_de_idade = len(anos_nasc) - maior_de_idade

print(f"Há {maior_de_idade} maiores de idade e {menor_de_idade} pessoas menores de idade.")

#Outra Solução

# from datetime import date
# atual = date.today().year
# contmaior = 0
# contmenor = 0
# for c in range(1,8):
#     nasc = int(input("Digite seu ano de nascimento: ").strip())
#     idade = atual - nasc
#     if idade >= 18:
#         contmaior = contmaior + 1 
#     else:
#         contmenor = contmenor + 1 
# print(f"Você informou {contmaior} pessoas MAIORES de idade.")
# print(f"Você informou {contmenor} pessoas MENORES de idade.")

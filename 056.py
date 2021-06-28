# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: 
# a média de idade do grupo, 
# qual é o nome do homem mais velho 
# e quantas mulheres têm menos de 20 anos.

soma_idade = 0
media_idade = 0
mulher_20menos = 0
homem_velho = 0
nome_velho = None
for p in range(1,5):
    print(f"Insira os dados da {p}a pessoa: ")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo: [F]Feminino ou [M]Masculino ").upper()
    soma_idade = soma_idade + idade
    media_idade = soma_idade / 4
    if idade <= 19 and sexo == "F":
        mulher_20menos = mulher_20menos + 1
    if sexo == "M":
        if idade > homem_velho:
            homem_velho = idade
            nome_velho = nome
print(f"a média das idades é de {media_idade:.0f} anos.")
print(f"Existem {mulher_20menos} mulheres com menos de 20 anos")
print(f"O nome do homem mais velho é {nome_velho}")

#Outrasolução

# Joana 24 F,Ana 28 F,Alan 25 M,Victor 32 M,Vilma 26 F

# print("Formato: nome idade sexo, nome idade sexo")
# print("F para sexo feminino M para Masculino")
# dados = input("Insira os dados: ").split(",")
# # print(dados)

# pessoas = []

# for dado in dados:
#     # import ipdb;ipdb.set_trace()
#     d = dado.split(" ")
#     # print(d)
#     p = {
#         "nome": d[0],
#         "idade": int(d[1]),
#         "sexo": d[2]
#     }
#     pessoas.append(p)
# # print(pessoas)

# media = 0
# mulheres = 0
# idade_homem = 0
# nome_homem = None

# for p in pessoas:
#     media = media + p['idade']
#     if p['sexo'] == 'F' and p['idade'] <= 19:
#         mulheres = mulheres + 1
#     if p['sexo'] == 'M':
#         if p['idade'] > idade_homem:
#             idade_homem = p['idade']
#             nome_homem = p['nome']

# media = media / len(pessoas)
# print(f"A média de idade é {media}.")
# print(f"Existem {mulheres} menores de 20 anos.")
# print(f"{nome_homem} é o nome do homem mais velho.")

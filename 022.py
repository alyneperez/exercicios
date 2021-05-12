# Exercício Python #022 – Analisador de textos

#Crie um programa que leia o nome completo de uma pessoa e mostre:
#• O nome com todas as letras maiúsculas
#• O nome com todas minúsculas
#• Quantas letras ao todo (sem considerar os espaços)
#• Quantas letras tem o primeiro nome

nome = input("Digite seu nome completo: ").strip()
nome = nome.upper()
print(f"Em maiúsculas: {nome}")
nome = nome.lower()
print(f"Em minúsculas: {nome}")
print (f"Quantidade de letras no nome todo: ",(len(nome) - nome.count(' ')))
div = nome.split()
print("Quantidade de letras primeiro nome: ",(len(div[0])))

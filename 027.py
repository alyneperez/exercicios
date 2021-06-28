# Exercício Python #027: Primeiro e último nome de uma pessoa

# # Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome separadamente.
# Ex: Ana Maria de Souza
# Primeiro: Ana
# Último: Souza

nome_completo = input("Digite seu nome completo: ")
print(nome_completo)
dividido = nome_completo.split()
print(f"O primeiro nome é {(dividido[0])} e o último é {dividido[-1]}")

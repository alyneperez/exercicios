# Exercício Python #025: Procurando uma string dentro de outra

# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = input("Qual seu nome completo? ").strip()
print(f"Seu nome tem Silva? {'silva' in nome.lower()}")

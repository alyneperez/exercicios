# Exercício Python #026: Primeira e última ocorrência de uma string

# Faça um programa que leia a frase pelo teclado e mostre:
    # • Quantas vezes aparece a letra “A”
    # • Em que posição ela aparece a primeira vez
    # • Em que posição ela aparece a última vez

frase = input("Digite uma frase: ").strip()
print(f"A frase digitada foi: {frase}")
print(f"A letra A aparece: {frase.lower().count('a')} vezes.")
print(f"A letra A aparece a primeira vez em: {frase.lower().find('a')}")
print(f"A letra A aparece pela última vez em: {frase.lower().rfind('a')}")

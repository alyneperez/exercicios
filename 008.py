# Exercício Python #008 - Conversor de Medidas

# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros. 

metro = float(input("Digite um valor em metros para ser convertido em cm e mm: "))
print(f"Você digitou {metro:.1f} metro(s), vale {metro * 100:.0f} centímetros e {metro * 1000:.0f} milímetros.")

# Outra solução:

# metro = float(input("Digite o valor em metros: "))
# centimetro = metro * 100
# milimetro = metro * 1000
# print(f"O valor de {metro}m é igual a {centimetro:.0f}cm e a {milimetro:.0f}mm.")

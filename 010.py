# Exercício Python #010 - Conversor de Moedas

# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos doláres ela pode comprar. 
# (Considere USD 1.00 = R$ 3.27)

real = float(input("Digite o valor a ser convertido em dólar: R$ "))
print(f"R${real :.2f} = US${real / 3.27:.2f}")

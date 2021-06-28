# Exercício Python #012 - Calculando Descontos

# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

produto = float(input("Digite o valor do produto: R$ "))
print(f"O produto custa R${produto:.2f} e terá um desconto de 5%, seu preço final será R${produto - (produto * 5) /100:.2f}")

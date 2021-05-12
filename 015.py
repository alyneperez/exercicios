# Exercício Python #015 - Aluguel de Carros

# Escreva um programa que pergunte a quantidade  de km percorridos por um carro alugado 
# e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

km = float(input("Insira a quantidade de km percorridos: km "))
dias = float(input("Digite a quantidade de dias em que o veículo foi alugado: "))
total = (km * 0.15) + (dias * 60)
print(f"O veículo foi alugado por {dias:.0f} dias e rodou {km:.1f}km TOTAL: R${total:.2f}")

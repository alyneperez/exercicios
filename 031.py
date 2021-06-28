# Exercício Python #031 - Custo da Viagem

# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input("Insira a distância que será percorrida: km "))
if distancia <= 200:
    print(f"A viagem terá uma distância de {distancia:.1f}km, totalizando R${distancia * 0.50:.2f}.")
else:
    print(f"A viagem terá uma distância de {distancia:.1f}km, totalizando R${distancia * 0.45:.2f}.")

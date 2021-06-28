# Exercício Python #029 - Radar eletrônico

# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input("Insira a velocidade atual do veículo: km/h "))
if velocidade >= 80:
    multa = (velocidade - 80) * 7
    print(f"Você está dirigindo acima da velocidade permitida de 80km/h. O veículo está sendo multado! MULTA: R${multa}")
else:
    print("Você está andando na velocidade permitida. Faça uma boa viagem!!")

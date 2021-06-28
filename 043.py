# Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))
imc = peso / (altura * altura)

print(f"Você tem {altura}m de altura e pesa {peso}kg: IMC = {imc:.0f}")

if imc < 18.4:
    print("Abaixo do peso")
elif imc <= 24.9:
    print("Peso Ideal")
elif imc <= 29.9:
    print("Sobrepeso")
elif imc <= 39.9:
    print("Obesidade")
else:
    print("Obesidade mórbida")


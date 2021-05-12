# Exercício Python #014 - Conversor de Temperaturas

#Escreva um programa que converta uma temperatura de digitada de °C e converta para °F.

# (°C × 9/5) + 32 = 41 °F formula #

temperatura = float(input("Insira a temperatura em graus celsius: "))
conversao = (temperatura * 9/5) + 32
print(f"{temperatura:.0f}°C = {conversao:.0f}°F")

# Exercício Python #034 - Aumentos múltiplos
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Digite o valor de seu salário para calcular o aumento: R$ ").strip())
print(f"O valor atual do salário é de R${salario:.2f}")
if salario > 1250:
    print(f"Você terá um aumento de 10%, igual a R${salario * 10/100:.2f} Totalizando R$ {salario + (salario * 10/100):.2f}")
else:
    print(f"Você terá um aumento de 15%, igual a R${salario * 15/100:.2f} Totalizando R$ {salario + (salario * 15/100):.2f}")

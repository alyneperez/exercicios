# Exercício Python #013 - Reajuste Salarial

# Faça um programa que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

salario = float(input("Digite o salário: R$" ))
aumento = (salario * 15) / 100
print(f"O funcionário recebia um salário de R${salario:.2f} e após aumento de 15%({aumento}) deverá receber R${salario + aumento:.2f}")

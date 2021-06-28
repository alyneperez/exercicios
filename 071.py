# EXERCÍCIO 071: Simulador de Caixa Eletrônico
# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
# usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
# cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.

print(" = " * 30)
print(f'{"BANCO PEREZ":^30}')
print(" = " * 30)
valor = int(input("Qual valor você quer sacar? R$ "))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f"Total de {totced} cédulas de R$ {ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print(" = " * 30)
print("Volte sempre ao BANCO PEREZ! Tenha um bom dia!")

#Outra Solução

# print("=*="*5)
# print("BANCO PEREZ")
# print("=*="*5)
# print("Limite mínimo R$1 e máximo R$1000")

# valor = int(input("Quanto deseja sacar? R$ "))

# uni = (valor // 1 % 10)
# dez = (valor // 10 % 10)
# cen = (valor // 100 % 10)

# if uni > 0 and uni <= 9:
#     print(f"{uni} notas de 1 REAL")

# if dez > 0 and dez <= 10 and valor != 20 and valor != 50 and valor != 60:
#     print(f"{dez} notas de 10 REAIS")
        
# if valor == 20:
#     print(f"1 nota de 20 REAIS")

# if valor == 50:
#     print(f"1 nota de 50 REAIS")
        
# if valor == 60:
#     print(f"3 notas de 20 REAIS") 

# if valor >= 100 and valor < 1000:
#     print(f"{(cen * 2)} notas de 50 REAIS")

# if valor == 1000:
#     print("20 notas de 50 REAIS")

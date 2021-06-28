# Exercício Python 070: Estatísticas em Produtos
# Crie um programa que leia o nome e o preço de vários produtos. O programa
# deverá perguntar se o usuário vai continuar. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$ 1000.
# C) Qual é o nome do produto mais barato.

total = maior1000 = maisbarato = cont = 0
barato = " "
while True:
    print("~INSIRA OS DADOS DO(S) PRODUTO(S)~")
    produto = input("PRODUTO: ").lower()
    preco = float(input("PRECO: R$"))
    resp = input("DESEJA CONTINUAR? S/N ").lower()  
    cont += 1
    if resp == "s":
        total += preco
        if preco > 1000:
            maior1000 += 1
    if cont == 1 or preco < maisbarato:
        maisbarato = preco
        barato = produto
    if resp == "n":
        total += preco
        break
        if preco > 1000:
            maior1000 += 1
print(f"~OBRIGADO! TOTAL DAS COMPRAS R$: {total:.2f}~")
print(f"Temos ao todo, {maior1000} produto(s) que custa(m) acima de R$1000.00")
print(f"O produto mais barato foi {barato}, custando R$ {maisbarato:.2f}")

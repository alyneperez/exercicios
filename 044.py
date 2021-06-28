# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

preco_inicial = float(input("Insira o valor inicial do produto: R$ "))

print(f"O produto custa R${preco_inicial:.2f}")
print("""ESCOLHA A FORMA DE PAGAMENTO: 
    [ 1 ] à vista dinheiro/cheque
    [ 2 ] à vista no cartão
    [ 3 ] Cartão parcelado """)

condicao_pgto = int(input("Qual será a condição de pagamento? "))

if condicao_pgto == 1:
    print(f"Você terá 10% de desconto. TOTAL: R${preco_inicial - (preco_inicial * 10/100):.2f}")
elif condicao_pgto ==2:
    print(f"Você terá 5% de desconto. TOTAL: R${preco_inicial - (preco_inicial * 5/100):.2f}")
elif condicao_pgto == 3:
    print("Em quantas vezes vc gostaria de parcelar? ")
    parcelamento = int(input("Digite a quantidade: "))
    if parcelamento <= 2:
        print(f"Preço formal.TOTAL: R${preco_inicial}")
    elif parcelamento >=3:
        print(f"Você terá 20% de juros. TOTAL: R${preco_inicial + (preco_inicial * 20/100):.2f}")
else:
    print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE.")

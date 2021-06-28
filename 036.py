# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_imovel = float(input("Digite o valor do imóvel que deseja adquirir: R$ "))
salario_comprador = float(input("Digite o valor de seu salário: R$ "))
prazo = int(input("Digite o prazo desejado: anos "))
parcela = valor_imovel / (prazo * 12)
print(f"O imóvel desejado custa R${valor_imovel:.2f} e o prazo desejado é de {prazo:.0f} anos.")
if parcela > (salario_comprador * 30/100):
    print("Empréstimo NEGADO! O valor da pmt ultrapassa 30% do salário informado.")
else:
    print(f"EMPRÉSTIMO APROVADO! O valor da parcela ficará em {prazo * 12}x de R${parcela:.2f}.")

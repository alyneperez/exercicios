# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#  No final, mostre quantos números foram digitados e qual foi a soma entre eles 
#  (desconsiderando o flag).

num = qtd = soma = 0
while num != 999:
    num = int(input("Digite um número [999 finaliza]: "))
    if num != 999:
        qtd += 1
        soma += num
print(f"Você digitou {qtd} números e a soma entre eles é {soma}")

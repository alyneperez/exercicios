# # Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. Mostrando na tela uma mensagem:
# # - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais.

primeiro = int(input("Digite um número inteiro: "))
segundo = int(input("Digite outro: "))
print(f"Os números digitados foram {primeiro} e {segundo}.")
if primeiro > segundo:
    print(f"O número {primeiro} é MAIOR que o número {segundo}")
elif segundo > primeiro:
    print(f"O número {segundo} é MAIOR que o número {primeiro}")  
else:
    print("Não existe valor maior, os dois números são IGUAIS!!")

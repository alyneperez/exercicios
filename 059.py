# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))

opcao = 0
while opcao != 5:
    print(""" Escolha:

    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA \n """)

    opcao = int(input("Digite sua opção: "))

    if opcao == 1:
        print(f"{n1} + {n2} = {(n1 + n2)}")
    elif opcao == 2:
        print(f"{n1} x {n2} = {(n1 * n2)}")
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print(f"{n1} é MAIOR que {n2}.")
        elif n2 > n1:
            maior = n2
            print(f"{n2} é MAIOR que {n1}.")
        else:
            print("Os números são iguais.")
    elif opcao == 4:
        n1 = int(input("Insira o primeiro número: "))
        n2= int(input("Insira o segundo número: "))

    elif opcao == 5:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")

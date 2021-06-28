# Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, 
# de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

num = int(input("Digite um número de 0 a 20 para ver sua versão em extenso: "))

extenso = ("zero", "um", "dois", "três", "quatro", "cinco",
        "seis", "sete", "oito", "nove", "dez", 
        "onze", "doze", "treze", "catorze", "quinze",
        "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

print(f"Você digitou o número {num}... \nEm extenso fica: {(extenso[num])}")

#Outra Solução:

# cont = ('zero', 'um', 'dois', 'três', 'quatro',
#         'cinco', 'seis', 'sete', 'oito', 'nove',
#         'dez', 'onze', 'doze', 'treze', 'catorze',
#         'quinze', 'dezesseis', 'dezessete', 'dezoito',
#         'dezenove', 'vinte')
# while True:
#     num = int(input('Digite um número entre 0 e 20: '))
#     if 0 <= num <= 20:
#         break
#     print('Tente novamente. ', end='')
# print(f'Você digitou o número {cont[num]}')
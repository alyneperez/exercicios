# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import sample

numeros = tuple((sample(range(0, 11), 5)))

print(f"Os números gerados foram: {numeros}")
print(f"O array é do tipo {type(numeros)}")
print(f"O maior número é {max(numeros)} e o menor é {min(numeros)}.")

#Outra Solução:

# from random import randint
# numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
#            randint(1, 10), randint(1, 10))
# print('Os valores sorteados foram: ', end='')
# for n in numeros:
#     print(f'{n} ', end='')
# print(f'\nO maior valor sorteado foi {max(numeros)}')
# print(f'O menor valor sorteado foi {min(numeros)}')

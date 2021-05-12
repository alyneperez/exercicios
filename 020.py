# Exercício Python #020 – Sorteando uma ordem na lista

# O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. (ordem de apresentação)

import random
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")
lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.sample(lista, k=4)
print("A ordem de apresentação será: ", sorteio)

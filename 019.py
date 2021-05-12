# Exercício Python #019 – Sorteando um item na lista

# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
aluno_1 = input("Insira o nome do 1º aluno: ")
aluno_2 = input("Insira o nome do 2º aluno: ")
aluno_3 = input("Insira o nome do 3º aluno: ")
aluno_4 = input("Insira o nome do 4º aluno: ")
lista = [aluno_1, aluno_2, aluno_3, aluno_4]
sorteio = random.choice(lista)
print("O aluno escolhido para apagar a lousa é:", sorteio)

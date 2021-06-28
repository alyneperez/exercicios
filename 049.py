# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, 
# só que agora utilizando um laço for.

num = int(input("Insira um número para ver sua tabuada: "))
print("=-=" * 6)
print("T A B U A D A ")
print("=-=" * 6)

for n in range(0, 11):
    print(f"{num} x {n:2} = {num * n}")

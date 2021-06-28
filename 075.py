# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
# No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

valores = tuple(int(input("Digite valores: "))for c in range(1, 5))
print(f"O numero nove aparece {valores.count(9)} vezes")
print(f"O valor 3 foi digitado pela primeira vez na {valores.index(3)+1}º posição" if 3 in valores else "Não foi digitado valor 3")
print("Valores pares digitados foram", end=" ")
print({n for n in valores if n % 2 == 0}, end=" ")

#outra Solução

# num = (int(input("Digite um número: ")),
#        int(input("Digite outro número: ")),
#        int(input("Digite mais um número: ")),
#        int(input("Digite o último número: ")))
# print(f"Você digitou os valores {num}")
# print(f"O valor 9 apareceu {num.count(9)} vezes")
# if 3 in num:
#     print(f"O valor 3 apareceu na {num.index(3)+1}ª posição")
# else:
#     print("O valor 3 não foi digitado em nenhuma posição")
# print("Os valores pares digitados foram ", end=" ")
# for n in num:
#     if n % 2 == 0:
#         print(n, end=" ")

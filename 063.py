# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer 
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
# Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
        
n = int(input('Exibir ate o termo (maior que 2): '))
# print(fibo(n))
for val in range(0,n):
    print(fibo(val), end=" ")

#Outra Solução:

# n = int(input("Quantos termos você quer mostrar? "))
# print("-" * 30)
# print("SEQUENCIA DE FIBONACCI")
# t1 = 0
# t2 = 1
# print("-" * 30)
# print(f"{t1} → {t2} " , end=" ")
# cont = 3
# while cont <= n: 
#     t3 = t1 + t2
#     print(f" → {t3}", end=" ")
#     t1 = t2
#     t2 = t3
#     cont += 1
# print("→ FIM")
# print("-" * 30)

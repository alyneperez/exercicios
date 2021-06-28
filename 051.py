# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#  No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input("Primeiro elemento: "))
razao = int(input("Razao: "))
n = 10

ultimo = primeiro + (n-1)*razao
ultimo = ultimo + 1

for i in range(primeiro, ultimo, razao):
    print(i, end=" ")

#Outra Solução

# print("=" * 20)
# print("10 TERMOS DE UMA P.A.")
# print("=" * 20)
# primeiro = int(input("Primeiro termo: "))
# razao = int(input("Razão: "))
# decimo = primeiro + (10 -1) * razao
# for c in range(primeiro, decimo + razao, razao):
#     print(f"{c}",end="→ ")
# print("FIM") 

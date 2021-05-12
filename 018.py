# Exercício Python #018 – Seno, Cosseno e Tangente 

# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. (modulo)

import math
angulo = int(input("Digite o angulo que vc deseja: "))
seno = math.sin(math.radians(angulo))
print(f"O ângulo de {angulo} tem o SENO de {seno:.2f}")
cosseno = math.cos(math.radians(angulo))
print(f"O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}")
tangente = math.tan(math.radians(angulo))
print(f"O ângulo de {angulo} tem a TANGENTE de {tangente:.2f}")

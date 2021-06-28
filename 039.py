# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com a sua idade, 
# se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar 
# ou se já passou do tempo do alistamento. 

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime

ano_nasc = int(input("Digite o ano de seu nascimento: "))
ano_atual = datetime.date.today().year
idade = ano_atual - ano_nasc
diferenca_maior = idade - 18 
diferenca_menor = 18 - idade
print(f"Você nasceu no ano de {ano_nasc} e atualmente possui {idade} anos.")
if idade < 18:  
    print(f"Você ainda irá se alistar. Faltam {diferenca_maior} anos.")
elif idade == 18:
    print("Você está na hora exata de se alistar. Faça seu agendamento o quanto antes!")
else:
    print(f"Já passou o tempo de seu alistamento. Deveria ter feito há {diferenca_menor} anos atrás.")

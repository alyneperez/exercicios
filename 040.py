# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
#  mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

nota_1 = float(input("Insira a primeira nota: "))
nota_2 = float(input("Insira a segunda: "))
media = (nota_1 + nota_2) / 2
print(f"Primeira nota:{nota_1} e Segunda nota: {nota_2}")
print(f"Sua média:{media:.1f}")

if media < 4.9:
    print("REPROVADO")

elif media <= 6.9:
    print("RECUPERAÇÃO")

else:
    print("APROVADO")

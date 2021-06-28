# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
#  Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input("Informe seu sexo: [M/F] ").strip().upper()[0]       
while sexo not in "MmFf":
    sexo = input("Dados inválidos. Por favor, informe novamente. ").strip().upper()[0]
print(f"Sexo {sexo} registrado com sucesso!")

#Outra Solução

# r = "M" or "F"
# while r == "M" or "F":
#     r = str(input("Qual seu sexo? [M/F] ")).upper()   #eu fiz 
#     if r == "M":
#         print("Você é do sexo masculino.")
#         break
#     elif r == "F":
#         print("Você é do sexo feminino.")
#         break
#     else:
#         print("Vocẽ digitou uma opção inválida, tente novamente.")
# print("Dados cadastrados, obrigado!!")

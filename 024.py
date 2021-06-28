# Exercício Python #024: Verificando as primeiras letras de um texto

# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome “SANTO”

cid = str(input("Em que cidade vc nasceu? ")).strip()
print(cid[:5].upper() == "SANTO")

# Exercício Python #011 - Pintando Parede

# Faça um programa que leia a altura e a largura de uma parede em metros, 
# calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².


altura  = float(input("Digite o valor da altura em metros: "))
largura = float(input("Digite a largura: "))
area = altura * largura
rendimento = area / 2
print(f"A parede possui a area de {area:.1f}m2 e por tanto precisaremos de {rendimento:.1f}l de tinta para pintá-la.")

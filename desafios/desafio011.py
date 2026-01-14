# Crie um programa que leia a largura e a
# altura de uma parede em metros, calcule
# a sua área e a quantidade de tinta necessária
# para pintá-la, sabendo que cada litro de tinta
# pinta uma área de 2m2

print('Desafio 11')
print('Programa para calcular quantidade de tinta necessária para pintar uma parede.')
print('Considere 1 litro de tinta para uma área de 2 metros quadrados.')
l = float(input('Qual a largura da parede: '))
a = float(input('Qual a altura da parede: '))
area = l * a
litro = area / 2
print('Será necessário {} litros de tinta para pintar {} metros quadrados de parede.'.format(litro, area))

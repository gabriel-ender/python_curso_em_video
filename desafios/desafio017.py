#Faça um programa que leia o comprimento do cateto oposto e do cateto
#adjacente de um triângulo retângulo, calcule e mostre o comprimento da
#hipotenusa.

from math import hypot

#Forma bruta de fazer. Usando calculos.
print('Desafio 17')
print('Programa que calcula o comprimento da hipotenusa num triângulo retângulo.')
co = float(input('Qual a medida em CM do cateto oposto: '))
ca = float(input('Qual a medida em CM do cateto adjacente: '))
h = (co ** 2 + ca ** 2) ** (1/2)
print('O comprimento da hipotenusa é {:.2f}'.format(h))

#Forma de fazer usando biblioteca MATH
h1 = hypot(co, ca)
print('O comprimento da hipotenusa é {:.2f}.'.format(h1))
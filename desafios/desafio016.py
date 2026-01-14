# Crie um programa que leia um número Real qualquer pelo teclado
# e mostre na tela a sua porção inteira. Ex: 6,158 = 6.

from math import trunc

print('Desafio 16')
print('Programa que permite mostrar na tela a porção inteira de um número Real.')
n = float(input('Digite um número Real: '))
print(f'O número {n} tem a parte inteira {trunc(n)}.')

#Pode ser feito também com (int) sem importar nenhuma biblioteca.

print(f'O número {n} tem a parte inteira {int(n)}.')
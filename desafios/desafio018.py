#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno
#cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

print('Desafio 18')
print('Programa que calcula seno, cosseno e tangente de um ângulo.')
angulo = float(input('Qual o ângulo que você deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('Com o ângulo de {:.2f}, o Seno é {:.2f}, o Cosseno é {:.2f} e a tangente é {:.2f}'.format(angulo, seno, cosseno, tangente))

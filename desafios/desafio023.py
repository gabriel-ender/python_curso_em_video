#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#EX: 1834
#unidade 4, dezena 3, centena 8 e milhar 1.

print('Desafio 23')
numero = int(input('Digite um número inteiro de 0 a 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Analisando o número {}.'.format(numero))
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(u, d, c, m))




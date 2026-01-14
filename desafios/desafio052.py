# Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.
print(f'{'=':=^40}')
print(f'{'Identificador de Números Primos': ^40}')
print(f'{'=':=^40}')
n = int(input('Digite um número: '))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        cont += 1
        print(c, end=' ')
print(f'\nO número {n} foi divisível {cont} vezes.')
if cont == 2:
    print('O número é PRIMO!')
else:
    print('O número NÃO É PRIMO!')
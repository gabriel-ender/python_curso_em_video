# Desafio 047 - Crie um programa que mostre na tela todos os números pares que estão
# no intervalo entre 1 e 50.

from time import sleep

print('Programa que mostra na tela todos os números pares entre 1 e 50.')
for c in range(2, 51, 2):
    print(c, end=' ')
    sleep(0.5)

#outro metodo
for c in range(1, 51):
    if c % 2 == 0: print(c, end=' ')


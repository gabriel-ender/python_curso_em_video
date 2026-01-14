# Faça um programa que calcule a soma de todos os numeros ímpares que são multiplos de 3
# e que se encontram no intervalo de 1 até 500.

print('Programa que calcula soma de todos os números ímpares, multiplos de 3 de 1 à 500.')
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'A soma dos {cont} valores solicitados é: {soma}')


# Desenvolva um programa que leia 6 números inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.

soma = 0
cont = 0
for c in range(1, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'Existem {cont} números PARES e a soma deles é {soma}')

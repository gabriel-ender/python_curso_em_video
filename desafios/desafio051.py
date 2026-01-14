# Desenvolva um programa que leia o primeiro termo e a razão
# de uma PA. No final, mostre os 10 primeiros termos dessa regressão.
print(f'{"Progressão Aritmética":=^40}')
ptermo = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
decimo = ptermo + (10 - 1) * razao
for c in range(ptermo, decimo + razao, razao):
    print(c, end='-')
print('FIM')

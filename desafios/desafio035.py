# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
# se elas podem ou não formar um triângulo.

print('Desafio 35')
print('Programa que identifica se 3 retas podem formar um triângulo.')
r1 = float(input('Primeiro Segmento (cm): '))
r2 = float(input('Segundo Segmento (cm): '))
r3 = float(input('Terceiro Segmento (cm): '))

# Regra para formar um triângulo: a soma das medidas de 2 retas devem ser maior que
# a medida da 3 reta.

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os Segmentos acima PODEM formar um triângulo!')
else:
    print('Os Segmentos acima NÃO PODEM formar um triângulo!')
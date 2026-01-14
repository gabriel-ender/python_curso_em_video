# Escreva um programa que converta uma temperatura digitada
# em ºC para ºF.

print('Desafio 14')
print('Conversor de temperaturas: ºC -> ºF ')
c = float(input('Digite a temperatura em ºC: '))
f = (c * 9/5) + 32
print('A temperatura de {:.2f}ºC equivale a {:.2f}ºF'.format(c, f))

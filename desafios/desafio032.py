# Faça um programa que leia um ano qualquer e diga se ele é BISSEXTO.

ano = int(input('Digite um ano: '))
if ano % 4 == 0 and ano % 4 != 0 or ano % 400 == 0:
    print('O ano é BISSEXTO')
else:
    print('O ano NÃO é BISSEXTO!')
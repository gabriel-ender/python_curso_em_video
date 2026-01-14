# Faça um programa que leia algo pelo teclado e mostre
# na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele. É numérico, é alfabético, é caps? Etc.

print('<<<Desafio 04>>')
print('Vamos descobrir qual tipo primitivo e demais características desse número.')
a1 = input('Digite qualquer coisa:  ')
print('É numérico? ', a1.isnumeric())
print('É texto? ', a1.isalpha())
print('Está em maiúsculo? ', a1.isupper())
print('É alphanumérico? ', a1.isalnum())

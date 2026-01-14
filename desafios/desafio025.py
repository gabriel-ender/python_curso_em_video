#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

print('Desafio 25')
nome = str(input('Qual o seu nome completo: ')).strip()
print('Seu nome tem Silva? ')
print('SILVA' in nome.upper())
#Faça um programa que leia o nome completo de uma pessoa mostrando
#em seguida o primeiro e o último nome separadamente.

print('Desafio 27')
nome = str(input('Digite seu nome completo: '))
print(nome)
lista = nome.split()
print('Muito prazer {}!'.format(lista[0]))
print('Seu último nome é: {}.'.format(lista[-1]))

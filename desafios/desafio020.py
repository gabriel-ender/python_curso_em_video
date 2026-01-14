#O mesmo professor do desafio 19 quer sortear a ordem de apresentação
#de trabalhos dos alunos. Faça um programa que leia o nome dos quatros
#alunos e mostre a ordem sorteada.

import random

print('Desafio 20')
print('Programa que sorteia ordem de apresentação dos alunos.')

n1 = input('Digite o 1º nome: ')
n2 = input('Digite o 2º nome: ')
n3 = input('Digite o 3º nome: ')
n4 = input('Digite o 4º nome: ')

l1 = [n1, n2, n3, n4]
random.shuffle(l1)
print(l1)

#Resolução do Guanabara.
# Eu criei uma variável (l1r = random.shuffle(l1)) para dar shuffle sendo que não precisa.
# Então fica assim random.shuffle(l1)
# Sempre simplificar as importações.


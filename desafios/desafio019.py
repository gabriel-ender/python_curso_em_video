#Um professor quer sortear um dos seus quatro alunos para apagar o quadro
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome
#do escolhido.

import random

print('Desafio 19')
print('Programa que escolhe um nome aleatório para apagar o quadro.')

n1 = input('Qual o nome do 1º aluno: ')
n2 = input('Qual o nome do 2º aluno: ')
n3 = input('Qual o nome do 3º aluno: ')
n4 = input('Qual o nome do 4º aluno: ')

l1 = [n1, n2, n3, n4]

nome = random.choice(l1)

print(f'Os nomes foram:\n{n1}\n{n2}\n{n3}\n{n4}')
print('E o escolhido foi {}!'.format(nome))


#Resolução do Guanabara.

# Exatamente igual a que fiz, somente reduziu a importação.

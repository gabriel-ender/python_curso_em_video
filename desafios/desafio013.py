# Faça um programa que leia o salário de um funcionário e mostre seu novo
# salário com 15% de aumento.

print('Desafio 13')
print('Calculando um aumento de 15% no salário do funcionário.')
s1 = float(input('Qual o salário atual: '))
s2 = s1 + (s1 * 15 / 100)
print('O salário após 15% de aumento é: R${}'.format(s2))

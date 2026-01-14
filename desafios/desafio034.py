# Escreva um programa que pergunte o salário de um funcionário e calcule o valor
# do seu aumento. Para salários superiores a R$ 1.250,00 aumento de 10%.
# Para salários inferiores, aumento de 15%.

print('Desafio 34')
print('Calculando aumento do salário.')
print('Salários até R$ 1.250,00 = Aumento de 15%.\nSalários superiores a R$ 1.250,00 = Aumento de 10%.')
salario = float(input('Qual o salário do funcionário: R$ '))
if salario > 1250:
    nsalario = salario + (salario * 10 / 100)
else:
    nsalario = salario + (salario * 15 / 100)
print('O novo salário é R$ {:.2f}'.format(nsalario))

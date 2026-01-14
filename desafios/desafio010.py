# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
# mostre quantos dólares ela pode comprar.

print('Desafio010')
print('Programa que calcula quantos dólares você pode comprar.')
r = float(input('Quantos reais você tem: '))
c = float(input('Qual a cotação do dolar no momento: '))
d = r / c
print('Você pode comprar U$ {:.3} '.format(d))


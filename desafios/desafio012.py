# Faça um algoritmo que leia o preço de um produto e mostre seu novo
# preço com 5% de desconto.

print('Desafio 12')
print('Programa pra saber novo preço do produto com 5% de desconto.')
p = float(input('Qual o preço do produto: '))
d = p - (p * 5 / 100)
print('O valor do produto com 5% de desconto é: R$ {}'.format(d))

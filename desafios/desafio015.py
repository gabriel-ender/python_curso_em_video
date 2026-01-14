# Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi
# alugado. Calcule o preço a pagar, sabendo que o carro custa
# R$ 60 por dia e R$0,15 por Km rodado.

print('Desafio 15')
print('Programa que permite calcular preço do carro alugado.')
d = int(input('Quantos dias o carro foi alugado: '))
km = float(input('Quantos Km foram rodados: '))
p = (d * 60) + (km * 0.15)
print('Custo total do aluguel: R$ {:.2f}'.format(p))


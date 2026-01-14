# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200 Km.
# E R$ 0,45 para viagens mais longas.

print('Desafio 31')
print('PREÇO DA PASSAGEM')
km = float(input('Quantos Km de distância tem seu destino? '))
if km > 200:
    p = (km * 0.45)
else:
    p = (km * 0.50)
print('Preço da passagem: R$ {:.2f}'.format(p))

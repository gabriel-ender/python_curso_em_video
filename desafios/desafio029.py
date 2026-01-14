# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
# 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite.
from time import sleep

print('=' * 20)
print('Radar de velocidade'.upper())
print('=' * 20)
v = int(input('Qual a velocidade do carro: '))
e = v - 80  # Fórmula para a velocidade que foi excedida da permitida.
m = e * 7   # Preço da multa pela velocidade excedida.
if v > 80:
    print('VOCÊ FOI MULTADO! Velocidade atual {}Km/h.'.format(v))
    sleep(2)
    print('Velocidade MÁXIMA permitida 80Km/h')
    sleep(2)
    print('Calculando preço da Multa...')
    sleep(3)
    print('A multa foi de R${:.2f}'.format(m))
else:
    print('======\n{}Km/h\n======'.format(v))
    print('Velocidade dentro do permitido (80Km/h).')
print('Boa viagem!')
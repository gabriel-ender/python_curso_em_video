# Crie um programa que faça o computador jogar Jokenpô com você.
from time import sleep
import random
print(f'{"Jogo de Jokenpô":#^40}')
print('[ 0 ] - PEDRA')
print('[ 1 ] - PAPEL')
print('[ 2 ] - TESOURA')
jogador = int(input('Qual a sua OPÇÃO:'))
itens = ('Pedra', 'Papel', 'Tesoura')
pc = random.randint(0, 2)
sleep(0.5)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
sleep(1)
print('O computador escolheu {}!'.format(itens[pc]))
print('O jogador escolheu {}!'.format(itens[jogador]))
if pc == 0: #Computador Pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
elif pc == 1: #Computador Papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR GANHA')
elif  pc == 2: #Computador Tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')


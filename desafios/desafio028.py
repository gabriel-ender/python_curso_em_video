#Escreva um programa que faça o computador "pensar" em um número inteiro
#entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
#escolhido pelo computador. O programa deverá escrever na tela se o usuário
#venceu ou perdeu.
from random import randint
from time import sleep

print('-=-' * 19)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 19)
nc = randint(0, 5) #Computador "Pensando".
n = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar.
print('PROCESSANDO...')
sleep(2)
if n == nc:
    print(f'Parabéns, eu pensei mesmo no número {n}.')
    print('Você conseguiu me VENCER!')
else:
    print(f'Que pena, você errou. Eu pensei no número {nc} e não no número {n}.')

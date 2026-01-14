# Melhore o jogo do DESAFIO 028 onde o computador vai pensar em um número
# entre 0 e 10.
# Só que agora o jogador vai tentar até acertar.
# Mostrar no final quantos palpites foram necessários para vencer.

# Minha resposta.

from random import randint
from time import sleep

# computador = randint(0, 10)
# chance = 1
# jogador = int(input("Qual número o computador pensou? 0 à 10: ").strip())
# sleep(1)
# while computador != jogador:
#     jogador = int(input("Número errado. Tente novamente: ").strip())
#     sleep(1)
#     chance += 1
# print("Parabéns, você ACERTOU.")
# sleep(1)
# print(f"O número escolhido pelo computador foi {computador}")
# print(f"Número de tentativas até o acerto: {chance}")

# Reposta do Professor Guanabara
computador = randint(0, 10)
print("Olá, eu sou o seu computador. Irei pensar em um número de 0 à 10. ")
sleep(1)
print("Será que você consegue acertar??")
sleep(1)
acertou = False
chance = 0
sleep(1)
while not acertou:
    jogador = int(input("Qual número o computador pensou: "))
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais... tente novamente.")
        elif jogador > computador:
            print("Menos... tente novamente.")
    chance += 1
print(f"PARABÉNS, acertou com {chance} palpite(s).")
print(f"O número que eu escolhi foi {computador}")
# Crie um programa que jogue par ou impar com o computador.
# O jogo só será interrompido quando o jogador perder.
# mostrando o total de vitórias consecutivas que ele conquistou no final.
# Após correção:
# Incluí o while condicao not in "PI" para testar se o usuário inseriu dados válidos.
# Professor Guanabara fez diferente o IF e ELSE para testar se é par ou impar.

from random import randint
from time import sleep
contador = 0
print("Vamos jogar PAR ou IMPAR!")
while True:
    n = int(input("Digite um valor: "))
    computador = randint(1,10)
    resultado = (n + computador)
    condicao = " "
    while condicao not in "PI":
        condicao = str(input("Par[P] ou Ímpar[I]: ")).upper().strip()[0]
    sleep(1)
    print("="*30)
    print(f"Humano escolheu {n}")
    print(f"Computador escolheu {computador}")
    print("="*30)
    sleep(2)
    print(f"{n} + {computador} = {resultado}",end=" ")
    print("DEU PAR" if resultado % 2 == 0 else "DEU IMPAR")
    print("="*30)
    sleep(1)
    if resultado % 2 == 0 and condicao == "P":
        print("JOGADOR VENCEU.")
        print("O jogo só acaba quando o HUMANO perde. Vamos jogar novamente...")
        contador += 1
        sleep(2)
    elif resultado % 2 != 0 and condicao == "I":
        print("JOGADOR VENCEU.")
        print("O jogo só acaba quando o HUMANO perde. Vamos jogar novamente...")
        contador += 1
        sleep(2)
    else:
        print("O COMPUTADOR VENCEU.")
        break
print(f"FIM DE JOGO. Você venceu {contador} vezes.")
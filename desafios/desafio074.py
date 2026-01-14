# Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla.
# Mostre a listagem de números gerados e também indique o maior e o menor valor
# que estão na tupla.
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))
print(f"Os valores sorteados são: ", end="")
for n in numeros:
    print(n, end=" ")
print(f"\nO MAIOR número sorteado é: {sorted(numeros)[-1]}")
print(f"O MENOR número sorteado é: {sorted(numeros)[0]}")
# ou pode usar o min e max para saber o menor e maior em tuplas.
print(f"O MAIOR número sorteado é: {max(numeros)}")
print(f"O MENOR número sorteado é: {min(numeros)}")

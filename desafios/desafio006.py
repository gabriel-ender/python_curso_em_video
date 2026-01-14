# Crie um algorítmo que leia um número e mostre o seu dobro, triplo
# e raiz quadrada.

print('Desafio 06')
print('Programa que lê um número e mostra o dobro, triplo e raiz quadrada.')
n = int(input('Digite um número que pertence aos inteiros: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print(f'O número escolhido foi {n}.')
print(f'O dobro de {n} é {d}.')
print(f'O triplo de {n} é {t}.')
print(f'A raiz quadrada de {n} é {r}.')
print('FIM')

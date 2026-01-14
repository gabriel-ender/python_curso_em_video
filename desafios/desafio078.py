# Faça um exercício que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas
# posições na lista.

n = list()
for c in range(0, 5):
    n.append(int(input(f'Digite um valor para a posição {c}: ')))
print(n)
print(f'O MENOR valor digitado foi {min(n)} nas posições: ', end=' ')
for posicao_n, valor_n in enumerate(n):
    if valor_n == min(n):
        print(f'{posicao_n}',end='...')
print()
print(f'O MAIOR valor digitado foi {max(n)} nas posições: ',end=' ')
for posicao_n, valor_n in enumerate(n):
    if valor_n == max(n):
        print(f'{posicao_n}',end='...')


# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher,
# mas agora utilizando um laço for.

n = int(input('Digite um número para saber a sua tabuada: '))
t = 0
cont= 0
for c in range(1, 11):
    cont += 1
    t = n * cont
    print(f'{n} X {cont:2} = {t:3}')

# outro jeito de fazer com menos linhas
n = int(input('Digite um número para saber a sua tabuada: '))
for c in range(1, 11):
    print(f'{n} X {c:2} = {n * c}')
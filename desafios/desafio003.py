# Crie um script Python que leia dois números e tente
# mostrar a soma entre eles.

print('<<<<Desafio 03>>>>')
print('Vamos somar? Escreva dois números e mostrarei a soma deles.')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
s = num1 + num2
print(f'A soma entre {num1} e {num2} é:', s)
print('A soma entre {} e {} é: {}'.format(num1, num2, s),)
# Duas maneiras de usar o .format

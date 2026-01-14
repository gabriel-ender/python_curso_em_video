#Faça um programa que leia uma frase pelo teclado e mostre:
#1.Quantas vezes aparece a letra A.
#2.Em que posição ela aparece pela primeira vez.
#3.Em que posição ela aparece a última vez.

print('Desafio 26')
frase = str(input('Digite uma frase: ')).strip()
fm = frase.upper()
print('A letra "A" aparece {} vezes na frase.'.format(fm.count('A')))
print('A letra "A" aparece pela primeira vez na posição {}.'.format(fm.find('A')+1))
print('A letra "A" aparece pela última vez na posição {}.'.format(fm.rfind('A')+1))
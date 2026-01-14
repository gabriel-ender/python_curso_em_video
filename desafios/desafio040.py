# Crie um programa que leia duas notas de um aluno e calcule sua média
# mostrando uma mensagem no final, de acordo com a média:
# Média abaixo de 5.0 Reprovado
# Média entre 5.0 e 6.9 Recuoeração
# Média 7.0 ou superior Aprovado

print('Desafio 40')
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1 + n2) / 2
print('A sua média foi {}.'.format(media))
if media < 5.0:
    print('Você foi REPROVADO!')
elif media >= 7.0:
    print('Você está APROVADO!')
elif media >= 5.0 and media < 7.0:
    print('Você está de RECUPERAÇÃO!')

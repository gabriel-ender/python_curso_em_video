# Escreva um programa que leia um número inteiro qualquer e peça
# para o usuário escolher qual será a BASE DA CONVERSÃO.
# 1 para Binário
# 2 para Octal
# 3 para Hexadecimal

print('Desafio 37')
n = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para CONVERSÃO.')
print('[ 1 ] converter para binário.\n[ 2 ] converter para octal.\n[ 3 ] converter para hexadecimal.')
escolha = int(input('Sua opção: '))
if escolha == 1:
    n1 = bin(n)
    print('{} convertido para BINÁRIO é igual a {}.'.format(n, n1[2:]))
elif escolha == 2:
    n2 = oct(n)
    print('{} convertido para OCTAL é igual a {}.'.format(n, n2[2:]))
elif escolha == 3:
    n3 = hex(n)
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(n, n3[2:]))
else:
    print('Erro, tente novamente.')
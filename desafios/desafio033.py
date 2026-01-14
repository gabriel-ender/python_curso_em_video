# Faça um programa que leia três números e mostre qual é o maior e o menor entre eles.

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))
if n1 > n2 and n1 > n3:
    print('O maior número é o {}'.format(n1))
    if n2 > n3:
        print('O menor número é o {}'.format(n3))
    else:
        print('O menor número é o {}'.format(n2))
if n2 > n1 and n2 > n3:
    print('O maior número é o {}'.format(n2))
    if n1 > n3:
        print('O menor número é o {}'.format(n3))
    else:
        print('O menor número é o {}'.format(n1))
if n3 > n1 and n3 > n2:
    print('O maior número é o {}'.format(n3))
    if n1 > n2:
        print('O menor número é o {}'.format(n2))
    else:
        print('O menor número é o {}'.format(n1))
print('FIM da resolução do Gabriel')

# Guanabara faz diferente. Ele já considera o n1 como menor e testa o n2 e n3. Diminui bastante as linhas.
print('Início da resolução do Guanabara.')

# Verificando o maior valor.
maior = n1 # Já considero o n1 maior. Se não for, os IFs irão corrigir testando.
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

# Verificando o menor valor. Considero o n1 como maior
menor = n1 #Já considero o n1 como menor. Se não for, os IFs irão corrigir testando.
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print('O MENOR valor digitado foi {}'.format(menor))
print('O MAIOR valor digitado foi {}'.format(maior))



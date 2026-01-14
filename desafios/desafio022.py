#Crie um programa que leia o nome completo de uma pessoa.
#Apareça o nome com todas as letras MAIÚSCULAS.
#O nome com todas as letras minúsculas.
#Quantas letras ao todo (sem considerar os espaços).
#Quantas letras tem o primeiro nome.

print('Desafio 22')
print('Programa que lê o nome completo e mostra algo.')
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em letra maiúscula é: {}'.format(nome.upper()))
print('Seu nome em letra minúscula é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))

#Duas formas de fazer...
print('Seu primeiro nome é {} e tem {} letras.'.format(nome.split()[0], len(nome.split()[0])))
#ou
print('O seu primeiro nome tem {} letras. '.format(nome.find(' ')))






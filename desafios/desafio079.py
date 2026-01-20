# Crie um programa onde o usuário possa digitar vários valores
# numéricos e cadastre-os em uma lista. Caso o número já exista
# lá dentro, ele não será adicionado. No final, serão exibidos todos
# os valores únicos digitados, em ordem crescente.
lista1 = list()
pergunta = 'S'
while pergunta in 'S':
    lista1.append(int(input('Digite um valor: ')))
    pergunta = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while pergunta not in 'NS':
        pergunta = str(input('Opção Inválida! Deseja continuar? [S/N]: ')).strip().upper()[0]
print(f'Lista 1: {sorted(lista1)}')
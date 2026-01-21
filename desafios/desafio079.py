# Crie um programa onde o usuário possa digitar vários valores
# numéricos e cadastre-os em uma lista. Caso o número já exista
# lá dentro, ele não será adicionado. No final, serão exibidos todos
# os valores únicos digitados, em ordem crescente.
lista1 = list()
pergunta = 'S'
a = ""
while pergunta in 'S':
    a = int(input(f"Digite um valor: "))
    if a not in lista1:
        lista1.append(a)
    else:
        print(f"O número {a} já existe na lista. Valor NÃO computado.")
    pergunta = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while pergunta not in 'NS':
        pergunta = str(input('Opção Inválida! Deseja continuar? [S/N]: ')).strip().upper()[0]
print(f'Lista 1: {sorted(lista1)}')
print("FIM DO PROGRAMA!")
# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final mostre:
# A: Quantas pessoas foram cadastradas;
# B: Uma listagem com as pessoas mais pesadas;
# C: Uma listagem com as pessoas mais leves.
pessoas = list()
dados = list()
pesada = list()
leve = list()
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso (kg): ')))
    pessoas.append(dados)
    dados = list()
    resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while resposta not in 'NS':
        resposta = str(input('Resposta Inválida. Quer continuar? [S/N]: ')).upper().strip()[0]
    if resposta in 'N':
        break
print(pessoas)
for nome, peso in pessoas:
    if peso > maior:
        maior = peso
        pesada = list()
        dados.append(nome)
        dados.append(peso)
        pesada.append(dados)
        dados = list()
    if peso < menor:
        menor = peso
        leve = list()
        dados.append(nome)
        dados.append(peso)
        leve.append(dados)
        dados = list()
    if peso == maior:
        dados.append(nome)
        dados.append(peso)
        pesada.append(dados)
        dados = list()
    if peso == menor:
        dados.append(nome)
        dados.append(peso)
        leve.append(dados)
        dados = list()
print("=-"*20)
print("Listagem de Pessoas LEVES:")
for nome, peso in leve:
    print(f"{nome} com {peso} Kg.")
print("=-"*20)
print("Listagem de Pessoas PESADAS:")
for nome, peso in pesada:
    print(f"{nome} com {peso} Kg.")
print("=-"*20)


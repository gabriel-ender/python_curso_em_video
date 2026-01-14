# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar.
# No final mostre:
# 1. Qual é o total gasto na compra;
# 2. Quantos produtos custam mais de R$ 1.000,00
# 3. Qual é o nome do produto mais barato.

print("="*50)
print(f"{"MERCADO JOÃO PESSOA":^50}")
print("="*50)
total_gasto = custo_mais_1000 = contador = menor = 0
produto_mais_barato = " "
while True:
    produto = str(input("Nome do Produto: ")).strip().title()
    preco = float(input(f"Preço do produto {produto}: R$ "))
    total_gasto += preco
    if preco > 1000:
        custo_mais_1000 += 1
    contador += 1
    if contador == 1: # or preco < menor:
        menor = preco
        produto_mais_barato = produto
    else:
        if preco < menor:
            menor = preco
            produto_mais_barato = produto
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Deseja cadastrar mais produtos? [S]im - [N]ão: ")).strip().upper()[0]
    if continuar == "N":
        break
    print("="*50)
print("="*50)
print(f"Total gasto na compra R$ {total_gasto:.2f}")
print(f"Quantidade de produtos com custo maior de R$ 1.000,00: {custo_mais_1000}")
print(f"O produto mais barato é {produto_mais_barato} e custa R$ {menor:.2f}.")

# É possível simplificar o ELSE. Deixa tudo no IF contador:
# if contador == 1 or preco < menor:
# e apaga o else inteiro.
# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual o valor sacado (inteiro).
# Informar quantas cédulas de cada valor será entregue. 50 20 10 1.

print(f"{" BANCO DA PRAÇA É NOSSA ":=^50}")
valor_de_saque = int(input("Valor de SAQUE: R$ "))
print("="*50)
while True:
    if valor_de_saque // 50 != 0:
        print(f"Total de {valor_de_saque // 50} cédula(s) de R$ 50,00")
        valor_de_saque %= 50
        if valor_de_saque % 50 == 0:
            break
    if valor_de_saque // 20 != 0:
        print(f"Total de {valor_de_saque // 20} cédula(s) de R$ 20,00")
        valor_de_saque %= 20
        if valor_de_saque % 20 == 0:
            break
    if valor_de_saque // 10 != 0:
        print(f"Total de {valor_de_saque // 10} cédula(s) de R$ 10,00")
        valor_de_saque %= 10
        if valor_de_saque % 10 == 0:
            break
    if valor_de_saque // 1 != 0:
        print(f"Total de {valor_de_saque // 1} cédula(s) de R$ 1,00")
    break
print(f"{"SAQUE EFETUADO COM SUCESSO":=^50}")


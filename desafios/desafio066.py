# Faça um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar 999.
# 1. Quantos números foram digitados.
# 2. Soma entre eles, desconsiderando o flag.
soma = contador = 0
while True:
    n = int(input("Digite um valor (999 parar): "))
    if n == 999:
        break
    contador += 1
    soma += n
print(f"A soma dos {contador} valores foi {soma}.")

# Crie um programa que leia dois valores e mostre um menu na tela.
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
from time import sleep

valor1 = int(input("1ª valor: "))
valor2 = int(input("2º valor: "))
# somar = 0             NAO PRECISA CRIAR ESSA VARIÁVEL FORA DA ESTRUTURA WHILE
# multiplicar = 0       NAO PRECISA CRIAR ESSA VARIÁVEL FORA DA ESTRUTURA WHILE
# maior = 0             NAO PRECISA CRIAR ESSA VARIÁVEL FORA DA ESTRUTURA WHILE
menu = 0
while menu != 5:
    print(f"Valores atuais: [{valor1}] e [{valor2}].")
    print("[1] - SOMAR\n[2] - MULTIPLICAR\n[3] - MAIOR\n[4] - NOVOS NÚMEROS\n[5] - SAIR DO PROGRAMA")
    menu = int(input("Qual opção desejada: ").strip())
    if menu == 1:
        somar = valor1 + valor2
        print(f"A soma de {valor1} + {valor2} = {somar}")
    elif menu == 2:
        multiplicar = valor1 * valor2
        print(f"A multiplicação de {valor1} X {valor2} = {multiplicar}")
    elif menu == 3:
        if valor1 > valor2: print(f"O valor maior é {valor1}")
        elif valor1 < valor2: print(f"O valor maior é {valor2}")
        elif valor1 == valor2: print("Não há número maior. Os dois são iguais.")
    elif menu == 4:
        print("Informe os números novamente:")
        valor1 = int(input("1ª valor: ").strip())
        valor2 = int(input("2º valor: ").strip())
    elif menu == 5:
        print("Você escolheu sair. Até mais!")
    else:
        print("Opção Inválida, digite uma opção novamente. Aguarde 3 segundos...")
    print("="*30)
    sleep(3)
print("END")

# Resolução do Professor está parecida. A única coisa que mudou foi acrescentar variável MAIOR na opção 3
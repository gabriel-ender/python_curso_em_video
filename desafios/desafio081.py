# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A: Quantos números foram digitados;
# B: A lista de valores, ordenada de forma decrescente;
# C: Se o valor 5 foi digitado e se está ou não na lista.
lista1 = []
while True:
    lista1.append(int(input("Digite um valor: ")))
    continuar = str(input("Deseja continuar? [S]/[N]: ")).upper().strip()[0]
    if continuar in "N":
        break
# lista1.sort(reverse=True) - Altera a lista original e não precisa colocar sorted nem reverse no print.
print(f"Foram digitados {len(lista1)} números.")
print(f"A lista contém os seguintes números em ordem decrescente: {sorted(lista1, reverse=True)}")
if 5 in lista1:
    print(f"O número 5 está na posição {sorted(lista1, reverse=True).index(5)} lista.")
else:
    print("O número 5 NÃO está na lista.")
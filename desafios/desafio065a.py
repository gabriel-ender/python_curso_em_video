# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a
# 1. Média entre todos os valores.
# 2. Qual foi o maior valor.
# 3. Qual foi o menor valor.
# 4. O programa deve perguntar para o usuário se ele quer ou não
# continuar a digitar valores.

maior = 0
menor = 0
somatorio = 0
contador = 0
flag = ""
while flag != "N":
    n = int(input("Digite um número: "))
    if contador == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    contador += 1
    somatorio += n
    flag = str(input("Quer continuar [S] [N]: ")).upper().strip()
print(f"Você digitou {contador} números e a média entre eles é {somatorio / contador:.2f}")
print(f"O menor valor é {menor} e o maior valor é {maior}.")
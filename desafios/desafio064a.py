# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a
# condição de parada.
# No final, mostre quantos números foram digitados
# Qual foi a soma entre eles. Desconsiderando o flag.
numero = 0
contador = 0
somatorio = 0
while numero != 999:
    numero = int(input("Digite um número (999 pra parar): "))
    if numero != 999:
        somatorio = somatorio + numero
        contador += 1
    else:
        somatorio = somatorio + 0
print(f"Você digitou {contador} números e a soma entre eles foi {somatorio}.")

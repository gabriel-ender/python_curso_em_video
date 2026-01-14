# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a
# condição de parada.
# No final, mostre quantos números foram digitados
# Qual foi a soma entre eles. Desconsiderando o flag.
numero = contador = somatorio = 0
numero = int(input("DIgite um número (999 para sair): "))
while numero != 999:
    somatorio = somatorio + numero
    contador = contador + 1
    numero = int(input("DIgite um número (999 para sair): "))
print(f"VOcê digitou {contador} números e a soma entre eles é {somatorio}")

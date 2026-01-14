# Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA.
# Mostre os 10 primeiros termos da progressão usando a estrutura while.

termo = int(input("Digite um número para saber sua PA: "))
razao = int(input("Digite a razão da PA: "))
contador = 1
pa = 0
while contador <= 10:
    pa = termo + (contador - 1) * razao
    print(pa,end="-")
    contador += 1
print('FIM')
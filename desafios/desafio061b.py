# Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA.
# Mostre os 10 primeiros termos da progressão usando a estrutura while.

# Resolução do Professor Guanabara.

print("10 Primeiros termos de uma Progressão Aritmética.")
termo = int(input("Qual o TERMO inicial: "))
razao = int(input("Qual a razão: "))
contador = 1
pa = termo
while contador <= 10:
    print(f"{pa+razao}",end=" ")
    contador += 1
    pa = pa + razao
print("FIM")
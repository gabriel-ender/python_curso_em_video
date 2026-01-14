# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
# Jeito que o Guanabara fez.
maior = 0
menor = 0
for pess in range(1, 6):
    peso = float(input(f'Peso da {pess}ª pessoa: '))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if maior < peso:
            maior = peso
        elif menor > peso:
            menor = peso
print(f"O MAIOR peso foi {maior:.3f} Kg.")
print(f"O MENOR peso foi {menor:.3f} Kg.")
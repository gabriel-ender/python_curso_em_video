# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
pesolista = []
for pess in range(1, 6):
    peso = float(input(f'Qual o peso da {pess}ª pessoa: '))
    pesolista.append(peso)
pesolistaorganizado = sorted(pesolista, reverse=True)
print(f'O MAIOR peso foi {pesolistaorganizado[0]:.3f} Kg.')
print(f'O MENOR peso foi {pesolistaorganizado[-1]:.3f} Kg')



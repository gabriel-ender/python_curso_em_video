# Escreva um programa que leia um valor em metros e o exiba
# convertido em centímetros e milímetros.

print('Desafio 08')
print('Conversor de unidade: de metros para cm e mm.')
u = float(input('Digite um valor em metros: '))
cm = u * 100
mm = u * 1000
print(f'O valor que você digitou foi {u}.')
print(f'{u} m equivale a {cm} cm.')
print(f'{u} m equivale a {mm} mm.')
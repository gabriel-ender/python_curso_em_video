# Escreva um programa que leia um número n inteiro qualquer,
# mostre na tela os n primeiros elementos de uma
# Sequência de Fibonacci.

print("="*22)
print("Sequência de Fibonacci")
print("="*22)
termo = int(input("Quantos termos você quer mostrar: "))
contador = 1
n = 0
n1 = 1
fibo = n + n1
print(fibo, end=" - ")
while contador < termo:
    fibo = n + n1
    print(f"{fibo}",end=" - ")
    n = n1
    n1 = fibo
    contador += 1
print("FIM")
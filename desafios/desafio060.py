# Faça um programa que leia um número qualquer e mostre o seu fatorial.

# n = int(input("Digite um número para saber o seu FATORIAL: "))
# n2 = n
# print(f"Calculando {n}!")
# while n != 1:
#     fatorial = n2 * (n - 1)
#     print(f"{n2} X {n - 1}",end=" = ")
#     n2 = fatorial
#     n = n - 1
# print(n2)


# Fazendo pela estrutura FOR

n = int(input("Digite um número para saber o seu FATORIAL: "))
print(f"Calculando {n}!")
c2 = n
for c in range(n-1, 0, -1):
    fatorial = c2 * (c)
    print(f"{c2} X {c}", end=" = ")
    c2 = fatorial
print(c2)

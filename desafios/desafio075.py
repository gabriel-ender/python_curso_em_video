# Desenvolva um programa que leia 4 valores.
# Guarde-os em uma TUPLA.
# [1] Quantas vezes apareceu o valor 9;
# [2] Em que posição foi digitado o primeiro valor 3;
# [3] Quais foram os números pares.
numeros = (int(input("Digite um número: ")), int(input("Digite outro número: ")),
           int(input("Digite mais um número: ")), int(input("Digite o último número: ")))
# Mostrando os valores digitados.
print(f"Você digitou os valores: {numeros}", end=" ")

# Mostrando se tem ou não o número 9
print(f"\nO número 9 apareceu {numeros.count(9)} vez(es)." if 9 in numeros else
"""\nO número 9 não apareceu em nenhuma posição.""")
# Mostrando onde aparece o número 3 ou não.
print(f"O número 3 apareceu na posição {numeros.index(3)+1}." if 3 in numeros else
"""O número 3 não aparece em nenhuma posição.""")
# Mostrando os números pares, ou não.
print(f"Número(s) par(es): ", end="")
for n in numeros:
    if n % 2 == 0:
        print(n, end=" ")

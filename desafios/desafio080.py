# Crie um programa onde o usuário possa digitar 5 valores numéricos
# e cadastre-os em uma lista, já na posição correta de inserção
# sem usar o sort().
lista1 = []
n = ""
for c in range(0, 5):
    n = int(input("Digite um valor: "))
    if c == 0 or n > lista1[-1]:
        lista1.append(n)
        print("Valor adicionado ao FINAL da lista!")
    if n < lista1[0]:
        lista1.insert(0, n)
        print("Valor adicionado no INÍCIO da lista!")
    if
print(f"Os números adicionados foram: {lista1}")

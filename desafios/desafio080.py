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
    else:
        pos = 0
        while pos < len(lista1):
            if n <= lista1[pos]:
                lista1.insert(pos, n)
                print(f"Valor adicionado na posição {pos} da lista!")
                break
            pos += 1
print(f"Os números adicionados foram: {lista1}")

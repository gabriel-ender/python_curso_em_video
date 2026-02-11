# Crie um programa que vai ler vários números e colocá-los em uma lista.
# Crie DUAS listas extras que vão conter os números pares e ímpares,
# respectivamente.
# Ao final, mostre o conteúdo das 3 listas.
lista1 = []
while True:
    lista1.append(int(input("Digite um número: ")))
    resposta = str(input("Deseja continuar? [S/N]: ")).upper().strip()[0]
    while resposta not in "SN":
        resposta = str(input("Opção Inválida! Deseja continuar? [S/N]: ")).upper().strip()[0]
    if resposta in "N":
        break
print(f"A lista completa {lista1}.")
lista_par = []
lista_impar = []
for elemento in lista1:
    if elemento % 2 == 0:
        lista_par.append(elemento)
    else:
        lista_impar.append(elemento)
print(f"A lista PAR é {lista_par}.")
print(f"A lista ÍMPAR é {lista_impar}.")

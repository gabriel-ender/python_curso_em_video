# Estrutura while
n = 0
s = 0
somatorio = 0
p = ""
while p in "Ss" :
    s = int(input("Digite um número: "))
    p = str(input("Deseja continuar? [S - sim] e [N - não]: "))
    somatorio += s
print(somatorio)


n1 = 1
par = impar = 0
print("Programa que soma e mostra quandos números são pares e ímpares. ")
print("O programa irá somar até você digitar o número 0 (zero) para parar.")
while n1 != 0:
    n1 = int(input("Digite um valor: "))
    if n1 != 0:
        if n1 % 2 == 0:
            par += 1
        else:
            impar += 1
print(f"Tem {impar} números ímpares e {par} números pares.")

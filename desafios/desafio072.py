# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
# por extenso, de 0 até 20.
# Seu programa deverá ler um número pelo teclado e mostrá-lo por extenso.
l1 = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
      "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete",
      "dezoito", "dezenove", "vinte")
n = int(input("Digite um número entre 0 e 20: "))
while True:
    if n < 0 or n > 20:
        n = int(input("Número inválido. Digite um número entre 0 e 20: "))
    else:
        break
print(f"Você digitou o número {l1[n]}.")



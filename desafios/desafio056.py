# Desenvolva um programa que leia o NOME, IDADE e SEXO de 4 pessoas.
# No final do programa mostre:
# 1. Média de idade das 4 pessoas.
# 2. Qual é a idade do homem mais velho.
# 3. Quantas mulheres tem menos de 20 anos.

somaidade = 0
mulher = 0
nomehomem = "Ninguém"
maioridade = 0
for p in range(1, 5):
    print(f"{p}ª Pessoa")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M / F]: ")).upper().strip()
    if p == 1 and sexo == "M":
        maioridade = idade
        nomehomem = nome
    else:
        if idade > maioridade and sexo == "M":
            maioridade = idade
            nomehomem = nome
    if sexo == "F" and idade < 20:
        mulher+= + 1
    somaidade += idade
print(f"A média de idade do grupo é de {somaidade / 4}")
print(f"O homem mais velho tem {maioridade} anos e se chama {nomehomem}!")
print(f"Ao todo, existem {mulher} mulheres com menos de 20 anos.")



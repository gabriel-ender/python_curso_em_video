# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# 1. Quantas pessoas tem mais de 18 anos.
# 2. Quantos homens foram cadastrados.
# 3. Quantas mulheres tem menos de 20 anos.

mais18 = homens = menos20mulher = 0
while True:
    idade = 0
    sexo = continuar = " "
    pessoa = str(input("Nome Completo: ")).strip().title().split() #tirar espaços do meio; letras maísculas no nome e transformar em lista.
    pessoa = (" ".join(pessoa)) # Junta todos os elementos da lista com um espaço. Para evitar espaços no meio do nome e deixar mais apresentavel.
    # print(pessoa)
    while idade <= 0:
        idade = int(input("Idade: "))
        # print(idade)
    while sexo not in "FM":
        sexo = str(input("Sexo [F] Feminino - [M] Masculino: ")).strip().upper()[0]
        # print(sexo)
    if idade > 18:
        mais18 += 1
    if sexo in "M":
        homens += 1
    if sexo in "F" and idade < 20:
        menos20mulher += 1
    while continuar not in "SN":
        continuar = str(input("Deseja incluir mais dados? [S]im | [N]ão: ")).strip().upper()[0]
    if continuar in "N":
        break
print("="*30)
print(f"{mais18} pessoas maiores de 18 anos." if mais18 > 1 else f"{mais18} pessoa maior de 18 anos.")
print("="*30)
print(f"{homens} homens cadastrados." if homens > 1 else f"{homens} homem cadastrado.")
print("="*30)
print(f"{menos20mulher} mulheres com menos de 20 anos." if menos20mulher > 1 else f"{menos20mulher} mulher com menos de 20 anos.")

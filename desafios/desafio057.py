# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F.
# Caso esteja errado, peça a digitação novamente até ter o valor correto.

# Começo de validação de Dados.

# # Meu Jeito
# sexo = ""
# while sexo != "M" and sexo != "F":
#     sexo = str(input("Qual o seu sexo? Considere M - masculino e F - feminino: ")).upper().strip()
#     if sexo != "M" and sexo != "F":
#         print('Dados inválidos. Digite novamente.')
#
# print(f"Dado inserido, o seu sexo é {sexo}.")

# Resolução do professor Guanabara
sexo = str(input("Qual o seu sexo? [M] - [F]: ")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("Sexo Inválido. Por favor, informe seu sexo [M] - [F]: ")).strip().upper()[0]
print(f"Dado inserido, sexo {sexo}.")

# .strip para retirar espaços início e fim
# .upper para deixar tudo maiúsculo.
# [0] após .upper para fatiar apenas o 1 caracter.

# Crie um programa que leia um ano de nascimento de 7 pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores de idade.
from datetime import date
print("Programa que irá ler nome e idade de 7 pessoas e mostrar se já é maior de idade ou não.")
contpessoa = 0
contmaior = 0
contmenor = 0
data = date.today().year
for c in range(1, 8):
    contpessoa += 1     # Em vez de criar uma variável, pode usar o c como contador de pessoa.
    nome = str(input(f'Nome da {contpessoa}ª pessoa: ').title())    # nome = str(input(f'Nome da {c}ª pessoa: ').title())
    anonascimento = int(input(f"Em que ano {nome} nasceu: "))
    if data - anonascimento >= 18:
        contmaior += 1
    else:
        contmenor += 1
print(f"Temos {contpessoa} pessoa(s) no total.")
print(f'Temos {contmaior} pessoa(s) maior de idade.')
print(f"E também temos {contmenor} pessoa(s) menor de idade.")

# O Guanabara usou o c como contador de pessoa. O que é uma maneira certe de se fazer para evitar linhas e criar variáveis
# desnecessárias. Ele criou uma variável chamada idade. Eu não criei mas no if já condicionei a idade.
# De resto, está certo.

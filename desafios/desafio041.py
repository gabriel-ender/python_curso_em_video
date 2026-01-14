from datetime import date
print('Confederação Nacional de Natação')
print('CATEGORIAS')
nascimento = int(input('Em que ano você nasceu: '))
idade = date.today().year - nascimento
print('Você tem {} anos de idade. Sua categoria será...'.format(idade))
if idade < 0 or nascimento < 1900:
    print('Dados inválidos, reinicie o programa e tente novamente.')
elif idade <= 9:
    print('Categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JUNIOR')
elif idade <= 25:
    print('Categoria SÊNIOR')
else:
    print('Categoria Master')
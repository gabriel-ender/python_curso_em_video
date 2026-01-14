nome = str(input('Qual o seu nome? ')).strip()
if nome.lower() == 'gustavo':
    print('Que nome legal!')
else:
    print('Seu nome é tão normal!')
print('Olá, {}.'.format(nome.title()))
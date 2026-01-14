# Faça um programa que leia o ano de nascimento de um jovem e
# informe, de acordo com sua idade, se ele ainda vai se alistar
# ao serviço militar, se é a hora de se alistar ou se já
# passou do tempo de alistamento.
# O programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

print('Desafio 39!')
print('EXÉRCITO BRASILEIRO')
print('Verifique aqui se você deve se alistar.')
n = int(input('Digite o ano de seu nascimento: '))
ano = date.today().year
prazo = ((date.today().year - n) - 18).__abs__()
idade = (date.today().year - n)
passou = ('Você tem {} anos. Já se passaram {} ano(s) de se alistar. Aliste-se Urgente.'.format(idade, prazo))
noprazo = ('Você tem {} anos e deve se alistar IMEDIATAMENTE.'.format(idade))
cedo = ('Você tem {} anos e ainda faltam {} ano(s) para se alistar.'.format(idade, prazo))

if idade < 18:
    print(cedo)
elif idade == 18:
    print(noprazo)
else:
    print(passou)

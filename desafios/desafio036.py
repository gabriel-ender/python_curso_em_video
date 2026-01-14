# Escreva um programa para aprovar o empréstimo bancário para a
# compra de uma casa. Pergunte o valor da casa, o salário do comprador
# e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o
# empréstimo será negado.

print('Desafio 36')
vc = float(input('Qual o valor da casa: R$ '))
s = float(input('Qual o valor do seu salário mensal: R$ '))
a = int(input('Em quantos anos você quer financiar: '))
c1 = s * 0.3
p = vc / (a * 12)
print('Para pagar uma casa de R$ {:.2f} em {} anos, a prestação será de R$ {:.2f}.'.format(vc, a, p))
if p > c1:
    print('Empréstimo negado!')
    print('A parcela de R$ {} excedeu os 30% ({}) do seu salário R$ {}.'. format(p, c1, s))
else:
    print('O empréstimo será CONCEDIDO!')
    


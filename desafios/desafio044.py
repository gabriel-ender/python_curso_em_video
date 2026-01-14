# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu Preço normal e Condição de pagamento:
# 1. À vista dinheiro/Pix: 10% de desconto;
# 2. À vista no Cartão de Crédito: 5% de desconto;
# 3. Parcelado até 2x no Cartão de Crédito: Preço normal.
# 4. Parcelado em 3x ou mais no Cartão de Crédito: 20% de juros.

print(f'{"Lojas Gabriel":=^40}')
print('Consulta Forma de pagamento de um Produto')
p = float(input('Preço do Produto R$ '))
print('FORMAS DE PAGAMENTO')
print('1. À vista no dinheiro/PIX.')
print('2. À vista no Cartão de Crédito.')
print('3. Parcelado até 2x no Cartão de Crédito.')
print('4. Parcelado em 3x ou mais no Cartão de Crédito.')
c = int(input('Escolha a forma de pagamento escrevendo o número correspondente: '))
if c == 1:
    c1 = p - (p * 10/100) # 10 % de desconto
    print('Sua compra no valor de R$ {:.2f} terá 10% de desconto e custará R$ {:.2f}.'.format(p, c1))
elif c == 2:
    c2 = p - (p * 5/100) # 5 % de desconto
    print('Sua compra no valor de R$ {:.2f} terá 5% de desconto e custará R$ {:.2f}.'.format(p, c2))
elif c == 3:
    vp = p / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} sem juros.'.format(vp))
    print('Sua compra irá custar os mesmos R$ {:.2f}'.format(p))
elif c == 4:
    parc = int(input('Quantas parcelas: '))
    c4 = p + (p * 20/100) # 20% de juros.
    vp = c4 / parc
    print('Sua compra será parcelada em {}x de R$ {:.2f} com juros de 20%.'.format(parc, vp))
    print('Sua compra de {:.2f} irá custar R$ {:.2f} no total.'.format(p, c4))
else:
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')

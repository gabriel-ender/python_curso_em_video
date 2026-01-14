print('Calculador de IMC.')
peso = float(input('Qual o seu peso (Kg): '))
alt = float(input('Qual sua altura (m): '))
idade = int(input('Qual a sua idade: '))
imc = peso / (alt**2)
imc1 = ('Você está ABAIXO do Peso ideal')
imc2 = ('Você está no peso IDEAL.')
imc3 = ('Você está ACIMA do Peso ideal')
imc4 = ('Você está com OBESIDADE, cuidado!')
print('Seu IMC é {:.2f}.'.format(imc))
if idade <= 60:
    if imc < 18.5:
        print(imc1)
    elif imc <= 24.99:
        print(imc2)
    elif imc <= 29.99:
        print(imc3)
    else:
        print(imc4)
elif idade > 60:
    if imc < 22:
        print(imc1)
    elif imc <= 27:
        print(imc2)
    elif imc <= 29.99:
        print(imc3)
    else:
        print(imc4)
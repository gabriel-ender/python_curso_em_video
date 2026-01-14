# Faça um programa que leia uma FRASE qualquer e diga
# se essa frase é um palíndromo, desconsiderando os espaços.
print(f'{'/':/^40}')
print(f'{'Identificador de frase Palíndromo':/^40}')
print(f'{"/":/^40}')
print('Palíndromo: é uma palavra, frase ou\nnúmero que permanece igual quando lida\nde trás para diante.')
frase1 = str(input('Digite uma frase: ').upper().replace(" ", ""))
frase2 = frase1[::-1].replace(" ", "").upper()
print(f'A frase que você digitou é: {frase1}')
print(f'A frase de trás para diante é: {frase2}')
if frase1 == frase2:
    print('Portanto: a Frase é Palíndromo :)')
else:
    print('Portanto: a Frase NÃO É Palíndromo :(')


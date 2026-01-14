# Mesmo desafio do palíndromo, só utilizando estrutura for.
frase = str(input("Digite uma frase: ").strip().upper())
palavras = frase.split()
palavrasjuntas = "".join(palavras)
inverso = ""
for letra in range(len(palavrasjuntas)-1, -1, -1): # Usei o for para "inverter" as letras de palavras juntas.
    inverso += palavrasjuntas[letra] # Usei o inverso para "adicionar" as letras invertidas geradas pela estrutura de repetição na própria variável inverso.
print(f'A frase que você digitou é: {palavrasjuntas}.')
print(f'A frase invertida é: {inverso}')
if palavrasjuntas == inverso:
    print('A frase É PALÍNDROMO :)')
else:
    print("A frase NÃO É PALÍNDROMO :(")

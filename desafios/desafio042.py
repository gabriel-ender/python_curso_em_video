print('Programa pra saber se 3 lados formam um triângulo e qual o tipo.')
l1 = float(input('Primeiro Segmento: '))
l2 = float(input('Segundo Segmento: '))
l3 = float(input('Terceiro Segmento: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos acima PODEM formar um TRIÂNGULO.')
    if l1 == l2 and l1 == l3 and l2 == l3:  # ou l1 == l2 == l3 (Python aceita e é usado pelo Guanabara).
        print('O triângulo é EQUILÁTERO.')
    elif l1 == l2 and l3 != l1 or l1 == l3 and l2 != l1 or l2 == l3 and l1 != l2:
        print('O triângulo é ISÓSCELES')
    elif l1 != l2 and l1 != l3 and l2 != l3:    # ou l1 != l2 != l3 != l1 (para diferente, não funciona igual a iqualdade. Deve escrever que o l3 != l1 igual feito no final.
        print('O triângulo é ESCALENO.')
else:
    print('Os segmentos acima NÃO podem formar um Triângulo.')


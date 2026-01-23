# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses
# abertos e fechados na ordem correta.
expressao = str(input("Digite a expressão: "))
ver_a = 0
ver_b = 0
for elemento in expressao:
    if elemento in "(":
        ver_a += 1
    if elemento in ")":
        ver_b += 1
if ver_a == ver_b:
    print("A expressão está CORRETA!")
    print(f"Possui {ver_a} '(' e {ver_b} ')'")
else:
    print("A expressão está INCORRETA!")
    print(f"Possui {ver_a} '(' e {ver_b} ')'")



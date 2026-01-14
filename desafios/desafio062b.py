# Melhore o desafio 61, perguntando para o usuário se ele
# quer mostrar mais alguns termos.
# O programa encerra quando ele mostrar 0 termos.
# CÓDIGO FEITO PELO PROFESSOR GUANABARA

print("-=-"*5)
print("Gerador de PA.")
print("-=-"*5)
termo = int(input("Qual o TERMO: "))
razao  = int(input("Qual a RAZÃO: "))
pa = termo
termos = 10
total = 0
cont = 1
while termos != 0:
    total = total + 10
    while cont <= total:
        print(f"{pa}",end= " - ")
        pa = pa + razao
        cont = cont + 1
    print("PAUSA")
    termos = int(input("Quantos termos você quer mostrar a mais: "))
print(f"Progressão finalizada com {total} termos mostrados. ")
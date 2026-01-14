# Melhore o desafio 61, perguntando para o usuário se ele
# quer mostrar mais alguns termos.
# O programa encerra quando ele mostrar 0 termos.
print("-=-"*5)
print("Gerador de PA.")
print("-=-"*5)
termo = int(input("Qual o TERMO: "))
razao  = int(input("Qual a RAZÃO: "))
contador = 0
pa = termo
termos = 10
while contador < termos:
    print(pa, end=" - ")
    contador+= 1
    pa = pa + razao
    if contador >= termos:
        print("PAUSA", end="")
        somatermos = int(input("\nQuantos termos você quer mostrar a mais: "))
        termos = termos + somatermos
print("FIM")
print(f"Foram mostrados {contador} TERMOS no total.")


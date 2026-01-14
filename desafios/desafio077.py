# Crie um programa que tenha uma tupla com várias palabras (Não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas VOGAIS.
palavras = ("varredura",
            "afogar",
            "amanhecer",
            "barbear",
            "vendedor",
            "tornozelo",
            "corneta",
            "paralelepipedo",
            "espesso",
            "floresta",
            "chocolate",
            "salada")
print(f"{"Identificador de VOGAIS":=^35}")
for palavra in palavras:
    print(f"\nNa palavra {palavra.upper()} temos: ",end="")
    for vogal in range(0, len(palavra)): # Dá pra fazer: for vogal in palavra: (também dá certo).
        if palavra[vogal].lower() in "aeiou":
            print(palavra[vogal],end=" ")

# for palavra in palavras:
#     print(f"\nNa palavra {palavra.upper()} temos: ",end="")
#     for vogal in palavra: # Dá pra fazer: for vogal in palavra: (também dá certo).
#         if vogal.lower() in "aeiou":
#             print(vogal,end=" ")
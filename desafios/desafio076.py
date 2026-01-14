# Crie um programa que tem uma tupla única com nomes de produtos e seus
# respectivos preços, na sequência.
# Mostre uma listagem de preços, organizando os dados em forma tabular.
print("="*40)
print(f"{"Listagem de Preço":^40}")
print("="*40)
produtos = ("Lápis", 1.75,
            "Borracha", 2.00,
            "Caderno", 15.90,
            "Estojo", 25.00,
            "Transferidor", 4.20,
            "Compasso", 9.99,
            "Mochila", 120.32,
            "Canetas", 22.30,
            "Livro", 34.90)
for c, lista in enumerate(produtos):
    if c % 2 == 0:
        print(f"{produtos[c]:.<31}", end="")
        print("R$ ", end="")
    if c % 2 != 0:
        print(f"{produtos[c]:6.2f}")
print("="*40)

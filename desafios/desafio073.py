# Crie uma tupla com os 20 primeiros colocados do Brasileirão da tabela
# 2025 final do Brasileirão, na ordem de colocação.
# Depois mostre:
# [1] Apenas os 5 primeiros colocados;
# [2] Os últimos 4 colocados da tabela;
# [3] Uma lista com os times em ordem alfabética;
# [4] Em que posição na tabela está o time do Palmeiras.
times = ("Flamengo", "Palmeiras", "Cruzeiro", "Mirassol", "Fluminense", "Botafogo",
         "Bahia", "São Paulo", "Grêmio", "Bragantino", "Atlético-MG", "Santos",
         "Corinthians", "Vasco da Gama", "EC Vitória", "Internacional", "Ceará SC",
         "Fortaleza", "Juventude", "Sport Recife")
print("="*48)
print(f"Os times classificados para a Libertadores são: ")
for liberta in range(0, 5):
    print(f"{liberta+1}. {times[liberta]}")
print("="*48)
print("Os times rebaixados são: ")
for rebaixado in range(16, 20):
    print(f"{rebaixado+1}. {times[rebaixado]}")
print("="*48)
print("Os times em ordem alfabética: ")
for timeordem in range(0, 20):
    print(sorted(times)[timeordem])
print("="*48)
print(f"O Palmeiras está na {times.index("Palmeiras")+1}ª posição.")
print(f"O Santos está na {times.index("Santos")+1}ª posição.")




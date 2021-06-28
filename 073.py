# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da 
# Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ("Fortaleza", "Athetico-PR", "Flamengo", "Atlético-GO", "Atlético-MG", 
        "Bragantino", "Fluminense", "Bahia", "Palmeiras", "Corinthians", 
        "Ceará SC", "Santos", "Internacional", "Juventude", "Cuiabá", 
        "Sport Recife", "São Paulo", "Chapecoense", "Grêmio", "América-MG")

print(f"TABELA DO CAMPEONATO BRASILEIRO DE FUTEBOL, SERIE-A (JUN/2021)\n{times}")
print('-=' * 15)
print(f"OS 5 PRIMEIRO COLOCADOS:\n {times[0:5]}")
print('-=' * 15)
print(f"OS 4 ÚLTIMO COLOCADOS: \n {times[-4:]}")
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f"O clube Chapecoense se encontra na posição {(times.index('Chapecoense'))}")

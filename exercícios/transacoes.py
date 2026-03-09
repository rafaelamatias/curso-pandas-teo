
# %%

import pandas as pd

# %%

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()

# %%

# 03.02 - Quantas colunas do tipo int há no arquivo transacoes.csv ?

int = transacoes.select_dtypes(include="int").columns
print("Número de colunas do tipo int:", len(int))

# %%

# 04.03 - Quantas transações ocorreram no dia 2025-02-01?

filtro = (transacoes["DtCriacao"] == "2025-09-17")
transacoes[filtro]
print("Número de transações em 2025-02-01:", transacoes[filtro].shape[0])



# %%

# 05.05 - Selecione a primeira transação diária de cada cliente.

transacoes.sort_values("DtCriacao")
transacoes["data"] = pd.to_datetime(transacoes["DtCriacao"]).dt.date
transacoes.drop_duplicates(keep="first", subset=["IdCliente", "data"])


# %%

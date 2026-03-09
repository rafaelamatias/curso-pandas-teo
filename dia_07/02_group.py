# %%

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes

# %%

transacoes.groupby(by=["IdCliente"]).count() # agrupa por cliente e conta quantas linhas tem para cada cliente

# %%
transacoes.groupby(by=["IdCliente"])[["IdTransacao"]].count() # agrupa por cliente e conta quantas transações tem para cada cliente

# %%

summary =(transacoes.groupby(by=["IdCliente"], as_index=False)
                        .agg({"IdTransacao": ["count"], "QtdePontos": ["sum", "mean"] })
    )
summary

# %%

summary.columns = ['idCliente', 'total_transacoes', 'total_pontos', 'media_pontos']
summary
# %%

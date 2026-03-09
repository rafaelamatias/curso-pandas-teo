# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()

# %%

df["qtdePontos"].dtype

# %%

df["qtdePontos"] = df["qtdePontos"].astype(float) # Convertendo para float 
df["qtdePontos"].dtype

# %%

df.head()

# %%

df["DtCriacao"] = df["DtCriacao"].astype("datetime64[ns]")  # Convertendo para datetime
df["DtCriacao"] # também é possível usar pd.to_datetime(df["DtCriacao"]), se não tiver as datas perfeitamente formatadas

# %%

df["DtCriacao"].dt.month # pode acessar dia, mês, ano, etc.

# %%

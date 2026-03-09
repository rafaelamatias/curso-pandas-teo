# %%

import pandas as pd

# %%

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head()

# %%

clientes.dropna() # Remover linhas com valores ausentes

# %%

clientes.dropna(how="all") # Remover linhas onde todos os valores são ausentes
clientes.dropna(how="any") # Remover linhas onde qualquer valor é ausente

# %%

df = pd.DataFrame({
    "nome": ["Ana", "Bruno", None, "Daniel", "Eduarda"],
    "idade": [25, None, 30, None, 22],
    "salario": [5000, 6000, None, 7000, None]
})
df


# %%

df.dropna(how="any", subset=["idade", "salario"]) # Remover linhas com valores ausentes na coluna "idade"

# %%

df.fillna(0) # Preencher valores ausentes com 0

# %%

medias = df[["idade", "salario"]].mean()
df.fillna(medias) # Preencher valores ausentes com a média da coluna

# %%


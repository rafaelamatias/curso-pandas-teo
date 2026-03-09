
# %%

import pandas as pd

# %%

df = pd.DataFrame({
    "nome": ["Ana", "Bruno", "Carlos", "Ana", "Bruno", "Daniel"],
    "sobrenome": ["Silva", "Souza", "Oliveira", "Silva", "Souza", "Almeida"],
    "idade": [25, 30, 35, 25, 30, 40],
    "salário": [5000, 6000, 7000, 5000, 6000, 8000]
})

df
# %%

df = df.sort_values("salário", ascending=False)

# %%

df.drop_duplicates(keep="last") # manter a primeira ocorrência


# %%
 
df.drop_duplicates() # remover duplicatas considerando todas as colunas

# %%

df.drop_duplicates(subset=["nome", "sobrenome"]) # remover duplicatas considerando apenas as colunas nome e sobrenome

# %%


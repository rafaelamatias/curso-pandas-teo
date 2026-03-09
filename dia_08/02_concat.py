
# %%

import pandas as pd

# Criando os DataFrames
df1 = pd.DataFrame({
    'Cliente': [1, 2, 3],
    'Nome': ['Ana', 'Bruno', 'Carlos'],
    'Idade': [20, 25, 30]
})
df1

# %% 

df2 = pd.DataFrame({
    'Cliente': [4, 5, 6],
    'Nome': ['Diana', 'Eduardo', 'Fernanda'],
    'Idade': [22, 28, 35]
})
df2

# %%

df3 = pd.DataFrame({
    'Idade': [50, 45, 23]
})

df3 = df3.sort_values(by='Idade', ascending=True).reset_index(drop=True)
df3

# %%

dfs = [df1, df2, df3]

pd.concat(dfs, axis=1, ignore_index=True)
# %%

pd.concat(dfs, axis=1, ignore_index=True)
# %%

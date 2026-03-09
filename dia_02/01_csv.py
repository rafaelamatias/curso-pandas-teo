# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv ", sep=";") # Lê o arquivo CSV com separador ponto e vírgula
df # Exibe o DataFrame lido



# %%

df.to_csv("clientes.csv", index=False) # Salva o DataFrame em um arquivo CSV sem o índice

# %%

df.to_excel("clientes.xlsx", index=False) # Salva o DataFrame em um arquivo Excel sem o índice

# %%
df_2 = pd.read_excel("clientes.xlsx") # Lê o arquivo Excel
df_2 # Exibe o DataFrame lido do Excel
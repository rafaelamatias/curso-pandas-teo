# %%

import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")  # Lê o arquivo CSV com separador ponto e vírgula
df_clientes  # Exibe o DataFrame lido
# %%

df_clientes.head(n = 3) # mesma coisa de sql limit 5

# %%

df_clientes.tail() # últimas 5 linhas / é possível definir números colocando n = número q quer

# %%


df_clientes.sample(10) # Pega 10 linhas aleatórias do DataFrame

# %%

df_clientes.shape  # Mostra a quantidade de linhas e colunas do DataFrame

# %%

df_clientes.columns  # Mostra os nomes das colunas do DataFrame

# %%

df_clientes.index # Mostra os índices do DataFrame

# %%

df_clientes.info() # Mostra informações resumidas sobre o DataFrame

# %%

df_clientes.info(memory_usage='deep') # Mostra informações detalhadas sobre o uso de memória do DataFrame

# %%

df_clientes.dtypes # Mostra os tipos de dados de cada coluna do DataFrame

# %%

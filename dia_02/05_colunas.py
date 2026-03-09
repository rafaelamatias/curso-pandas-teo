# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")

df.shape # Mostra a quantidade de linhas e colunas do DataFrame

# %%

df.info(memory_usage='deep') # Mostra informações detalhadas sobre o uso de memória do DataFrame
# %%

df.dtypes   # Mostra os tipos de dados de cada coluna do DataFrame

# %%

# PARA RENOMEAR COLUNAS

df = df.rename(columns= {"QtdePontos": "QuantidadePontos", 
                         "IdCliente": "IdentificadorCliente"})
df

# é usado uma função de dicionário, onde a chave é o nome antigo e o valor é o nome novo
 

# %%

df["IdentificadorCliente"]  # Acessa a coluna "IdentificadorCliente" do DataFrame


# %%

df[["IdentificadorCliente", "QuantidadePontos"]]  # Acessa múltiplas colunas do DataFrame
# %%

colunas = list(df.columns)  # Obtém a lista de nomes das colunas do DataFrame
colunas.sort()  # Ordena a lista de nomes das colunas em ordem alfabética
colunas  # Exibe a lista ordenada de nomes das colunas
# %%

df = df[colunas]  # Reorganiza as colunas do DataFrame com base na lista ordenada
df  # Exibe o DataFrame com as colunas reorganizadas
# %%

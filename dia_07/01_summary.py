# %%

import pandas as pd

idades = [20, 25, 30, 35, 40]

idades = pd.Series(idades)
idades

# %%

idades.describe() # faz uma sumarização dos dados, mostrando a média, o desvio padrão, os valores mínimo e máximo, e os quartis
# %%

clientes = pd.read_csv("../data/clientes.csv", sep=";") # lê o arquivo CSV e armazena em um DataFrame chamado
clientes

# %%

redes_sociais = ["flEmail", "flTwitch", "flYouTube", "flBlueSky", "flInstagram"]
clientes[redes_sociais].sum() # faz uma sumarização dos dados, mostrando a média, o desvio padrão, os valores mínimo e máximo, e os quartis
# %%

num_columns = clientes.dtypes[~(clientes.dtypes == "object")].index.tolist() # seleciona as colunas numéricas do DataFrame e retorna uma lista com os nomes dessas colunas
clientes[num_columns].mean()

# %%


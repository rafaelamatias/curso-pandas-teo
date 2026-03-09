

# %%

import pandas as pd

# %%

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head()

# %%

# 3.01 Quantas linhas há no arquivo clientes.csv ?

linhas, colunas = clientes.shape
print("Número de linhas:", linhas)

# %%

# 3.04 Qual o id do cliente no índice 4 no arquivo clientes.csv ?

clientes["idCliente"][4]

# %%

# 3.05 Qual o saldo de pontos do cliente na 10a posição (sem ordenar) do arquivo clientes.csv ?

clientes.iloc[10]["qtdePontos"]

# %%

# 4.01 Quantos clientes tem vínculo com a Twitch?

filtro = (clientes["flTwitch"] == 1)
clientes[filtro].shape
print("Número de clientes com Twitch:", clientes[filtro].shape[0])

# %%

# 04.02 - Quantos clientes tem um saldo de pontos maior que 1000?

filtro =(clientes["qtdePontos"] > 1000)
clientes[filtro]
print("Clientes com mais de 1000 pontos:" , clientes[filtro].shape[0])


# %%



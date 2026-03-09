# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df.head()

# %%
# valores maiores que 50 na coluna QtdePontos

pontos = df['QtdePontos'] >= 50 # filtro simples
df[pontos]

# %%
# valores entre 50 e 100 na coluna QtdePontos

pontos_2 = (df['QtdePontos'] >= 50) & (df['QtdePontos'] < 100) # filtro com dois critérios / também da pra usar o *
df[pontos_2]

# %%
# valores iguais a 1 ou 100 na coluna QtdePontos

pontos_3 = (df['QtdePontos'] == 1) | (df['QtdePontos'] == 100) # filtro com dois critérios / também da pra usar o |
df[pontos_3]
# %%
# valores entre 1 e 100 na coluna QtdePontos e que a coluna DescSistemaOrigem seja igual a 'twitch'

pontos_4 = ((df['QtdePontos'] >= 1 ) & (df['QtdePontos'] <= 100) & (df['DescSistemaOrigem'] == 'twitch')) 
df[pontos_4]

# %%

# %%

import pandas as pd
import numpy as np

df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()


# %%
# Criando uma nova coluna com valor fixo

df['pontos_100'] = df['qtdePontos'] + 100
df.head()

# %%

# Criando uma nova coluna com valor condicional

df['emailTwitch'] = df['flEmail'] + df['flTwitch'] 
df.head()

# %%

df['flEmail'] + df['flTwitch'] + df['flYouTube'] + df['flBlueSky'] + df['flInstagram']



# %%

df['quantidade_social'] = df['flEmail'] + df['flTwitch'] + df['flYouTube'] + df['flBlueSky'] + df['flInstagram']
df.head()
# %%

df['todas_social'] = df['flEmail'] * df['flTwitch'] * df['flYouTube'] * df['flBlueSky'] * df['flInstagram']
df.head()
# %%

df['qtdePontos'].describe()

# %%

df['logPontos'] = np.log(df['qtdePontos'])


# %%

df['logPontos'].describe()  # Estatísticas resumidas
df['logPontos'].value_counts().sort_index().head(10)  # Distribuição das 10 primeiras barras

# %%

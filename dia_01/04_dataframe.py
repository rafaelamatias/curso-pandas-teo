
# %%

import pandas as pd


idades = [
        1, 29, 40, 25, 5, 6, 7, 8, 
        9, 10, 12, 12, 13, 14, 15
        ]

nomes = [ "Ana", "Bruno", "Carlos", "Daniel", "Eduardo",
            "Fabiana", "Gabriel", "Heloisa", "Igor", "Juliana",
            "Karla", "Larissa", "Marcos", "Natália", "Olívia"
          ] 


series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)

# %%

df = pd.DataFrame()
df['Idades'] = series_idades
df['Nomes'] = nomes


type(df)
# %%


df.iloc[0]  # consulta pela posição


# %%

df['Nomes'] # consulta pela coluna

# %%

df.iloc[0]['Nomes']  # consulta pela posição e coluna
# %%

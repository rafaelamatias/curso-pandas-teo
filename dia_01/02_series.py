# %%

idades = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

media_idade = sum(idades) / len(idades)

print("A média das idades é:", media_idade)

# %%

import pandas as pd

idades = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

serie_idades = pd.Series(idades)
serie_idades 

# %%
# Estatísticas descritivas

medias_idades = serie_idades.mean()
medias_idades

var_idades = serie_idades.var()
var_idades

sumary_idades = serie_idades.describe()
sumary_idades

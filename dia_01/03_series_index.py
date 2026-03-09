# %%

import pandas as pd

idades = [
        1, 29, 40, 25, 5, 6, 7, 8, 
        9, 10, 12, 12, 13, 14, 15
        ]

serie_idades = pd.Series(idades)
serie_idades 

# %% 
# a grande diferença do Series é o índice que muda de acordo com a posição dos dados, 
# então para consultar tipo serie_idades[0] é 1, serie_idades[1] é 29 e assim por diante.

serie_idades = serie_idades.sort_values()
serie_idades

# %%


serie_idades.iloc[-1]  # consulta pelo índice padrão (posição)

# %%

serie_idades.iloc[:3]



# %%

idades = [
        1, 29, 40, 25, 5, 6, 7, 8, 
        9, 10, 12, 12, 13, 14, 15
        ]

indexes = [ "Ana", "Bruno", "Carlos", "Daniel", "Eduardo",
            "Fabiana", "Gabriel", "Heloisa", "Igor", "Juliana",
            "Karla", "Larissa", "Marcos", "Natália", "Olívia"
          ] 

series_idades = pd.Series(idades, index=indexes)
series_idades

# %%

series_idades["Olívia"] 
# %%

import pandas as pd
from requests import head

df = pd.read_csv("../data/clientes.csv ", sep=";")
df.head()   

# %%
# aplica uma função a cada elemento da coluna "idCliente"

def get_last_id(x):
    return x.split("-")[-1]

df["idCliente"].apply(get_last_id)
# %%

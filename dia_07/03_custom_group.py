# %%

import pandas as pd
import numpy as np

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()
# %%

def diff_amp(x: pd.Series):
    amplitude = x.max() - x.min()
    media = x.mean()
    return np.sqrt((amplitude - media) ** 2)
    
# %%

(transacoes.groupby(by=["IdCliente"])
            .agg({
                "IdTransacao": ["count"], 
                "QtdePontos": ["sum", "mean", diff_amp]})
            )
# %%

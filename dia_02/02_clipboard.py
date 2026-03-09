# %%

import pandas as pd


df = pd.read_clipboard(sep=';')  # Lê os dados da área de transferência com separador ponto e vírgula
df  # Exibe o DataFrame lido

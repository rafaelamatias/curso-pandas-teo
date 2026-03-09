# %%

import pandas as pd
import requests

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)
response.raise_for_status()  # garante que deu certo

dfs = pd.read_html(response.text)

dfs[1]  # primeira tabela
# %%
df_uf = dfs[1]

df_uf.to_csv("unidades_federativas.csv", index=False)  # Salva o DataFrame em um arquivo CSV sem o índice
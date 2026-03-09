# %%

from copy import replace

import pandas as pd
import requests

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" 
}

response = requests.get(url, headers=headers)
response.raise_for_status()  # garante que deu certo

dfs = pd.read_html(response.text)

uf = dfs[1]

# %%

def str_to_float(x:str):
    x = (x.replace(" ", "")
              .replace(",", ".")
              .replace("\xa0", ""))
    return float(x)


# %%

uf["Área (km²)"] = uf["Área (km²)"].apply(str_to_float)
uf["População (Censo 2022)"] = uf["População (Censo 2022)"].apply(str_to_float)
uf["PIB (2015)"] = uf["PIB (2015)"].apply(str_to_float)
uf["PIB per capita (R$) (2015)"] = uf["PIB per capita (R$) (2015)"].apply(str_to_float)

# %%

uf.head()
uf.dtypes

# %%

def mortalidade_to_float(x:str):
    x = float(x.replace("‰", "")
         .replace(",", ".")
         ) / 1000
    return x


# %%

uf["Mortalidade infantil (2016)"] = uf["Mortalidade infantil (2016)"].apply(mortalidade_to_float)
uf["Mortalidade infantil (2016)"]

# %%

def classifica_bom(linha):
    return (linha["PIB per capita (R$) (2015)"] > 30000
            and linha["Mortalidade infantil (2016)"] < 15
            and linha["IDH (2010)"] > 700
            )

# %%

uf.apply(classifica_bom, axis=1) # axis=1 para aplicar a função linha a linha, e não coluna a coluna

# %%

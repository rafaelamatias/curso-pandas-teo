
# %%

import pandas as pd

# %%

produtos = pd.read_csv("../data/produtos.csv", sep=";")
produtos.head()

# %%

# 03.03 - Quantas colunas do tipo object há no arquivo produtos.csv ?

object = produtos.select_dtypes(include="object").columns
print("Colunas do tipo object:", len(object))

# %%

# %%

import pandas as pd

# %%

df = pd.read_csv("dados_cartão.csv", sep=";")
df
# %%

df['dtTransacao'] = pd.to_datetime(df['dtTransacao']) # Converter a coluna 'dtTransacao' para o tipo datetime
df['vlParcela'] = df['vlVenda'] / df['qtParcelas'] # Criar a coluna 'vlParcela' dividindo o valor da venda pelo número de parcelas
df['ordemParcela'] = df.apply(lambda row: [i for i in range(row['qtParcelas'])], axis=1) # Criar a coluna 'ordemParcela' com uma lista de números de
df_explode = df.explode('ordemParcela') # Explodir a coluna 'ordemParcela' para criar uma linha para cada parcela
df_explode

# %%
def calcDtParcela(row):
    dt = row["dtTransacao"] + pd.DateOffset(months=row["ordemParcela"])
    dt =  f"{dt.year}-{dt.month}"
    return dt

df_explode["dtParcela"] = df_explode.apply(calcDtParcela, axis=1)
df_explode
# %%

(df_explode.groupby(["idCliente", "dtParcela"])
           ['vlParcela'].sum()
           .reset_index()
           .pivot_table(index='idCliente',
                        columns='dtParcela',
                        values='vlParcela',
                        fill_value=0))
# %%

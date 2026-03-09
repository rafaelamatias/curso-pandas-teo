
# %%

import pandas as pd

df = pd.read_csv('homicidios_consolidados.csv', sep=';')
df.head()
# %%

df_stack = (df.set_index(['nome', 'período']) # para definir as colunas 'nome' e 'período' como índice
            .stack() # para empilhar as colunas de métricas em uma única coluna
            .reset_index() # para resetar o índice e transformar as colunas de índice em colunas normais
            )
df_stack.columns = ['nome', 'período', 'métrica', 'valor'] # para renomear as colunas do DataFrame resultante

df_stack

# %%

df_unstack = (df_stack.set_index(['nome', 'período', 'métrica'])
                   .unstack()
                   .reset_index()
                   ) # para definir as colunas 'nome', 'período' e 'métrica' como índice

# %%

metricas = df_unstack.columns.droplevel(0)[2:].tolist() # para obter as métricas a partir das colunas do DataFrame resultante
df_unstack.columns = ['nome', 'período'] + metricas # para renomear as colunas do DataFrame resultante
df_unstack.head()
# %%

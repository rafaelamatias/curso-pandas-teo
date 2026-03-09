
# %%

import pandas as pd

transacoes = pd.read_csv('../data/transacoes.csv', sep=';')
transacoes.head()

# %%

clientes = pd.read_csv('../data/clientes.csv', sep=';')
clientes.head()

# %%

clientes = clientes.rename(columns={'idCliente': 'IdCliente'})

# %%

# Merge: junção de DataFrames
# O método merge() é utilizado para realizar junções entre DataFrames com base em uma ou mais colunas comuns. Ele é semelhante ao JOIN em SQL e permite combinar dados de diferentes fontes de maneira eficiente.

transacoes.merge(
    right=clientes,
    how='left', 
    on=['IdCliente'],
    suffixes=('_transacao', '_cliente')
)
# %%

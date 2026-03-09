# %%

import pandas as pd

# %%

transacoes = pd.read_csv('../data/transacoes.csv', sep=';')
transacoes.head()
# %%

transacao_produto = pd.read_csv('../data/transacao_produto.csv', sep=';')
transacao_produto.head()

# %%

produtos = pd.read_csv('../data/produtos.csv', sep=';')
produtos.head()

# %%

cliente_transacao_produto = transacoes.merge(
    transacao_produto,
    how='left',
    on=['IdTransacao']
)[['IdTransacao', 'IdCliente', 'IdProduto']] 

cliente_transacao_produto.head()

# %%

cliente_transacao_produto.dtypes

# %%
produtos.dtypes

# %% 

produtos['IdProduto'] = produtos['IdProduto'].astype('object')
produtos.dtypes
# %%

df_full = cliente_transacao_produto.merge(
    produtos,
    on=['IdProduto'],
    how='left',
)
df_full
# %%

df_full = df_full[df_full['DescNomeProduto'] == "Presença Streak"]
df_full.head()
# %%


produtos = produtos[produtos["DescNomeProduto"] == "Presença Streak"] # Filtrando o DataFrame produtos para conter apenas as linhas onde a coluna 'DescNomeProduto' é igual a "Presença Streak"
produtos.head()

teste =(transacoes.merge(transacao_produto, how='left',on=['IdTransacao']) # Realizando um merge entre os DataFrames transacoes e transacao_produto usando a coluna 'IdTransacao' como chave de junção. O tipo de junção é 'left', o que significa que todas as linhas do DataFrame transacoes serão mantidas, e as correspond
            .merge(produtos, how = 'right', on = ['IdProduto']) # Realizando um merge entre o resultado anterior e o DataFrame produtos usando a coluna 'IdProduto' como chave de junção. O tipo de junção é 'right', o que significa que todas as linhas do DataFrame produtos serão mantidas, e as correspondentes do resultado anterior serão combinadas.
            .groupby(by='IdCliente')['IdTransacao'] # Agrupando o DataFrame resultante pelo 'IdCliente' e contando o número de transações ('IdTransacao') para cada cliente.
            .count()
)
teste.head()
# %%

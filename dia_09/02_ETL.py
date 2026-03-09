# %%


import pandas as pd
import sqlalchemy


# %%

# Ler o arquivo SQL e armazenar a consulta em uma variável chamada 'query'
with open('etl.sql') as open_file:
    query = open_file.read()


print(query)


# %%

# Criar uma conexão com o banco de dados SQLite localizado no caminho '../data/olist.db'

engine = sqlalchemy.create_engine('sqlite:///../data/olist.db')


# %%

# Executar a consulta SQL armazenada na variável 'query' e armazenar os resultados em um DataFrame do pandas chamado 'df'
df = pd.read_sql_query(query, con=engine)


# %%
df
# %%

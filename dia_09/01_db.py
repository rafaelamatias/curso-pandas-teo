# %%

import pandas as pd

import sqlalchemy # uma biblioteca para trabalhar com bancos de dados relacionais

# %%

engine = sqlalchemy.create_engine('sqlite:///../data/olist.db') # criar uma conexão com o banco de dados, nesse caso um banco de dados SQLite localizado no caminho '../data/olist.db'

# %%

clientes = pd.read_sql_table(table_name = 'tb_customers', 
                             con = engine) # ler a tabela 'tb_customers' do banco de dados e armazenar os dados em um DataFrame do pandas chamado 'clientes'

# %%

clientes.head()
# %%

query = " SELECT * FROM tb_customers LIMIT 30" # criar uma consulta SQL para selecionar todos os dados da tabela 'tb_customers'

df_30 = pd.read_sql_query(query, con = engine) # executar a consulta SQL e armazenar os resultados em um DataFrame do pandas chamado 'df_30'
df_30

# %%






# %% 

import pandas as pd
import os # para acessar os arquivos do diretório

# função para ler os arquivos e organizar os dados

def read_file(file_name):
    df = (pd.read_csv(f"../../data/ipea/{file_name}.csv", sep=';')
            .rename(columns={'valor': file_name})
            .set_index(['nome', 'período'])
            .drop(['cod'], axis = 1)
            )
    
    return df

# %%

# listando os arquivos do diretório

file_names = os.listdir("../../data/ipea/")

#  criando uma lista de DataFrames a partir dos arquivos do diretório

dfs = []
for i in file_names:
    file_names = i.split('.')[0]
    dfs.append(read_file(file_names))

# %%

df_full = pd.concat(dfs, axis=1).reset_index().sort_values(by='período', ascending=False)
# %%
df_full.to_csv('homicidios_consolidados.csv', index=False, sep=';')

# %%

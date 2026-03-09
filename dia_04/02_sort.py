
# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head()
# %%

clientes['qtdePontos']
# %%

# Ordenando a série qtdePontos em ordem crescente

clientes['qtdePontos'].sort_values()

# %%
# Encontrando o(s) cliente(s) com a maior quantidade de pontos

max_pontos = clientes['qtdePontos'].max()
clientes_max = clientes[clientes['qtdePontos'] == max_pontos]
clientes_max

# %%
# Ordenando o DataFrame pelos pontos em ordem decrescente

clientes.sort_values(by='qtdePontos', ascending=False).head(10)
# %%

top_10 = (clientes.sort_values(by='qtdePontos', ascending=False).
          head(10)['idCliente']
)
top_10
# %%

brinquedo = pd.DataFrame(
    {
        'nome' : ['Boneca', 'Carrinho', 'Quebra-cabeça', 'Bola', 'Teddybear'],
        'preco' : [29.00, 29.00, 15.00, 10.00, 25.00],
        'quantidade' : [100, 150, 200, 300, 80]
    }
)

brinquedo
# %%
# Ordenando por preço (decrescente) e quantidade (decrescente)

brinquedo.sort_values(by=['preco', 'quantidade'], ascending=[False, False])
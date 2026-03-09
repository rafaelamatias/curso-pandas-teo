# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head()
# %%

# Filtro para clientes com qtdePontos igual a zero

filtro = clientes['qtdePontos'] == 0
clientes_0 = clientes[filtro]
clientes_0["flag_1"] = 1

# %%


A = [1, 2, 3]
B = A.copy() # cópia rasa (shallow copy)

print("A", A)
print("B", B)

B.append(4)
print("A", A)
print("B", B)

# %%

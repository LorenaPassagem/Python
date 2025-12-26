#%%
import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv")

df_clientes
# %% 
## Mostra as 5 primeiras linha o df
df_clientes.head()
## Mostra as 20 primeiras linha o df
df_clientes.head(n=20)
# %%
## Mostra as 5 ultima linha o df
df_clientes.tail()
# %%
## Mostra as 20 ultima linha o df
df_clientes.tail(n=20)
# %%
## 10 Amostra aleatória 
df_clientes.sample(10)

# %%
## Total de linha e colunas
## shape é um atributo
df_clientes.shape

# %%
## Nome das  colunas
df_clientes.columns
# %%
## info do DataFrame
df_clientes.info()
# %%

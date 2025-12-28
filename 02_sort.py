
#%%
import pandas as pd
clientes = pd.read_csv('../data/clientes.csv', sep=';')
clientes
#%%
## Maior quantidade de pontos
maximoPontos = clientes['qtdePontos'].max()
filtro = clientes['qtdePontos'] == maximoPontos
clientes[filtro]
#%%
## Menor quantidade de pontos
minimoPontos = clientes['qtdePontos'].min()
min = clientes['qtdePontos'] == minimoPontos
clientes[min]
# %%
## Os 5 primeiros com maior quantidade de pontos
clientes.sort_values(by='qtdePontos', ascending=False).head(5)
# %%


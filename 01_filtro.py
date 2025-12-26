#%%
import pandas as pd

df = pd.read_csv('../data/transacoes.csv', sep=';')
df.head()
# %%
## Quais transção tiveram mais de 50 pontos
filtro = df['QtdePontos'] > 50
# %%
df[filtro]
# %%
## Quais transação tiveram mais de 50 pontos e menor do que 100
filtro = (df['QtdePontos'] >= 50) & (df['QtdePontos'] < 100 ) 

df[filtro]

# %%
## Quais transação tiveram valores mais que 1 pontos e menor do que 100
filtro = (df['QtdePontos'] == 1) | (df['QtdePontos'] == 100 ) 

df[filtro]

# %%

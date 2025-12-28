#%%
import pandas as pd
import numpy as np
df = pd.read_csv('../data/clientes.csv', sep=';')

df.head()

# %%
## Adicionado 100 pontos para cada usuário  
df['Pontos_100'] = df['qtdePontos'] + 100
df.head()
# %%
## Criando um a coluna nova informado se a pessoa tem email ou twitch
df['flEmail'] +df['flTwitch']

# %%
df['EmailTwitch'] = df['flEmail'] + df['flTwitch']
df.head()
# %%
## intersecção entre email e twitch
df['EmailOUTwitch'] = df['flEmail'] * df['flTwitch']
df.head()
# %%
## Total de pessoas que tem duas redes social
df['duasRedesSocail'] = df['flEmail'] + df['flTwitch'] + df['flBlueSky'] + df['flInstagram']
filtroRede = df['TotalRedesSociais'] == 2
df[filtroRede]
# %%
## Pessaol tem ao menos  uma rede social
df['TotalRedesSociais'] = df['flEmail'] * df['flTwitch'] * df['flBlueSky'] * df['flInstagram']

#%% Introdução a biblioteca Numpy
np.log(df['qtdePontos'])
# %%

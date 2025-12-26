#%%
import pandas as pd

df = pd.read_csv('../data/transacoes.csv', sep=';')

## Quantas linhas esse df tem?
print ('Esse DF tem', df.shape[0], 'linhas')

## Quais os tipos de cada coluna?
print("Os tipos de cada coluna são", df.dtypes)
# %%
## Como renomear alguma coluna?
df.rename(columns={"QtdePontos": "qtPnt" , "DescSistemaOrigem": "Origem"}, inplace=True)
df
# %%
## Como acessar uma coluna especifica?
df['IdCliente']

# %%
## Agora quero 2 colunas -- vem em formato de um DF
df[['IdCliente', 'DtCriacao']]
# %%
## Trazendo amostras de 2 colunas
df[['IdCliente', 'DtCriacao']].sample(5)
    ## Inicio 
df[['IdCliente', 'DtCriacao']].head()
df
    ## Fim 
df[['IdCliente', 'DtCriacao']].tail()
df
# %%
## Ordenar  as colunas  em ordem alfabetica?
colunes = list(df.columns)
colunes.sort()
colunes

df = df[colunes]
df
# %%

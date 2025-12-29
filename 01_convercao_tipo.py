#%%
import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')
df
# %%
## Converter inteiro para float por exemplo
df['qtdePontos'].astype(str)
df['qtdePontos'].astype(str).astype(float)
# %%
## Converção de datas
## É possivel fragmentar em dia mês, ano...
dia = pd.to_datetime(df['DtCriacao']).dt.day
dia
#%%
dia_semana = pd.to_datetime(df['DtCriacao']).dt.day_of_week
dia_semana

# %%
data = pd.to_datetime(df['DtCriacao']).dt.date
data
# %%
mes = pd.to_datetime(df['DtCriacao']).dt.month
mes
# %%

#%%
## DataFrame - conjutos de séries
import pandas as pd

idades = [32, 38, 30, 30, 31, 35, 25, 29, 31, 37, 27, 23, 36, 33, 39]
nomes = ["Téo", "Maria", "Jose", "Luis", "Ana", "Nah", "Dani", "Mah",
         "Fer", "Nanda", "Naty", "Nih", "Pedro", "Kozato","Lorena"]


df = pd.DataFrame()

df['idades'] = idades
df

df['nomes'] = nomes
df
# %%
## Pegando todas as informações de uma linha do DataFrame
df.iloc[0]['idades']
# %%
## Quero a idade da ultima pessoa
df.iloc[-1]['idades']['nomes']

# %%

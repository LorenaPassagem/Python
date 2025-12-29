#%%
import pandas as pd

clientes = pd.read_csv('../data/clientes.csv', sep=';')
# %%
## Remover os na
clientes = clientes.dropna()
clientes
# %%
## A linha inteira tem que ser na
clientes = clientes.dropna(how='all')
clientes
# %%
dados = pd.DataFrame( {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo', 'Fernanda'],
    'Idade': [None, None, 27, 35, 41, 29],
    'Salario': [3200, 4500, 3800, 5200, None, 4700]
 }
)
dados
# %%
dados.dropna(how='any')
# %%
## remover os na so pelo criterio de idade
dados.dropna(how='all',subset=['Idade', 'Nome'])
# %%
## eliminado o NA com o fillna
##Para a Serie idade
media = dados['Idade'].mean()
dados['Idade'].fillna(media)
## Para o DF inteiro
## Aqui substitui o valor dos na pelo media das idade, como exemplo
dados.fillna(media)
# %%

dados.fillna({'Nome':'Alguem', 'Idade': 0})
dados
# %%

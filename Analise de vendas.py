#%%
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("loja_pedidos.csv")
df
# %%
"""Retirar o $ """
df['item_price'] = df['item_price'].str.replace('$', '').str.replace(' ', '1')
df['item_price']
#%%
""" O campo 'item_price' não tem NaN """
df.isna().any()
# %%
"""Convertendo o campo 'item_price' de object para float"""
df['item_price'] = df['item_price'].astype(float)
df['item_price'].sum()
# %%
df
# %%
df['Valor Total'] = df['item_price'] * df['quantity']
df
#%%
""" Fazendo o grafico com a lib. Matplotlib"""

x = df['item_name']
y = df['Valor Total']

plt.bar(x, y, label='Item mais vendidos', color='#207B6E')
plt.title('Item mais vendidos')
plt.xlabel('Valor Total')
plt.xticks(rotation = 45)
plt.ylabel('Item')

plt.show()
# %%

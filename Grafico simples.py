#%%
"""Nesse projeito inicial carreguei um arquivo em formato .csv com a biblioteca Pandas 
 e usei a biblioteca Matplotlib para fazer gráficos com os dados desse arquivo    """
import pandas as pd
import matplotlib.pyplot as plt

# %%
df = pd.read_csv('dados.csv')
df
# %%
"""Estica o gráfico"""
fig = plt.figure(figsize=(12, 8))

"""Carrega os dados do DataFrame criado acima  """
dias = df['Date']
petro = df['PETR4']
itau = df['ITUB4']

"""Criando os graficos com os dados  """
plt.plot(dias, petro, label ='Petro', color='green', linestyle='--', marker='.')
plt.plot(dias, itau, label ='Itau', color='gray', linestyle='--', marker='.')

""" Coloca um titulo no gráfico """
plt.title("Cotação - 2025/1")
"""Titulo nos eixos x e y"""
plt.xlabel('Dias')
plt.ylabel('Valor da ação (R$)')
""" Legenda para as linhas"""
plt.legend()

plt.show()
# %%

#Converta o seguinte dicionário para DataFrame e obtenha:
#Sumário de cada coluna
#Média da coluna idade
#Último nome da coluna nome
#%%
import pandas as pd
import numpy as np
#%%
dados = {'nome':[ "Téo", "Nah", "Napoleão"], 'idade': [31, 32, 14]}


# %%
df = pd.DataFrame(dados)
df

# %%

sumario = df.describe()
sumario
# %%
media = df['idade'].mean()
media
# %%
ultimo_nome = df['nome'].iloc[-1]
ultimo_nome
# %%
ultimonomediferente = df['nome'].tail(1)
ultimonomediferente
# %%

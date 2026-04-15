#%%%
import pandas as pd 
import numpy as np 
dados = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]
df = pd.DataFrame(dados)
df
# %%
media = df.mean()
media
# %%
desvio_padrao = df.std()
desvio_padrao
# %%
maior_numero = df.max()
maior_numero
# %%

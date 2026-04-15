#%%
import pandas as pd
import numpy as np
homicidios = pd.read_csv("../data/ipea/homicidios-mulheres-negras.csv", sep=";")
#%%
colunas_numero = homicidios.select_dtypes(include="number")
colunas_numero
# %%
colunas_objeto = homicidios.select_dtypes(include="object")
colunas_objeto
# %%
homicidios.info(memory_usage='deep')
# %%


# %%

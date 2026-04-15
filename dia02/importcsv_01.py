#%%
import pandas as pd
import numpy as np

homicidios = pd.read_csv("../data/ipea/homicidios.csv", sep=";")
# %%
quantidade_linhas = homicidios.shape[0]
quantidade_linhas
# %%
quantidade_colunas = homicidios.shape[1]
quantidade_colunas
# %%
nome_primeira_coluna = homicidios.columns[0]
nome_primeira_coluna
# %%
ou = homicidios.iloc[0]
ou
# %%
ultima_linha = homicidios.tail(1)
ultima_linha
# %%
ultima_coluna = homicidios.columns[-1]
ultima_coluna
# %%
homicidios.info(memory_usage='deep')
# %%

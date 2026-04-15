# %%
import pandas as pd


#%%
idades = [ 30, 40, 50, 60]
idades
#%%
idades = [ 30, 40, 50,60 ]
media = sum(idades) / len(idades)
total = 0
for i in idades:
    total += (media -i)**2
variancia = total / (len(idades) - 1)
print(f'{variancia}')
# %%
#%%
series_idades = pd.Series(idades)
series_idades.mean()

# %%
series_idades.var()

# %%
series_idades.median()

# %%
series_idades.sum
# %%
series_idades.describe()
# %%
series_idades.max()
# %%
series_idades.shape
# %%
idades[0]
#%%
series_idades

# %%
series_idades.index
# %%
series_idades.describe
# %%
series_idades.quantile(0.80)
# %%
series_idades.iloc[0]
# %%

#%%
series_idades.iloc[30]

# %%

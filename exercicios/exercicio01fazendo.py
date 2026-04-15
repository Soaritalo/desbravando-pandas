#%%
import pandas as pd
#%%
data = { "nome":["teo" , "nah", "lara","maria"],
        "sobrenome":["calvo","ataide", "calvo","calvo"],
        "idade":[31, 32, 31, 2]}
#%%
data["idade"][0]
# %%
df = pd.DataFrame(data)
df 
# %%
df["idade"]
# %%
type(df["idade"])
# %%
df["sobrenome"]

# %%
df["nome"].iloc[0]


# %%
df.iloc[2]
# %%
df.info()
# %%
df.info(memory_usage='deep')
# %%
df.dtypes
# %%
df['peso'] = [80, 53, 65 , 14]
sumario = df.describe()
# %%
sumario = df.describe()
sumario['peso']['mean']
# %%
df.head(2)
#%%
df.tail(2)
#%%
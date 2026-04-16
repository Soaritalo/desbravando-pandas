#%%
import pandas as pd
df = pd.read_csv("../data/products.csv", sep=";", names= ["id", "name", "Description"])
df
#%%
df = df.rename(columns={"Name":"Nome", "Description": "Descrição"})

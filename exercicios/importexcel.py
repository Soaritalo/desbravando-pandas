#%% 
import pandas as pd
df = pd.read_excel("../data/transactions.xlsx")
# %%
df.shape
# %%
df.head()
# %%
df.tail()
# %%
colunas = ("UUID","Points", "IdCustomer" , "DtTransaction", "Points")
# %%
df.info(memory_usage='deep')
# %%

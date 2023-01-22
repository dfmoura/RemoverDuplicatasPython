#!/usr/bin/env python
# coding: utf-8

# ### Remover Duplicatas Python

# In[14]:


lista = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]


# ### Forma mais simples: set

# In[16]:


lista = list(set(lista))
print(lista)


# ### Se a ordem importa: dict.fromkeys

# In[20]:


lista = [5, 5, 3, 3, 4, 4, 2, 2, 1, 1]
lista = list(dict.fromkeys(lista))
print(lista)


# ### Se for em um arquivo de dados

# In[27]:


import pandas as pd

produtos = pd.read_csv("Produtos.csv", sep=";")
produtos = produtos.drop_duplicates("Produto")
display(produtos)


# In[ ]:





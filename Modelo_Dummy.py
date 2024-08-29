#!/usr/bin/env python
# coding: utf-8

# ### Construindo modelo Dummy
# 
# Vamos trabalhar com uma série temporal (onde pra cada possivel data eu tenho um valor) e queremos prever o futuro dessa série, como:
# 
# - Prever a demanda de clientes nos próximos meses (pra cada possível mês) ou esse mês mesmo antes que ele chegue no final. 
# 
# Esse modelo é importante pois é a análise mais simples que pode ser feita. 
# 

# In[2]:


import pandas as np
import matplotlib.pyplot as plt
import pandas as pd


# https://dadosabertos.bcb.gov.br/dataset/27742-saldo-das-operacoes-de-credito-por-atividade-economica---servicos-financeiros
# 
# dados utilizados do site 
# 
# Campo: Tipo da série, Unidade de medida, Código SGS </br>
# Valor: Série temporal mensal, Milhões de reais, 27743

# In[14]:


get_ipython().system(' pip install pandas')


# In[16]:


df = pd.read_csv(r'C:\Users\vivia\OneDrive\Área de Trabalho\DATA SCIENCE\Flai Inteligencia Artificial - DS\Formação 2 - Machine Learning O Caminho do Cientista de Dados\01 - Fundamentos de Machine Learning\702c9871-576b-41c6-9748-9ab760759f40\bcdata.sgs.27743.csv', sep=';')
df.loc[:,'data'] = pd.to_datetime(df.data, format='%d/%m/%Y')
df


# In[ ]:


plt.figure(figsize=(15,5))
plt.plot(df.data, df.valor)


# In[ ]:


plt.figure(figsize=(15,5))
plt.plot(df.data, df.valor, ".-")
plt.grid()


# In[ ]:


df.iloc[df.data>'2020-01-01'].iloc[0].valor # fica mais fácil de ser usado


# In[ ]:


df.iloc[df.data>'2020-01-01']


# In[ ]:


df.iloc[df.data>'2020-01-01'].valor.iloc[0]


# In[ ]:


df.iloc[df.data>'2020-01-01'].valor.loc[97]


# In[ ]:


predicoes = []
erros = []

for dat in df.data:
    valor = df.loc[ df.data==dat ].valor.iloc[0]
    pred  = df.loc[ df.data==(dat-pd.DateOffset(moths=1))].valor.iloc[0]
    
    predicoes.append( pred)
    erros.append(pred-valor)
    
    # Ele vai dar erro pois 
    pred  = df.loc[ df.data==(dat-pd.DateOffset(moths=1))].valor.iloc[0] 
    # vai mostrar algo antes de 2012, mas não tem dados antes dessa data 


# In[ ]:


predicoes = []
erros = []

for dat in df.data:
    if dat == pd.to_datetime('2012-01-01'):
        erros.append(np.nan)
        predicoes.append(np.nan)
        continue
    
    
    valor = df.loc[ df.data==dat ].valor.iloc[0]
    pred  = df.loc[ df.data==(dat-pd.DateOffset(moths=1))].valor.iloc[0]
    
    predicoes.append( pred)
    erros.append(pred-valor)


# In[ ]:


predicoes


# In[ ]:


df_pred = pd.DataFrame()
df_pred.loc[:, 'data'] = df.data
df_pred


# In[ ]:


df_pred = pd.DataFrame()
df_pred.loc[:, 'data'] = df.data
df_pred.loc[:, 'valor'] = df.valor
df_pred.loc[:, 'predicoes'] = predicoes
df_pred.loc[:, 'erros'] = erros
df_pred


# In[ ]:


plt.figure(figsize=(15,5))
plt.plot(df_pred.data, df_pred.erros, '.-')
plt.grid()
plt.xlim(left=pd.to_datetime('2020-01-01'))


# In[ ]:


plt.figure(figsize=(15,5))
plt.plot(df_pred.data, df_pred.valor, 'b.-')
plt.plot(df_pred.data, df_pred.predicoes, 'g.-')
plt.grid()


# In[ ]:


df.loc[:,'predicoes'] = df.valor.shift(1)
df


# In[ ]:


df.loc[:, 'erro'] = df.predicoes - df.valor
df


# In[ ]:


df_pred


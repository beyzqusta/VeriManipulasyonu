#!/usr/bin/env python
# coding: utf-8

# ### Pandas 2

# In[7]:


import numpy as np
import pandas as pd
m=np.random.randint(1,10,size=(10,3))
df1=pd.DataFrame(m,columns=["var1","var2","var3"])
df1


# In[3]:


df[df.var1>3]


# In[4]:


df[df.var2>6]["var3"]


# In[5]:


df.loc[(df.var1<8),["var1","var2"]]


# In[8]:


df2=df1+41
df2


# In[10]:


pd.concat([df1,df2]) # dataframeleri birleştirir


# In[11]:


pd.concat([df1,df2], ignore_index=True) #index problemini çözer  


# In[13]:


df1=pd.DataFrame({'calisanlar':['ali','veli','ayse','fatma'], 'grup':['muhasebe','muhendislik','muhendislik','İK'] })
df2=pd.DataFrame({ 'calisanlar':['ali','veli','ayse','fatma'],'girisyili': [2010,2009,2013,2019]})
pd.merge(df1,df2)


# In[14]:


df3=pd.merge(df1,df2)
df4=pd.DataFrame({ 'grup':['muhasebe','muhendislik','muhendislik','İK'], 'mudur': ['beyza','emre','eymen','emine']})
pd.merge(df3,df4)


# In[16]:


df5=pd.merge(df3,df4)
df6=pd.DataFrame({'grup':['muhasebe','muhendislik','muhendislik','İK','İK','muhendislik'],'yetenek': ['excel','python','linux','matematik','kodlama','excei']})
pd.merge(df5,df6)


# In[ ]:





# In[19]:


df=pd.DataFrame({"gruplar":["a","b","c","a","b","c"], "veri":[10,20,33,45,85,74]} , columns=["gruplar","veri"])
df.groupby("gruplar").mean()
df.groupby("gruplar").sum()


# In[27]:


df=pd.DataFrame({"gruplar":["a","b","c","a","b","c"], "degisken1": [10,20,30,40,50,60], "degisken2": [100,200,300,400,500,600]} , columns=["gruplar","degisken1","degisken2"])
df.groupby("gruplar").aggregate("min","max")


# In[29]:


df.groupby("gruplar").aggregate({"degisken1":"min","degisken2":"max"})


# In[30]:


df.groupby("gruplar").std()


# In[31]:


df.apply(np.sum)


# In[ ]:





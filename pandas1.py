#!/usr/bin/env python
# coding: utf-8

# ### Pandas
# 

# In[2]:


# Numpy Arraylerinden farklı olarak pandasta değerler indexleri ile birlikte tutulur


# In[3]:


import pandas as pd


# In[11]:


seri=pd.Series([1,5,8,9,6,7,14])
seri


# In[13]:


seri.axes # index bilgileri (0dan 5 e kadar)


# In[14]:


seri.size #eleman sayısı


# In[15]:


seri.ndim #boyutu


# In[16]:


seri.values # array şeklinde erişmemizi sağlar


# In[17]:


seri.head(2) #ilk iki elemanı getirir


# In[19]:


seri.tail(3) #sondan üçünü getirir


# In[24]:


seri=pd.Series([5,8,7,9,45,65,25,74,12,13,36,59,67], index=[1,2,3,4,5,6,7,8,9,10,11,12,13])
seri


# In[ ]:





# #### DATA FRAME OLUŞTURMA
# 

# In[27]:


import pandas as pd
l=[1,2,3,4,5,6]
a=pd.DataFrame(l,columns=["degisken"])
a


# In[28]:


import numpy as np
m=np.arange(1,10).reshape((3,3))
b=pd.DataFrame(m,columns=["var1","var2","var3"])
b


# In[30]:


b.columns=("deg1","deg2","deg3") #ismini değiştirdik
b


# In[32]:


s1=np.random.randint(10,size=5)
s2=np.random.randint(10,size=5)
s3=np.random.randint(10,size=5)
sozluk={"var1":s1,"var2":s2,"var3":s3}
df=pd.DataFrame(sozluk)
df                                        #sozluk kullanarak dataframe oluşturuldu


# In[34]:


df.drop(1,axis=0,inplace=True)  #inplace kullanılmazsa dataframede kalıcı silinmez
df


# In[36]:


m=np.random.randint(1,30,size=(10,3))
df=pd.DataFrame(m,columns=["var1","var2","var3"])
df


# In[37]:


#loc : tanımlandığı şekil ile kullanılır
#iloc : alışık olunan index ile seçim yapar


# In[39]:


df.iloc[0:3] # o dan 3e kadar sayar (0. , 1. , 2. indexi sayar)


# In[40]:


df.loc[0:3] # 0 ile 3. indexi sayar (0. , 1. , 2. , 3. indexi sayar)


# In[42]:


df.loc[0:3,"var2"] #iloc ile var3 yazarak aratma yapamayız


# In[ ]:





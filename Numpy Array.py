#!/usr/bin/env python
# coding: utf-8

# ### NUMPY ARRAY

# In[19]:


import numpy as np


# In[4]:


np.array([1,2,3])


# In[18]:


np.arange(0,30,3) #arange ile iki değer arası sayılar oluşturulabilir


# In[10]:


np.linspace(0,1,10) #linspace


# In[13]:


# ndim=boyut sayısı
# shape=boyut bilgisi
# size=toplam eleman sayısı
# dtype=veri tipi


# In[ ]:


np.random.randint(0,10,(3,5))


# In[41]:


np.random.randint(0,10,(3,5,))
a=np.random.randint(0,10,(3,5,))
a.ndim


# In[45]:


a.shape


# In[42]:


a.size


# In[40]:


a.dtype


# ### Reshaping

# In[49]:


np.arange(1,10)
np.arange(1,10).reshape(3,3)
#TEK BOYUTLU MATRİSİ 3 BOYUTLUYA YENİDEN ŞEKİLLENDİRİR


# ### Concatenation

# In[57]:


x=np.array([1,2,4])
y=np.array([5,8,6])
# arrayleri birleştirir


# In[60]:


np.concatenate([x,y]) 


# ### Splitting

# In[59]:


x=np.array([1,2,3,4,5,6,7,8,9])
np.split(x,[3,5]) # arrayi 3 e kadar ayırır sonra 5 e kadar ayırır 


# ### Short

# In[62]:


v=np.array([1,5,7,6,45,87,99,12,365,58,10,236,78])
np.short(v) #arrayi küçükten büyüğe sıralar


# In[ ]:





# ### index ile elemana erişme

# In[65]:


a=np.random.randint(10,size=(3,5))
a


# In[66]:


a[0][0]


# In[67]:


a[1][4]


# In[68]:


a[2][4]=10 #elemenanını değiştirdik


# In[69]:


a


# ### Array Alt Küme (Slicing)

# In[71]:


a=np.random.randint(10,size=(5,5))
a


# In[72]:


a[:,0] #0. sütun


# In[73]:


a[0] #0.satır


# In[74]:


a[0:2 , 0:3] #0 dan 2 ye kadar satırlar 0 dan 3 e kadar sütunlar


# In[76]:


a[::,:2] #tüm satırları al ve ilk iki sütunu al


# In[ ]:





# In[79]:


b=np.random.randint(10,size=(5,5))
b


# In[81]:


alt_a=b[0:3 , 0:5 ]
alt_a


# In[82]:


alt_a[0,0]=15
alt_a[1,3]=18
alt_a


# ### Fancy İndex

# In[84]:


v=np.array([3,6,9,12,74,875,98,26,65,41,23,31,68,71,12,16,39,95])
a=[1,3,12] #fancy index 
v[a]


# ### matematiksel işlemler 

# In[86]:


e=np.random.randint(15,size=(3,8))
e


# In[87]:


e*5


# In[88]:


e/5*7-5+4


# In[89]:


np.subtract(e,4) #cikarma


# In[90]:


np.add(e,45) #toplama


# In[91]:


np.multiply(e,3) #çarpma


# In[92]:


np.divide(e,2) #bölme


# In[93]:


e**2 #karesini alır


# In[94]:


np.power(e,3) 


# In[95]:


np.mod(e,3) #modunu alır


# In[ ]:





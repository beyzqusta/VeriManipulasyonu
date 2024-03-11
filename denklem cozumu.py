#!/usr/bin/env python
# coding: utf-8

# ### İki bilinmeyenli Denklem

# #### 5 * x0 + x1=12
# #### x0 + 3 * x1=10

# In[2]:


import numpy as np


# In[5]:


a=np.array([[5,1],[1,3]])


# In[6]:


b=np.array([12,10])


# In[7]:


x=np.linalg.solve(a,b)
x


# In[ ]:





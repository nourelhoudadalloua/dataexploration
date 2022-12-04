#!/usr/bin/env python
# coding: utf-8

# Chapter 1 : Data Exploration and Cleaning 
# Book : Data Science with python case studies

# In[2]:


import pandas as pd


# In[3]:


df = pd.read_excel("C://Users//nourd//Downloads//default_of_credit_card_clients__courseware_version_1_21_19.xls")


# In[4]:


df.head().T


# In[10]:


#inspect for null values 
df.info() 
len(df)


# In[5]:


len(df)


# In[6]:


df.describe()


# In[7]:


df.columns


# In[10]:


df['ID'].nunique()


# In[11]:


df.shape


# In[18]:


id_counts = df['ID'].value_counts() 


# In[19]:


id_counts.value_counts()


# In[ ]:





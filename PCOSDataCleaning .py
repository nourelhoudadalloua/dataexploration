#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


import numpy as np 


# In[4]:


import matplotlib.pyplot as plt


# In[5]:


import seaborn as sns 
sns.set()


# In[6]:


import warnings
warnings.filterwarnings('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[47]:


PCOS_inf = pd.read_csv("C://Users//nourd//OneDrive//Documents//Datasets//PCOS_infertility.csv") 
PCOS_inf.head()


# In[48]:


PCOS_inf.info()


# In[30]:


PCOS_data = pd.read_excel("C://Users//nourd//OneDrive//Documents//Datasets//PCOS_data_without_infertility.xlsx",sheet_name = "Full_new")
PCOS_data.head().T


# In[31]:


PCOS_data.info() 
#mariage status contains one single missing value as well as fast food 
#PCOS is of float type 
#unamed variable have all null values exept for two  
#----
#convert to categorical variables 
#too many lines of a code for a single operation it can be reduced to a function  

#PCOS_data['PCOS (Y/N)']=PCOS_data['PCOS (Y/N)'].astype('category')
#PCOS_data['Weight gain(Y/N)']=PCOS_data['Weight gain(Y/N)'].astype('category')
#PCOS_data['hair growth(Y/N)']=PCOS_data['hair growth(Y/N)'].astype('category')
#PCOS_data['Skin darkening (Y/N)']=PCOS_data['Skin darkening (Y/N)'].astype('category')
#PCOS_data['Hair loss(Y/N)']=PCOS_data['Hair loss(Y/N)'].astype('category')
#PCOS_data['Pimples(Y/N)']=PCOS_data['Pimples(Y/N)'].astype('category')
#PCOS_data['Fast food (Y/N)']=PCOS_data['Fast food (Y/N)'].astype('category')
#PCOS_data['Reg.Exercise(Y/N)']=PCOS_data['Reg.Exercise(Y/N)'].astype('category')  

#function to vonvert to category 
def category_conversion(df,*args): 
    df[args].astype('category')


# In[33]:


PCOS_data.info()


# In[34]:


PCOS_data['Marraige Status (Yrs)'].value_counts()


# In[13]:


PCOS_data[PCOS_data['Marraige Status (Yrs)'].isnull()].T 


# In[35]:


PCOS_data[~ PCOS_data['Unnamed: 44'].isna()].T


# In[36]:


#lets assign the median to the missing data
PCOS_data['Marraige Status (Yrs)'].fillna(PCOS_data['Marraige Status (Yrs)'].median(),inplace=True) 
PCOS_data['Marraige Status (Yrs)'].isnull().sum()


# In[37]:


PCOS_data['Fast food (Y/N)'].fillna(PCOS_data['Fast food (Y/N)'].median(),inplace=True)
PCOS_data['Fast food (Y/N)'].isnull().sum()


# In[38]:


PCOS_data.drop('Unnamed: 44',axis=1,inplace=True)


# In[39]:


PCOS_data.head()


# In[45]:


PCOS_inf.head()


# In[49]:


PCOS_inf.info()


# In[43]:


#convert the variables to category data type 
#PCOS_inf['PCOS (Y/N)'] = PCOS_inf['PCOS (Y/N)'].astype('category')  


# In[50]:


PCOS_inf.info()


# In[51]:


#merge the two datasets 
data = pd.merge(PCOS_data,PCOS_inf, on='Patient File No.', suffixes={'','_y'},how='left')


# In[52]:


data.head().T


# In[53]:


data.columns


# In[59]:


data[['Sl. No_y','PCOS (Y/N)_y','AMH(ng/mL)_y']].isnull().sum()/len(data) * 100 
data[['  I   beta-HCG(mIU/mL)_y','II    beta-HCG(mIU/mL)_y']].isnull().sum()/len(data) * 100
#all the columns have null value so we should drop the column 


# In[65]:


data.drop(['  I   beta-HCG(mIU/mL)_y','II    beta-HCG(mIU/mL)_y'],axis=1,inplace=True)


# In[67]:


data.info()


# In[68]:


PCOS_data.shape


# In[69]:


data.shape


# In[71]:


data.describe().T


# In[73]:


from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
target = data['PCOS (Y/N)']
data.drop('PCOS (Y/N)',axis=1,inplace=True)


# In[74]:


target


# In[75]:


plt.figure(figsize=(8,7))
sns.countplot(target)
plt.title('Data imbalance')
plt.show()


# In[76]:


X_train,X_test, y_train, y_test = train_test_split(data, target, test_size=0.15, random_state=1, stratify = target)
X_train,X_valid, y_train, y_valid =  train_test_split(X_train, y_train, test_size=0.3, random_state=1, stratify=y_train)


# In[77]:


from sklearn.metrics import roc_auc_score
def print_scores(m):
    res = [roc_auc_score(y_train,m.predict_proba(X_train)[:,1]),roc_auc_score(y_valid,m.predict_proba(X_valid)[:,1])]
    for r in res:
        print(r)  
        


# In[78]:


rf = RandomForestClassifier(n_jobs=-1,n_estimators=150,max_features='sqrt',min_samples_leaf=10)
rf.fit(X_train,y_train)
print_scores(rf)


# In[ ]:





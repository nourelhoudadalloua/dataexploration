#!/usr/bin/env python
# coding: utf-8

# # Chapter 1
# 
# Examples and Exercises from Think Stats, 2nd Edition
# 
# http://thinkstats2.com
# 
# Copyright 2016 Allen B. Downey
# 
# MIT License: https://opensource.org/licenses/MIT
# 

# In[1]:


from os.path import basename, exists


def download(url):
    filename = basename(url)
    if not exists(filename):
        from urllib.request import urlretrieve

        local, _ = urlretrieve(url, filename)
        print("Downloaded " + local)


download("https://github.com/AllenDowney/ThinkStats2/raw/master/code/thinkstats2.py")
download("https://github.com/AllenDowney/ThinkStats2/raw/master/code/thinkplot.py")


# In[2]:


download("https://github.com/AllenDowney/ThinkStats2/raw/master/code/nsfg.py")

download("https://github.com/AllenDowney/ThinkStats2/raw/master/code/2002FemPreg.dct")
download(
    "https://github.com/AllenDowney/ThinkStats2/raw/master/code/2002FemPreg.dat.gz"
)


# ## Examples from Chapter 1
# 
# Read NSFG data into a Pandas DataFrame.

# In[3]:


import nsfg


# In[4]:


preg = nsfg.ReadFemPreg()
preg.head()


# Print the column names.

# In[5]:


preg.columns


# Select a single column name.

# In[6]:


preg.columns[1]


# Select a column and check what type it is.

# In[7]:


pregordr = preg['pregordr']
type(pregordr)


# Print a column.

# In[8]:


pregordr


# Select a single element from a column.

# In[9]:


pregordr[0]


# Select a slice from a column.

# In[10]:


pregordr[2:5]


# Select a column using dot notation.

# In[11]:


pregordr = preg.pregordr


# Count the number of times each value occurs.

# In[12]:


preg.outcome.value_counts().sort_index()


# Check the values of another variable.

# In[13]:


preg.birthwgt_lb.value_counts().sort_index()


# Make a dictionary that maps from each respondent's `caseid` to a list of indices into the pregnancy `DataFrame`.  Use it to select the pregnancy outcomes for a single respondent.

# In[14]:


caseid = 10229
preg_map = nsfg.MakePregMap(preg)
indices = preg_map[caseid]
preg.outcome[indices].values 


# ## Exercises

# Select the `birthord` column, print the value counts, and compare to results published in the [codebook](ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NSFG/Cycle6Codebook-Pregnancy.pdf)

# In[17]:


preg.birthord.value_counts()


# We can also use `isnull` to count the number of nans.

# In[18]:


preg.birthord.isnull().sum()


# Select the `prglngth` column, print the value counts, and compare to results published in the [codebook](ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NSFG/Cycle6Codebook-Pregnancy.pdf)

# In[19]:


preg.prglngth.value_counts()


# To compute the mean of a column, you can invoke the `mean` method on a Series.  For example, here is the mean birthweight in pounds:

# In[20]:


preg.birthord.mean()


# Create a new column named <tt>totalwgt_kg</tt> that contains birth weight in kilograms.  Compute its mean.  Remember that when you create a new column, you have to use dictionary syntax, not dot notation.

# In[23]:


preg['totalwgt_kg'] = (preg['birthwgt_lb'] + preg['birthwgt_oz'])*0.45359237 


# `nsfg.py` also provides `ReadFemResp`, which reads the female respondents file and returns a `DataFrame`:

# In[24]:


download("https://github.com/AllenDowney/ThinkStats2/raw/master/code/2002FemResp.dct")
download("https://github.com/AllenDowney/ThinkStats2/raw/master/code/2002FemResp.dat.gz")


# In[25]:


resp = nsfg.ReadFemResp()


# `DataFrame` provides a method `head` that displays the first five rows:

# In[26]:


resp.head()


# Select the `age_r` column from `resp` and print the value counts.  How old are the youngest and oldest respondents?

# In[ ]:





# We can use the `caseid` to match up rows from `resp` and `preg`.  For example, we can select the row from `resp` for `caseid` 2298 like this:

# In[ ]:


resp[resp.caseid==2298]


# And we can get the corresponding rows from `preg` like this:

# In[ ]:


preg[preg.caseid==2298]


# How old is the respondent with `caseid` 1?

# In[ ]:





# What are the pregnancy lengths for the respondent with `caseid` 2298?

# In[ ]:





# What was the birthweight of the first baby born to the respondent with `caseid` 5012?

# In[ ]:





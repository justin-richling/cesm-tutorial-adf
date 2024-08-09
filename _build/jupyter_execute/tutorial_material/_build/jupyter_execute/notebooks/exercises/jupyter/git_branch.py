#!/usr/bin/env python
# coding: utf-8

# # Choosing Different Git Branch
# 
# If you plan on working with the ADF in Jupyter in. adevelopmental capacity, sometimes it is necessary to work in different branches. This can be problematic or a hassle but can be done for JupyterHub with a couple extra steps:
# 
# 1) Locally, navigate to where your ADF main/development branches exist
# 2) 

# In[4]:


#adf_path = "/glade/work/{user}/ADF" # <-- uncomment and use your username
adf_path = "/glade/work/richling/ADF/ADF/" # <-- then comment out

#print(f"current working directory = {local_path}")
print(f"ADF path                  = {adf_path}")


# In[5]:


import os


# In[6]:


os.chdir(adf_path)


# In[7]:


pwd


# In[8]:


get_ipython().system('git branch')


# In[9]:


get_ipython().system('git checkout tem-diagnostics')


# In[10]:


get_ipython().system('git branch')


# In[ ]:





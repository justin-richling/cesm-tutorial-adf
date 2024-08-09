#!/usr/bin/env python
# coding: utf-8

# # ADF in Jupyter
# 
# Let's take a look at how to run the ADF in Jupyter notebooks
# 
# This can be done through JupyterHub or locally as a Jupyter Notebook

# <html>
#    <body>
#       <h3> Using the <em> download attribute of a tag </em> to create file download button using JavaScript. </h3>
#       <p> Click the below button to download this Jupyter Notebook</p>
#       <a href = "notebooks/basic_examples/run/jupyter.ipynb"
#       Download = "test_image">
#          <button type = "button"> Download </button>
#       </a>
#    </body>
# </html>

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')

import os.path
from pathlib import Path
import sys


# In[2]:


# Determine ADF directory path
# If it is in your cwd, set adf_path = local_path, 
# otherwise set adf_path appropriately

local_path = os.path.abspath('')


# In[9]:


#adf_path = "/glade/work/{user}/ADF" # <-- uncomment and use your username
adf_path = "/glade/work/richling/ADF/ADF/" # <-- then comment out

print(f"current working directory = {local_path}")
print(f"ADF path                  = {adf_path}")


# In[10]:


#set path to ADF lib
lib_path = os.path.join(adf_path,"lib")
print(f"The lib scripts live here, right? {lib_path}")

#set path to ADF plotting scripts directory
plotting_scripts_path = os.path.join(adf_path,"scripts","plotting")
print(f"The plotting scripts live here, right? {plotting_scripts_path}")

#Add paths to python path:
sys.path.append(lib_path)
sys.path.append(plotting_scripts_path)


# In[11]:


#import ADF diagnostics object
from adf_diag import AdfDiag

# If this fails, check your paths output in the cells above,
# and that you are running the NPL (conda) Kernel
# You can see all the paths being examined by un-commenting the following:
#sys.path


# ### Single CAM vs CAM case
# ---

# In[17]:


# Set path for config YAML file
#config_path = "/path/to/your/yaml/file/"
config_path = "/glade/work/richling/ADF/adf-demo/config_files/"

# Set name of config YAML file:
config_fil_str = "config_model_vs_model.yaml"

# Make full path to config file
config_file=os.path.join(config_path,config_fil_str)


# In[18]:


#Initialize ADF object with config file
adf = AdfDiag(config_file)
adf


# In[19]:


# Grab the case names
case_names = adf.get_cam_info("cam_case_name",required=True)
print(case_names)
case_names = adf.get_baseline_info("cam_case_name",required=True)
print(case_names)


# In[20]:


adf.climo_yrs


# In[21]:


var_list = adf.diag_var_list
list(var_list)


# #### First part of ADF is to create time series files
#     
#     * if they don't already exist or input files are in time series format already
#     
# ##### This is under the hood when the ADF is run via terminal

# In[22]:


get_ipython().run_cell_magic('time', '', '#Create model time series.\nadf.create_time_series()\n')


# In[ ]:


get_ipython().run_cell_magic('time', '', '#Create model baseline time series (if needed):\n\n# Since we are doing model vs model\nif not adf.compare_obs:\n    adf.create_time_series(baseline=True)\n')


# In[ ]:





# In[ ]:





# In[ ]:


get_ipython().run_cell_magic('time', '', '#Create model climatology (climo) files.\nadf.create_climo()\n')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


get_ipython().run_cell_magic('time', '', '#Regrid model climatology files to match either observations or CAM baseline climatologies.\n#This call uses the "regridding_scripts" specified in the config file:\nadf.regrid_climo()\n')


# In[ ]:





# In[ ]:





# In[ ]:


#Perform analyses on the simulation(s).
#This call uses the "analysis_scripts" specified in the
#config file:
adf.perform_analyses()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#Create plots.
#This call uses the "plotting_scripts" specified
#in the config file:
adf.create_plots()


# In[ ]:





# In[ ]:





# In[ ]:


#Create website if requested in the config file
if adf.create_html:
    adf.create_website()


# In[ ]:





# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # Exercise - Run ADF via Jupyter
# 
# In addition to running the ADF in the terminal, it can also be run in Jupyter Notebooks!
# 
# Let's use the same two CAM simulations we used to run the ADF in the terminal, but this time let's run it for climo years 2001-2005
# 

# ```{admonition} Question:
# :class: hint
# What do you need to do to run the ADF with a new set of climo years? 
# 
# ::::{admonition} Help?
# :class: dropdown attention
# GO DO IT!
# ::::
# 
# Yeah?
# ```

# ```{admonition} Question:
# :class: hint
# What do you need to do to run the ADF with a new set of climo years? 
# 
# ::::{admonition} Help?
# :class: dropdown attention
# 
# ::::::{admonition} Yes
# :class: dropdown warning
# That'd be $3.50 please
# ::::::
# 
# :::::::{admonition} No
# :class: dropdown tip
# GO DO IT!
# :::::::
# 
# ::::
# 
# Yeah?
# ```

# For this example we will run the ADF diagnostics for two different CAM simulations for a 5 years, 2001-2005
# 
# Running the ADF in a Jupyter Notebook allows for some really handy access to the output data as well as all the paths
# 
# <p>The test (experiment) case is <code class="docutils literal notranslate"><span class="pre">f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001</span></code></p>
# <p style="margin-top: -15px;">The baseline (control) case is <code class="docutils literal notranslate"><span class="pre">f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001</span></code></p>
# 

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')

import os.path
from pathlib import Path
import sys


# In[ ]:


# Determine ADF directory path
# If it is in your cwd, set adf_path = local_path, 
# otherwise set adf_path appropriately

local_path = os.path.abspath('')


# Set the path for the ADF, ie the root directory of the ADF `/glade/work/{user}/ADF`

# In[ ]:


adf_path = "/glade/work/{user}/ADF"

print(f"current working directory = {local_path}")
print(f"ADF path                  = {adf_path}")


# In[ ]:


#set path to ADF lib
lib_path = os.path.join(adf_path,"lib")
print(f"The lib scripts live here, right? {lib_path}")

#set path to ADF plotting scripts directory
plotting_scripts_path = os.path.join(adf_path,"scripts","plotting")
print(f"The plotting scripts live here, right? {plotting_scripts_path}")

#Add paths to python path:
sys.path.append(lib_path)
sys.path.append(plotting_scripts_path)


# In[ ]:


#import ADF diagnostics object
from adf_diag import AdfDiag

# If this fails, check your paths output in the cells above,
# and that you are running the NPL (conda) Kernel
# You can see all the paths being examined by un-commenting the following:
#sys.path


# In[ ]:





# ### Single CAM vs CAM case
# ---

# ##### Config yaml file location and name

# In[ ]:


# Set path for config YAML file
#config_path = "/path/to/your/yaml/file/"
config_path = "/glade/work/richling/ADF/adf-tutorials/ADF-Tutorial/config_files/"

# Set name of config YAML file:
config_fil_str = "config_model_vs_model_single.yaml"

# Make full path to config file
config_file=os.path.join(config_path,config_fil_str)


# In[ ]:


#Initialize ADF object with config file
adf = AdfDiag(config_file)
adf


# Say you want to grab the case names as a variable for later use, ie plot titles or file name, etc. The ADF object can provide that as well:

# In[14]:


# Grab the case names
case_names = adf.get_cam_info("cam_case_name",required=True)
print(case_names)
case_names = adf.get_baseline_info("cam_case_name",required=True)
print(case_names)


# Grab the climo years for all cases available (observations won't have climo years from the ADF)

# In[16]:


adf.climo_yrs


# Grab a list of all desired variables

# In[15]:


var_list = adf.diag_var_list
list(var_list)


# In[ ]:





# ---

# ## ADF Standard Work Flow

# #### First part of ADF is to create time series files
#     
#     * if they don't already exist or input files are in time series format already
#     
# ##### This is under the hood when the ADF is run via terminal

# In[17]:


get_ipython().run_cell_magic('time', '', '#Create model time series.\nadf.create_time_series()\n')


# In[18]:


get_ipython().run_cell_magic('time', '', '#Create model baseline time series (if needed):\n\n# Since we are doing model vs model\nif not adf.compare_obs:\n    adf.create_time_series(baseline=True)\n')


# #### Next, create climotology files from time series files

# In[20]:


get_ipython().run_cell_magic('time', '', '#Create model climatology (climo) files.\nadf.create_climo()\n')


# #### Finally, regrid climotology files

# In[ ]:


get_ipython().run_cell_magic('time', '', '#Regrid model climatology files to match either observations or CAM baseline climatologies.\n#This call uses the "regridding_scripts" specified in the config file:\nadf.regrid_climo()\n')


# ```
# Regridding CAM climatologies...
#     /glade/work/richling/ADF/adf-tutorials/adf-output/regrid not found, making new directory
# 	 Regridding case 'f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001' :
# 	 - regridding PS (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001'])
# 	    /glade/work/richling/ADF/adf-tutorials/adf-output/diag-plot/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001_1995_2012_vs_f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001_1995_2012 not found, making new directory
# 	 - regridding FLNT (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001'])
# 	 - regridding FSNT (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001'])
# 	 - regridding LHFLX (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001'])
# 	 - regridding LWCF (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001'])
# 	 - regridding OMEGA500 (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001'])
# 	 - regridding PBLH (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001'])
# 	 - regridding PRECL (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001'])
# 	 - regridding PRECT (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001'])
# 	 - regridding PSL (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001'])
# 	 - regridding QFLX (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001'])
# 	 - regridding CLDLIQ (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001'])
# Please ignore the interpolation warnings that follow!
# Interpolation point out of data bounds encountered
# Interpolation point out of data bounds encountered
# Please ignore the interpolation warnings that follow!
# Interpolation point out of data bounds encountered
# Interpolation point out of data bounds encountered
# 	 - regridding Q (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001'])
# Please ignore the interpolation warnings that follow!
# Interpolation point out of data bounds encountered
# Interpolation point out of data bounds encountered
# Please ignore the interpolation warnings that follow!
# Interpolation point out of data bounds encountered
# Interpolation point out of data bounds encountered
# 	 - regridding RELHUM (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001'])
# Please ignore the interpolation warnings that follow!
# Interpolation point out of data bounds encountered
# Interpolation point out of data bounds encountered
# Please ignore the interpolation warnings that follow!
# Interpolation point out of data bounds encountered
# Interpolation point out of data bounds encountered
# 	 - regridding SHFLX (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001'])
# 	 - regridding SST (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001'])
# 	 - regridding SWCF (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001'])
# 	 - regridding T (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001'])
# Please ignore the interpolation warnings that follow!
# Interpolation point out of data bounds encountered
# Interpolation point out of data bounds encountered
# Please ignore the interpolation warnings that follow!
# Interpolation point out of data bounds encountered
# Interpolation point out of data bounds encountered
# 	 - regridding TAUX (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001'])
# 	 - regridding TAUY (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001'])
# 	 - regridding THETA (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001'])
# 	 - regridding THETA failed, no file. Continuing to next variable.
# 	 - regridding TREFHT (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001'])
# 	 - regridding TS (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001'])
# 	 - regridding U (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001'])
# Please ignore the interpolation warnings that follow!
# Interpolation point out of data bounds encountered
# Interpolation point out of data bounds encountered
# Please ignore the interpolation warnings that follow!
# Interpolation point out of data bounds encountered
# Interpolation point out of data bounds encountered
# 	 - regridding U10 (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001'])
# 	 - regridding ICEFRAC (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001'])
# 	 - regridding OCNFRAC (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001'])
# 	 - regridding LANDFRAC (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001'])
#   ...CAM climatologies have been regridded successfully.
# CPU times: user 59.7 s, sys: 17.7 s, total: 1min 17s
# Wall time: 1min 27s
# ```

# ### Start diagnostics calls now

# ##### Run the analysis script to create the AMWG tables

# In[ ]:


#Perform analyses on the simulation(s).
#This call uses the "analysis_scripts" specified in the
#config file:
adf.perform_analyses()


# ##### Run the plotting scripts

# In[ ]:


#Create plots.
#This call uses the "plotting_scripts" specified
#in the config file:
adf.create_plots()


# ### Now we can generate webpage `html` files

# In[ ]:


#Create website if requested in the config file
if adf.create_html:
    adf.create_website()


# ---

# ## End single CAM vs CAM case
# 
# Hope everything went well...
# 

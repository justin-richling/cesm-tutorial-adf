#!/usr/bin/env python
# coding: utf-8

# # Exercise - Run ADF via Jupyter
# 
# In addition to running the ADF in the terminal, it can also be run in Jupyter Notebooks!
# 
# Let's use the same two CAM simulations we used to run the ADF in the terminal, but this time let's run it for climo years 2001-2005
# 

# 

# In[ ]:





# For this example we will run the ADF diagnostics for two different CAM simulations for a 5 years, 2000-2006
# 
# Running the ADF in a Jupyter Notebook allows for some really handy access to the output data as well as all the paths
# 
# The test (experiment) case is `f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001`
# 
# The baseline (control) case is `f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001`
# 

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


import os.path
from pathlib import Path
import sys


# In[ ]:


# Determine ADF directory path
# If it is in your cwd, set adf_path = local_path, 
# otherwise set adf_path appropriately

local_path = os.path.abspath('')


# In[ ]:





# #### It is important to remember the <strong>two</strong> things important in this notebook are the:
#     * ADF branch you want, which will also be dependent on adf_path
#     * Config yaml file you want

# ##### ADF location
# 
# * NOTE: you will have to change the branch via terminal if you want a certain branch in this notebook
# 
# Or you could use a cell to do it:
# 
#     !git checkout <your-branch>

# In[ ]:


# You can change the path to ADF (git branch) so it can be different than the
# current location

#adf_path = "/path/to/your/ADF"
adf_path = "/glade/work/richling/ADF/ADF_dev/Justin_ADF/ADF"

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


# ## Let's look at some basic info from the ADF

# #### Read out some of the declared variables from the config file

# In[ ]:


basic_info_dict = adf.read_config_var("diag_basic_info")
list(basic_info_dict)


# In[ ]:


# Quick check if we are comparing against obs, in case we forgot our ginkaloba pills this morning
obs = adf.get_basic_info('compare_obs')
print("'get basic info' found compare_obs =",obs)


# In[ ]:


# A similar but different way to check directly from the adf object:
adf.compare_obs


# In[ ]:


# Baseline case details
baseline_dict = adf.read_config_var("diag_cam_baseline_climo")
list(baseline_dict)

```python
dir(adf)
```<div class="admonition tip">
<p>Some **content**</p>

````html
```python
dir(adf)
```
````

</div>

```{admonition} &ensp; 
:class: dropdown, hint

::::
['_AdfBase__debug_log',
 '_AdfConfig__config_dict',
 '_AdfConfig__create_search_dict',
 '_AdfConfig__expand_yaml_var_ref',
 '_AdfConfig__kword_pattern',
 '_AdfConfig__search_dict',
 '_AdfDiag__analysis_scripts',
 '_AdfDiag__cvdp_info',
 '_AdfDiag__diag_scripts_caller',
 '_AdfDiag__function_caller',
 '_AdfDiag__plotting_scripts',
 '_AdfDiag__regridding_scripts',
 '_AdfDiag__time_averaging_scripts',
 '_AdfInfo__base_nickname',
 '_AdfInfo__basic_info',
 '_AdfInfo__cam_bl_climo_info',
 '_AdfInfo__cam_climo_info',
 '_AdfInfo__compare_obs',
 '_AdfInfo__derived_var_list',
 '_AdfInfo__diag_var_list',
 '_AdfInfo__eyear_baseline',
 '_AdfInfo__eyears',
 '_AdfInfo__num_cases',
 '_AdfInfo__num_procs',
 '_AdfInfo__plot_location',
 '_AdfInfo__syear_baseline',
 '_AdfInfo__syears',
 '_AdfInfo__test_nicknames',
 '_AdfObs__use_defaults',
 '_AdfObs__var_obs_dict',
 '_AdfObs__variable_defaults',
 '_AdfWeb__case_web_paths',
 '_AdfWeb__plot_type_multi',
 '_AdfWeb__plot_type_order',
 '_AdfWeb__website_data',
 '__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 'add_diag_var',
 'add_website_data',
 'baseline_climo_dict',
 'basic_info_dict',
 'cam_climo_dict',
 'case_nicknames',
 'climo_yrs',
 'compare_obs',
 'create_climo',
 'create_html',
 'create_plots',
 'create_time_series',
 'create_website',
 'debug_log',
 'derived_var_list',
 'diag_var_list',
 'end_diag_fail',
 'expand_references',
 'get_baseline_info',
 'get_basic_info',
 'get_cam_info',
 'get_cvdp_info',
 'log_press',
 'main_site_paths',
 'num_cases',
 'num_procs',
 'perform_analyses',
 'plot_location',
 'read_config_var',
 'regrid_climo',
 'setup_run_cvdp',
 'use_defaults',
 'var_obs_dict',
 'variable_defaults']
::::
```::::{admonition}
:::python
dir(adf)
:::
::::

sdad::::{Warning}
<strong>Please do not modify this file unless you plan to push your changes back to the ADF repo!</strong>
             
If you would like to modify this file for your personal ADF runs then it is recommended to make a copy of this file, make modifications in that copy, and then point the ADF to it using the `defaults_file` config variable in the <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/configs/yaml/runtime.html#defaults-file"><code class="docutils literal notranslate"><span class="pre">config_your_run.yaml</span></code> (copy of config_cam_baseline_example.yaml)</a>.


:::{admonition} Example
:class: seealso
From the ADF root directory

    cp lib/adf_variable_defaults.yaml lib/my_variable_defaults.yaml

In <code class="docutils literal notranslate"><span class="pre">config_your_run.yaml</span></code>:

Under the subset `diag_basic_info`:

<p style="margin-top: -5px;">&ensp; use_defaults: <code class="docutils literal notranslate"><span class="pre">false</span></code></p>

<p style="margin-top: -5px;">&ensp; defaults_file: <code class="docutils literal notranslate"><span class="pre">/path/to/your_variable_defaults.yaml</span></code></p>
:::
::::```{admonition} `{python} dir(adf)`
:class: dropdown, hint

::::
['_AdfBase__debug_log',
 '_AdfConfig__config_dict',
 '_AdfConfig__create_search_dict',
 '_AdfConfig__expand_yaml_var_ref',
 '_AdfConfig__kword_pattern',
 '_AdfConfig__search_dict',
 '_AdfDiag__analysis_scripts',
 '_AdfDiag__cvdp_info',
 '_AdfDiag__diag_scripts_caller',
 '_AdfDiag__function_caller',
 '_AdfDiag__plotting_scripts',
 '_AdfDiag__regridding_scripts',
 '_AdfDiag__time_averaging_scripts',
 '_AdfInfo__base_nickname',
 '_AdfInfo__basic_info',
 '_AdfInfo__cam_bl_climo_info',
 '_AdfInfo__cam_climo_info',
 '_AdfInfo__compare_obs',
 '_AdfInfo__derived_var_list',
 '_AdfInfo__diag_var_list',
 '_AdfInfo__eyear_baseline',
 '_AdfInfo__eyears',
 '_AdfInfo__num_cases',
 '_AdfInfo__num_procs',
 '_AdfInfo__plot_location',
 '_AdfInfo__syear_baseline',
 '_AdfInfo__syears',
 '_AdfInfo__test_nicknames',
 '_AdfObs__use_defaults',
 '_AdfObs__var_obs_dict',
 '_AdfObs__variable_defaults',
 '_AdfWeb__case_web_paths',
 '_AdfWeb__plot_type_multi',
 '_AdfWeb__plot_type_order',
 '_AdfWeb__website_data',
 '__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 'add_diag_var',
 'add_website_data',
 'baseline_climo_dict',
 'basic_info_dict',
 'cam_climo_dict',
 'case_nicknames',
 'climo_yrs',
 'compare_obs',
 'create_climo',
 'create_html',
 'create_plots',
 'create_time_series',
 'create_website',
 'debug_log',
 'derived_var_list',
 'diag_var_list',
 'end_diag_fail',
 'expand_references',
 'get_baseline_info',
 'get_basic_info',
 'get_cam_info',
 'get_cvdp_info',
 'log_press',
 'main_site_paths',
 'num_cases',
 'num_procs',
 'perform_analyses',
 'plot_location',
 'read_config_var',
 'regrid_climo',
 'setup_run_cvdp',
 'use_defaults',
 'var_obs_dict',
 'variable_defaults']
::::
```
# For an in-depth break down of all the possible properties and methods, without values, from the `adf` object

# In[ ]:


dir(adf)


# Say you want to grab the case names as a variable for later use, ie plot titles or file name, etc. The ADF object can provide that as well:

# In[14]:


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

# In[ ]:





# ###
# 
# Let's use the same two CAM simulations we used to run the ADF in the terminal, but this time let's run it for climo years 2001-2005

#  

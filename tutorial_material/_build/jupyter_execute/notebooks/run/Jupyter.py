#!/usr/bin/env python
# coding: utf-8

# # ADF in Jupyter
# 
# In addition to running the ADF in the terminal, it can also be run in Jupyter Notebooks!
# 
# Since NCAR has a JupyterHub account, we can either <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/run/Jupyter/jupyter_adf_run.html">run the ADF via Jupyter</a> or <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/run/Jupyter/jupyter_adf_analysis.html">analyze already run ADF diagnostics</a> in Jupyter too! Holy Cow.
# 
# 
# 

# 

# 

# #### Tips for ADF in Jupyter

# In[ ]:


#Initialize ADF object with config file
adf = AdfDiag(config_file)
adf


# <adf_diag.AdfDiag at 0x2b4984b32b80>

# ###### Basic Info from Run-time Yaml File

# In[ ]:


basic_info_dict = adf.read_config_var("diag_basic_info")
list(basic_info_dict)


# ```
# ['compare_obs',
#  'create_html',
#  'obs_data_loc',
#  'cam_regrid_loc',
#  'cam_overwrite_regrid',
#  'cam_diag_plot_loc',
#  'use_defaults',
#  'plot_press_levels',
#  'weight_season',
#  'num_procs',
#  'redo_plot']
# ```

# ###### Boolean for Observations in Basic Info from Run-time Yaml File

# In[ ]:


# Quick check if we are comparing against obs, in case we forgot our ginkaloba pills this morning
obs = adf.get_basic_info('compare_obs')
print("'get basic info' found compare_obs =",obs)


# 'get basic info' found compare_obs = False

# In[ ]:


# A similar but different way to check directly from the adf object:
adf.compare_obs


# ###### 

# In[ ]:


# Baseline case details
baseline_dict = adf.read_config_var("diag_cam_baseline_climo")
list(baseline_dict)


# False

# In[ ]:


# Grab the case names
case_names = adf.get_cam_info("cam_case_name",required=True)
print(case_names)
case_names = adf.get_baseline_info("cam_case_name",required=True)
print(case_names)


# ```
# ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001']
# f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001
# ```

# In[ ]:


adf.climo_yrs


# ```
# {'syears': [1995],
#  'eyears': [2012],
#  'syear_baseline': 1995,
#  'eyear_baseline': 2012}
# ```

# In[ ]:


var_list = adf.diag_var_list
list(var_list)


# ```
# ['FLNT',
#  'FSNT',
#  'LHFLX',
#  'LWCF',
#  'OMEGA500',
#  'PBLH',
#  'PRECL',
#  'PRECT',
#  'PS',
#  'PSL',
#  'QFLX',
#  'CLDLIQ',
#  'Q',
#  'RELHUM',
#  'SHFLX',
#  'SST',
#  'SWCF',
#  'T',
#  'TAUX',
#  'TAUY',
#  'THETA',
#  'TREFHT',
#  'TS',
#  'U',
#  'U10',
#  'ICEFRAC',
#  'OCNFRAC',
#  'LANDFRAC']
# ```

# In[ ]:


dir(adf)


# ```
# ['_AdfBase__debug_log',
#  '_AdfConfig__config_dict',
#  '_AdfConfig__create_search_dict',
#  '_AdfConfig__expand_yaml_var_ref',
#  '_AdfConfig__kword_pattern',
#  '_AdfConfig__search_dict',
#  '_AdfDiag__analysis_scripts',
#  '_AdfDiag__cvdp_info',
#  '_AdfDiag__diag_scripts_caller',
#  '_AdfDiag__function_caller',
#  '_AdfDiag__plotting_scripts',
#  '_AdfDiag__regridding_scripts',
#  '_AdfDiag__time_averaging_scripts',
#  '_AdfInfo__base_nickname',
#  '_AdfInfo__basic_info',
#  '_AdfInfo__cam_bl_climo_info',
#  '_AdfInfo__cam_climo_info',
#  '_AdfInfo__compare_obs',
#  '_AdfInfo__derived_var_list',
#  '_AdfInfo__diag_var_list',
#  '_AdfInfo__eyear_baseline',
#  '_AdfInfo__eyears',
#  '_AdfInfo__num_cases',
#  '_AdfInfo__num_procs',
#  '_AdfInfo__plot_location',
#  '_AdfInfo__syear_baseline',
#  '_AdfInfo__syears',
#  '_AdfInfo__test_nicknames',
#  '_AdfObs__use_defaults',
#  '_AdfObs__var_obs_dict',
#  '_AdfObs__variable_defaults',
#  '_AdfWeb__case_web_paths',
#  '_AdfWeb__plot_type_multi',
#  '_AdfWeb__plot_type_order',
#  '_AdfWeb__website_data',
#  '__class__',
#  '__delattr__',
#  '__dict__',
#  '__dir__',
#  '__doc__',
#  '__eq__',
#  '__format__',
#  '__ge__',
#  '__getattribute__',
#  '__gt__',
#  '__hash__',
#  '__init__',
#  '__init_subclass__',
#  '__le__',
#  '__lt__',
#  '__module__',
#  '__ne__',
#  '__new__',
#  '__reduce__',
#  '__reduce_ex__',
#  '__repr__',
#  '__setattr__',
#  '__sizeof__',
#  '__str__',
#  '__subclasshook__',
#  '__weakref__',
#  'add_diag_var',
#  'add_website_data',
#  'baseline_climo_dict',
#  'basic_info_dict',
#  'cam_climo_dict',
#  'case_nicknames',
#  'climo_yrs',
#  'compare_obs',
#  'create_climo',
#  'create_html',
#  'create_plots',
#  'create_time_series',
#  'create_website',
#  'debug_log',
#  'derived_var_list',
#  'diag_var_list',
#  'end_diag_fail',
#  'expand_references',
#  'get_baseline_info',
#  'get_basic_info',
#  'get_cam_info',
#  'get_cvdp_info',
#  'log_press',
#  'main_site_paths',
#  'num_cases',
#  'num_procs',
#  'perform_analyses',
#  'plot_location',
#  'read_config_var',
#  'regrid_climo',
#  'setup_run_cvdp',
#  'use_defaults',
#  'var_obs_dict',
#  'variable_defaults']
# ```

# In[ ]:





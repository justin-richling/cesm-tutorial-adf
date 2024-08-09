#!/usr/bin/env python
# coding: utf-8

# ## ADF Basics
# 
# Now that the ADF and environment have been set up, let's take just a quick look at what the ADF actually does and the flow of it. To run the ADF, there are just a couple of steps and then <abbr title="Famous last words"><strong>it's good to go!</strong></abbr>
# 

# ---

# ### ADF Setup
# 
# A simple look at the steps for using the ADF
# 
# <a>0.</a> Run CAM/other simulation to get ADF input files <br>
# &ensp;&ensp;&ensp;history files (ie: h0, h1, etc.)<br>
# &ensp;&ensp;&ensp;time series files (ie: C/AMIP)
# 
# <a>1.</a> Configure copies of yaml file(s) for the input files<br>
# &ensp;&ensp;&ensp;config_cam_baseline_example.yaml - <strong>required</strong><br>
# &ensp;&ensp;&ensp;lib/adf_variable_defaults.yaml - optional
# 
# <a>2.</a> Run the ADF<br>
# &ensp;&ensp;&ensp;simple command line call: `./run_adf_diag <your config file>.yaml`
# 
# <a>3.</a> View Diagnostics<br>
# &ensp;&ensp;&ensp;Locally<br>
# &ensp;&ensp;&ensp;Jupyter/JupyterHub<br>
# &ensp;&ensp;&ensp;Publish to website

# ### ADF Flow
# 
# A simple look at the flow of the ADF<br>
# &ensp;&#x21B3; Create time series files from monthly history files (if they don’t exist or are being overwritten)<br>
# &ensp;&ensp;&#x21B3; Create climatology files from either ADF generated or pre-existing time series files (ie CMIP)<br>
# &ensp;&ensp;&ensp;&#x21B3; Regrid Test case from Baseline case and vice-versa from climatology files<br>
# &ensp;&ensp;&ensp;&ensp;&#x21B3; Run Analysis scripts<br>
# &ensp;&ensp;&ensp;&ensp;&ensp;&#x21B3; Run Plotting scripts<br>
# &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&#x21B3; Generate Website pages
# 
# 
# ** Most parts of the ADF are optional and can be turned off for your desired need:
# 
# Potential Examples:
#            
# - If you only want regridded data, turn off plotting, analysis, website parts
#     
# - If you want plotting and only need a few plot images, you can turn off the website part
#     
# - If you only want time series files, you can turn off all other parts
#     
# - If you don’t care about the statistics (AMWG) tables, turn off analysis part
#     
# - etc.
# 
# ---
```
<a>0.</a> Run CAM simulation to get history (ie: h0, h1, etc.) files
                                   
<a>1.</a> Configure yaml file(s) for the history files

	NOTE:  Make copies of these files and modify/customize the copies!

    config_cam_baseline_example.yaml  (necessary, must copy and change!)

    lib/adf_variable_defaults.yaml   (necessary, but optional to copy and change)


<a>2.</a> Run the ADF
&#x26A0; Errors?  Check config files   Check error/logs   Check data/paths</p>
&#x2705; Success: Check output data/images</p>
<p>Locally</p>
<p>Via HTML files  (optional)</p>
```0. Run CAM simulation to get history ( h0* ) file(s) 
           *or other history files
                                   
1. Configure yaml file(s) for the history files

	NOTE:  Make copies of these files and modify/customize the copies!

    config_cam_baseline_example.yaml  (necessary, must copy and change!)

    lib/adf_variable_defaults.yaml   (necessary, but optional to copy and change)


2. Run the ADF
&#x26A0; Errors?  Check config files   Check error/logs   Check data/paths</p>
&#x2705; Success: Check output data/images</p>
<p>Locally</p>
<p>Via HTML files  (optional)</p>

# In[ ]:




<p>&#x26A0; Errors?  Check config files   Check error/logs   Check data/paths</p>```{added}
OMG!
``````{success}
OMG!
``````html
<div class="admonition note" name="html-admonition" style="background: red; padding: 10px">
<p class="title">Error</p>
Check config files
Check error/logs
Check data/paths
</div>
```
<div class="admonition note" name="html-admonition" style="background: lightgreen; padding: 10px">
<p class="title">Success</p>
Check output data/images
</div>
# In[ ]:





# ### ADF Layout
# 
# A simple look at the structure of the ADF directories

# ```
# .
# |-- config_amwg_default_plots.yaml
# |-- config_cam_baseline_example.yaml
# |-- env
# |   `-- conda_environment.yaml
# |-- jupyter_sample.ipynb
# |-- lib
# |   |-- adf_base.py
# |   |-- adf_config.py
# |   |-- adf_diag.py
# |   |-- adf_info.py
# |   |-- adf_obs.py
# |   |-- adf_variable_defaults.yaml
# |   |-- adf_web.py
# |   |-- plotting_functions.py
# |   |-- test
# |   |   |-- pylintrc
# |   |   `-- unit_tests
# |   |       |-- pytest.ini
# |   |       |-- test_adf_base.py
# |   |       |-- test_adf_config.py
# |   |       `-- test_files
# |   |           |-- config_cam_double_nested.yaml
# |   |           |-- config_cam_keywords.yaml
# |   |           `-- config_cam_unset_var.yaml
# |   `-- website_templates
# |       |-- adf_diag.css
# |       |-- NCAR.gif
# |       |-- template.html
# |       |-- template_index.html
# |       |-- template_mean_diag.html
# |       |-- template_mean_tables.html
# |       |-- template_multi_case_index.html
# |       |-- template_table.html
# |       `-- template_var.html
# |-- LICENSE
# |-- README.md
# |-- run_adf_diag
# `-- scripts
#     |-- analysis
#     |   `-- amwg_table.py
#     |-- averaging
#     |   `-- create_climo_files.py
#     |-- plotting
#     |   |-- cam_taylor_diagram.py
#     |   |-- global_latlon_map.py
#     |   |-- global_latlon_vect_map.py
#     |   |-- meridional_mean.py
#     |   |-- polar_map.py
#     |   |-- qbo.py
#     |   |-- regional_map_multicase.py
#     |   `-- zonal_mean.py
#     `-- regridding
#         `-- regrid_and_vert_interp.py
# ```

# In[ ]:





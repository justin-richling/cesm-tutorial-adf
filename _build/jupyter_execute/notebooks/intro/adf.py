#!/usr/bin/env python
# coding: utf-8
```{figure} ./amwg_table_subset.png
---
width: 850px
name: directive-fig
---
Here is my figure caption!
```
<a href="./amwg_table_subset.png" ><img src="amwg_table_subset.png"/></a>**<u>AMWG</u>** (Atmospheric Model Working Group) <u>**D**</u>iagnostics <u>**F**</u>ramework

# # Intro to the ADF
# 
# This package is meant to be an update/upgrade to the much used and beloved AMWG diagnostics package used by the atmospheric/chemistry CESM community. It is still under active development and is near it's first major version.
# 
# 
# ### What is it?
# 
# The ADF is an open source, community developed Python-based set of collection of analysis (averaging), re-gridding, and plotting scripts aimed at replacing the old AMWG Diagnostics package (NCL-based). It is designed to be a multipurpose tool and has been built to be somewhat flexible for customization.
# 
# 
# 
# ### Who is it for?
# 
# The ADF is geared towards users who are running CAM or CAM-like (MPAS) simulations that are looking to compare their runs agains other CAM simulations, observations/reanalysis or model comparison sets (like CMIP/AMIP).
# 
# ### Key Features
# 
# &ensp;<strong>Flexible and Open Source</strong>
# 
# &ensp;&emsp; - ADF code is completely open to the public<br>
# &ensp;&emsp;&emsp; - Users can modify their clone of the ADF to fit their needs if desired
# 
# &ensp;<strong>Use of <a href="https://geocat-comp.readthedocs.io/en/v2023.10.1/index.html" target="_blank"><u>GeoCAT</u></a> functions (currently limited use)</strong>
# 
# &ensp;<strong>Use of <a href="https://www.redhat.com/en/topics/automation/what-is-yaml" target="_blank"><u>YAML configuration files</u></a></strong>
# 
# &ensp;&emsp; - helps to avoid changing source code
# 
# &ensp;<strong>Option for use of multiple processors</strong>
# 
# &ensp;<strong>Installation via Git and Conda package manager</strong>
# 
# &ensp;&emsp; - CISL machines are set to run out of the box with required dependencies
# 
# &ensp;<strong>Centralize vertical interpolation</strong>
# 
# &ensp;-> Regridding and vertical interpolation script which interpolates all model variables with a vertical component onto a standard set of pressure levels
# 
# &ensp;-> Allows 3D model variable comparison against 3D observations
# 
# &ensp;&emsp; - Assuming the observations are also on the same set of pressure levels
#     
# &ensp;<strong>Enable interpolation on <a href="https://www.mmm.ucar.edu/models/mpas/" target="_blank"><u>MPAS</u></a> vertical coordinate</strong>
# 
# &ensp;-> Checks for the MPAS height-based vertical coordinate, and if present it will enable pressure-to-pressure vertical interpolation required to get MPAS data onto the standard pressure levels used by the ADF
# 
# 
# 
# 
# ### Types of ADF Comparisons
# 
# There are essentially 3 types of comparisons:
# 
# * CAM vs CAM
# * CAM vs Observations/Reanalysis
# * CAM vs CMIP
# 
# &ensp;Each of which can be run as:
# 
# <ul>
# <li><p>Single Case Comparison - One test (experiment) case vs one baseline (control/target) case</p></li>
#     <li><p>Multiple Case Comparison<a style="color:red;">**</a> - Multiple test cases vs one baseline case</p></li>
#     <p style="margin-top: -5px;">&emsp;&emsp; <a style="color:red;">**</a> In progress, will not be part of this tutorial at the moment :(</p>
# </ul>
# 
# 
# Each have their own requirements for the run-time config file. The requirements for each type of comparison will be addressed in their respective sections of this tutorial under the <strong>GUIDED EXAMPLES</strong> section.
# 
# ````{attention}
# Depending on how many years, plot types and variables you configure, the more time it takes
# 
# * Rough average for all default plots, 10-20 years for 30 variables is ~45 minutes
# 
# ```{note}
# This is an active area of development; there are potential ways of cutting time/processes
# ```
# 
# ````
# 
# ---

# ## ADF Basics
# 
# Now let's take a quick look at what the ADF actually does and the flow of it.
# 
# 
# ### ADF Flow
# 
# A simple look at the flow of the ADF<br>
# &ensp;&#x21B3; Create time series files from monthly history files<br>
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
# 
# 
# 
# ### ADF Layout
# 
# A simple look at the structure of the ADF directories
# 
# 
# 
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
# 
# 
# 
# 
# 
# ### ADF Setup
# 
# A simple look at the steps for using the ADF
# 
# <a>0.</a> Run CAM/other simulation to get ADF input files <br>
# &ensp;&ensp;&ensp;history files (ie: h0, h1, etc.)<br>
# &ensp;&ensp;&ensp;time series files (ie: C/AMIP)
# 
# <a>1.</a> Configure copies of yaml file(s) for the input files<br>
# &ensp;&ensp;&ensp;config_cam_baseline_example.yaml<br>
# &ensp;&ensp;&ensp;lib/adf_variable_defaults.yaml 
# 
# <a>2.</a> Run the ADF<br>
# &ensp;&ensp;&ensp;simple command line call: `./run_adf_diag config_myadf.yaml`
# &ensp;&ensp;&ensp;run ADF in Jupyter notebook
# 
# <a>3.</a> View Diagnostics<br>
# &ensp;&ensp;&ensp;Locally<br>
# &ensp;&ensp;&ensp;Jupyter/JupyterHub<br>
# &ensp;&ensp;&ensp;Publish to website
# 

# In[ ]:





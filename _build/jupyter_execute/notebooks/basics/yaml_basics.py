#!/usr/bin/env python
# coding: utf-8

# # YAML files
# 
# 
## How to run the ADF

There are two ways to run the ADF, the first and most stright forward is runnning the ADF in the terminal and the second is via Jupyter.

The first steps are to set the desired (and required) variables in the config yaml file(s). In this demo, we will run the ADF standard variable defaults file (`adf_variable_defaults.yaml`), but feel free to explore making your own, please refer back to the <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/intro/yaml/adf_variable_defaults.html" target="_blank">Variable Defaults</a> yaml section.




## Types of ADF Comparisons

There are a couple different ADF runs one can do:

<p>Single Case Comparison</p>
<p>Multiple Case Comparison**</p>
<p style="margin-top: -15px;">&ensp; ** In progress, will not be part of this tutorial currently :(</p>

## Available Comparison Cases

There are essentially 3 types of comparisons:

* CAM vs CAM
* CAM vs Observations/Reanalysis
* CAM vs CMIP

Each have their own requirements for the run-time config file (eg `config_cam_baseline_example`). The requirements for each type of comparison will be addressed in their respective sections of this tutorial.

# 
# 
# The ADF requires 2 different yaml configuration files: 
# 
# `config_cam_baseline_example.yaml` and `adf_variable_defaults.yaml`
# 
# NOTE: Throughout this tutorial we will reference these as the <strong>run-time</strong> and <strong>variable default</strong> yaml files respectively.
# 
# 
# If yaml files are new to you, they are just specialized text files that python (and other languages) can read in and use as configuration files. In the case of the ADF, the variables set in the yaml files will be parsed into Python dictionaries and will accessable throughout the ADF workflow.
# 
# A couple of notes about using the ADF yaml files:<br>
# &ensp;&ensp;Variables can be referenced within the yaml file called with the `${}` syntax.<br>
# IE if we set a `user` variable `user: richling` we can call this by `${user}` and `richling` wil be used where ever it is referenced.<br>
# 
# <style>
# .tooltip {
#   position: relative;
#   display: inline-block;
#   border-bottom: 1px dotted black;
# }
# 
# .tooltip .tooltiptext {
#   visibility: hidden;
#   width: 120px;
#   background-color: black;
#   color: #fff;
#   text-align: center;
#   border-radius: 6px;
#   padding: 5px 0;
#   position: absolute;
#   z-index: 1;
#   bottom: 150%;
#   left: 50%;
#   margin-left: -60px;
# }
# 
# .tooltip .tooltiptext::after {
#   content: "";
#   position: absolute;
#   top: 100%;
#   left: 50%;
#   margin-left: -5px;
#   border-width: 5px;
#   border-style: solid;
#   border-color: black transparent transparent transparent;
# }
# 
# .tooltip:hover .tooltiptext {
#   visibility: visible;
# }
# </style>
# 
# 
# 
# 
# ::::{Warning}
# <strong>Please do not modify either of these files!</strong>
#              
# It is recommended to make a copy of each file, make modifications in those copies, and then run them with the ADF.
# 
# Modifying the originals should only be done if you plan to push changes back to the main ADF repo.
# ::::
# 
# 
# ##### Run-time yaml
# 
# <h5><code class="docutils literal notranslate"><span class="pre" style="color: #076E85;">&emsp;config_cam_baseline_example.yaml</span></code></h5>
# 
# 
# <p>This is the most important file for the ADF, it stores all the necessary information that the ADF needs to run including all the relevant information about the case and baseline/observation/cmip runs.</p>
# 
# <p>It is also broken up into <strong>subsections</strong> with each subsection of the yaml file representing grouped sets of information sent to the ADF each having their own variable names.</p>
# 
# ###### <u>Subsections</u>
# 
# * diag_basic_info
#     - Basic overall run variables
#     
# * diag_cam_climo
#     - Test (experiment) case variables
#     
# * diag_cam_baseline_climo
#     - Baseline (control) case variables
#     - Note: these are the same variables as `diag_cam_climo` just for the baseline case
#     
# * diag_cvdp_info
#     - For running the Climate Variability Diagnostics Package https://www.cesm.ucar.edu/projects/cvdp
#     - This will run in the background of the ADF
#     
# * time_averaging_scripts
#     - Climotology file creation
#     
# * regridding_scripts
#     - Regridding of climo files
#     
# * analysis_scripts
#     - AMWG statisics tables
#     
# * plotting_scripts
#     - Various plotting scripts
#     
# * diag_var_list
#     - List of CAM variables for ADF to run
# 
# 
# CAVEAT: using variables in this yaml file<br>
# In this file, we have built subsections in which variables set in a subsection are only callable by referencing the subsection first with a "`.`" then variable name.
# 
# IE: Say we want to set the climo years in the <strong>test case</strong> subsection `diag_cam_climo` and call them in the <strong>baseline case</strong> subsection `diag_cam_baseline_climo`
# 
# <strong>diag_cam_climo:</strong><br>
# 
# &emsp;&ensp; start_year: 1995  -> we would reference this with `diag_cam_climo.start_year`<br>
# &emsp;&ensp; end_year: 2000  -> we would reference this with `diag_cam_climo.end_year`<br>
# 
# Now if we wanted to reference these climo years in the <strong>baseline</strong> subsection:<br>
# 
# <strong>diag_cam_baseline_climo:</strong><br>
# 
# &emsp;&ensp; start_year:  &dollar;{`diag_cam_climo.start_year`}<br>
# &emsp;&ensp; end_year:  &dollar;{`diag_cam_climo.end_year`}
# </p>
# 
# 
# We can also set global variables (like the `user` example) that can be called in any subsections without the '.' notation. 
# 
# IE: Say we want to reference the user variable in the <strong>test case</strong> subsection `diag_cam_climo`
#     
# <strong>diag_cam_climo:</strong><br>
# 
# &emsp;&ensp; cam_climo_loc: <code class="docutils literal notranslate"><span class="pre" style="color: black;">/glade/work/${user}/ADF/data/climos/</span></code>  -> <code class="docutils literal notranslate"><span class="pre" style="color: black;">/glade/work/richling/ADF/data/climos/</span></code>
# 
# ```{tip}
# <p>Please see the <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/reference/yaml/config_cam_baseline_example.html" target="_blank">config yaml file reference section</a> for more details about this config file including how to use defined variables and more information about the config variables.</p>
# ```
# 
# 

# ---

# ##### Variable Default yaml
# 
# <h5><code class="docutils literal notranslate"><span class="pre" style="color: #076E85;">&emsp;lib/adf_variable_defaults.yaml</span></code></h5>
# 
# 
# This yaml file is designed to host a myriad of information related to each of the variables that are being analyzed in the ADF. Some main points to using this file is to customize plotting options or calcuations/analysis on a variable by variable basis.
# 
# Example of options for zonal wind `U` 
# ```
# U:
#   colormap: "Blues"
#   contour_levels_range: [-10, 90, 5]
#   diff_colormap: "BrBG"
#   diff_contour_range: [-15, 15, 2]
#   scale_factor: 1
#   add_offset: 0
#   new_unit: "ms$^{-1}$"
#   mpl:
#     colorbar:
#       label : "ms$^{-1}$"
#   obs_file: "U_ERA5_monthly_climo_197901-202112.nc"
#   obs_name: "ERA5"
#   obs_var_name: "U"
#   vector_pair: "V"
#   vector_name: "Wind"
#   category: "State"
# ```
# 
# 
```{tip}
<p>Please see the <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/reference/yaml/adf_variable_defaults.html" target="_blank">variable defaults yaml file reference section</a> for more details of the contents.</p>

<p>Also visit the <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/exercises/custom_defaults.html" target="_blank">exercise example</a> for using a custom variable defaults file.</p>
```
---Please see the <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/reference/yaml/adf_variable_defaults.html" target="_blank">reference section</a> for the variable defaults file for more details of the contents. 

Also see the <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/exercises/custom_defaults.html" target="_blank">exercise example</a> for using a custom variable defaults file.###### Custom Set

::::{Warning}
<strong>Please do not modify this file unless you plan to push your changes back to the ADF repo!</strong>
             
If you would like to modify this file for your personal ADF runs then it is recommended to make a copy of this file, make modifications in that copy, and then point the ADF.<br>

Please see the <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/reference/yaml/adf_variable_defaults.html" target="_blank">reference section</a> for the variable defaults file for further assistance. Also see the <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/exercises/custom_defaults.html" target="_blank">exercise example</a> for customization
::::
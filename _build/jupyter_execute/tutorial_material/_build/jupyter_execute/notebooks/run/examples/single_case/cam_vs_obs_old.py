#!/usr/bin/env python
# coding: utf-8

# ## CAM vs Obs/Reanalysis

# For this example we will run the ADF diagnostics for two different CAM simulations for a 5 years, 1995-2000
# 
# <p>The test (experiment) case is <code class="docutils literal notranslate"><span class="pre">f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001</span></code></p>
# <p style="margin-top: -15px;">The baseline (control) case will be a designated set of observations/reanalysis</p>
# 
<div class="admonition warning">
<p>Some **content**</p>
  <div class="admonition seealso">
  <div class="title">Example</div>
  <p>From the ADF root directory</p>
      <p>    `cp config_cam_example.yaml config_adf_tutorial.yaml`</p>

  </div>
</div>
# #### config_cam_baseline_example.yaml
# 
# ::::{Warning}
# <strong>Please do not modify this file!</strong>
#              
# It is recommended to make a copy of this file, make modifications in that copy, and then run that with the ADF.
# 
# ::::

# From the ADF root directory
# 
#     cp config_cam_baseline_example.yaml config_cam_vs_obs.yaml
# 
#### config_cam_example.yaml

Please refer back to the ADF Reference page for more info on these variables and for other optional variables

```{Warning}
Note:  Please do not modify this file.
             
It is recommended to make a copy of this file, make modifications in that copy, and then run that in the ADF.

`````{admonition} Example
:class: seealso
From the ADF root directory

    cp config_cam_example.yaml config_adf_tutorial.yaml
`````
```

<div class="admonition warning">
<p>Some **content**</p>
  <div class="admonition seealso">
  <div class="title">Example</div>
  <p>From the ADF root directory</p>
      `cp config_cam_example.yaml config_adf_tutorial.yaml`

  </div>
</div>
# Open the new `config_cam_vs_obs.yaml` file with your favorite editor again
# 
# The following subsections have variables that will be changed:
# 
# * <p style="margin-top: -5px;"><a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/run/model_vs_model.html#diag-basic-info">diag_basic_info</a></p>
# * <p style="margin-top: -5px;"><p style="margin-top: -5px;"><a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/run/model_vs_model.html#diag-cam-climo">diag_cam_climo</a></p>
# 

# ---

# ###### diag_basic_info
# 
# Create a new variable for the root ADF path `adf_path`. This will be used to house the different directories for the time series, climo, and regridded files as well as where the plots and websites will go
# 
# <p style="margin-top: -5px;">&ensp; adf_path: <code class="docutils literal notranslate"><span class="pre">/glade/scratch/${user}/ADF</span></code></p>
# 
# Also create a variable `hist_path` for the path to the history files
# 
# <p style="margin-top: -5px;">&ensp; hist_path: <code class="docutils literal notranslate"><span class="pre">/glade/scratch/richling/ADF/tutorials/data</span></code></p>
# 
# Now we can change the paths for the regridded data and plot locations
# 
# <p style="margin-top: -5px;">&ensp; cam_regrid_loc: <code class="docutils literal notranslate"><span class="pre">${adf_path}/regrid</span></code></p>
# 
# <p style="margin-top: -5px;">&ensp; cam_diag_plot_loc: <code class="docutils literal notranslate"><span class="pre">${adf_path}/plots</span></code></p>
# 
# 
# 
# <p style="margin-top: -5px;">&ensp; compare_obs: <code class="docutils literal notranslate"><span class="pre">true</span></code></p>
# 
# `/glade/work/nusbaume/SE_projects/model_diagnostics/ADF_obs`
# 
# If you want to provide a location for a different set of observations than the ADF default ones, one further step is required:
# 
# Change the location of obs files
# 
# <p style="margin-top: -5px;">&ensp; obs_data_loc: <code class="docutils literal notranslate"><span class="pre">/path/to/your/obs/</span></code></p>
# 
# ```{Note}
# This only matters if the path isn't specified in the variable defaults file.
# 
# In the <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/intro/yaml/adf_variable_defaults.html">variable defaults file</a> each variable can be assigned a specific obs file from any given path different from what is being set here.
# 
# Example of custom location for Boundary Layer obs file
# 
# <div>
# <p>PBLH:
# <p style="margin-top: -20px; font-family:georgia,garamond,serif;">&ensp;   category:  "Surface variables"
# <p style="margin-top: -20px; font-family:georgia,garamond,serif;">&ensp;   <span style="background-color: #FFFF00">obs_file: "/path/to/my/ADF_obs/Some_PBLH_climo.nc"</span>
# <p style="margin-top: -20px; font-family:georgia,garamond,serif;">&ensp;   obs_name: "SOME_OBS"
# <p style="margin-top: -20px; font-family:georgia,garamond,serif;">&ensp;   obs_var_name: "PBLH"
# </div>
# <br>
# 
# For PBLH, the ADF will use <code class="docutils literal notranslate"><span class="pre">/path/to/my/ADF_obs/Some_PBLH_climo.nc</span></code> instead of default
# 
# <p>It will override the location given by <code class="docutils literal notranslate"><span class="pre">obs_data_loc</span></code></p>
# 
# ```
# 
# ###### diag_cam_climo
# 
# <p style="margin-top: -5px;">&ensp; cam_case_name: <code class="docutils literal notranslate"><span class="pre">f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001</span></code></p>
# 
# <p style="margin-top: -5px;">&ensp; cam_hist_loc: <code class="docutils literal notranslate"><span class="pre">${hist_path}/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001</span></code></p>
# <p style="margin-top: -5px;">&ensp; cam_climo_loc: <code class="docutils literal notranslate"><span class="pre">${adf_path}/climo/{diag_cam_climo.cam_case_name}</span></code></p>
# <p style="margin-top: -5px;">&ensp; start_year: <code class="docutils literal notranslate"><span class="pre">1995</span></code></p>
# <p style="margin-top: -5px;">&ensp; end_year: <code class="docutils literal notranslate"><span class="pre">2000</span></code></p>
# <p style="margin-top: -5px;">&ensp; cam_ts_loc: <code class="docutils literal notranslate"><span class="pre">${adf_path}/ts/{diag_cam_climo.cam_case_name}</span></code></p>
# 

# ---

# <style>
#     #box {
#     word-wrap:normal;
#     overflow:scroll;
# }
# </style>
# 
# <h5>With all these variables now set, let's take a quick catalogue of the different paths we just set:</h5>
# 
# Regridded file location:
# <div id="box" >
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">/glade/scratch/{user}/ADF/regrid</span></code></p>
# 
# Diagnostic plot location:
# 
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">/glade/scratch/{user}/ADF/plots</span></code></p>
# 
# This will output a new directory in this location:
# 
# <p style="margin-top: -25px;"><code class="docutils literal notranslate"><span class="pre">&ensp; f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001_1995_2000_vs_f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001_1995_2000/</span></code></p>
# 
# Climatology file locations:
# 
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">/glade/scratch/{user}/ADF/climo/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001</span></code></p>
# 
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">/glade/scratch/{user}/ADF/climo/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001</span></code></p>
# 
# Timeseries locations:
#     
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">/glade/scratch/{user}/ADF/ts/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001</span></code></p>
# 
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">/glade/scratch/{user}/ADF/ts/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001</span></code></p>
#     
# </div>

# In[ ]:





# ---

# #### adf_variable_defaults.yaml
# 
# Location for many plotting, unit, etc defualts for any/all CAM output variables
# 
# 
#### ADF Default Set

<p>If you want to use the ADF default values you need to set <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/configs/yaml/runtime.html#use-defaults"><code class="docutils literal notranslate"><span class="pre">use_defaults</span></code></a> in your copy of the config_yaml to true
</p>
# ###### Custom Set
# 
# <p>If you plan on using a modified file for your custom values you need to set <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/configs/yaml/runtime.html#use-defaults"><code class="docutils literal notranslate"><span class="pre">use_defaults</span></code></a> in your copy of the config_yaml to false and set the path to the custom variable default file with <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/configs/yaml/runtime.html#defaults-file"><code class="docutils literal notranslate"><span class="pre">defaults_file</span></code></a>
# </p>
# 
# For running the ADF against obs, you can customize the obs file for each specific variable!
# 
# ::::{Warning}
# <strong>Please do not modify this file unless you plan to push your changes back to the ADF repo!</strong>
#              
# If you would like to modify this file for your personal ADF runs then it is recommended to make a copy of this file, make modifications in that copy, and then point the ADF to it using the `defaults_file` config variable in the <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/configs/yaml/runtime.html#defaults-file"><code class="docutils literal notranslate"><span class="pre">config_adf_tutorial.yaml</span></code> (copy of config_cam_baseline_example.yaml)</a>.
# 
# 
# :::{admonition} Example
# :class: seealso
# From the ADF root directory
# 
#     cp lib/adf_variable_defaults.yaml lib/my_variable_defaults.yaml
# 
# 
# In <code class="docutils literal notranslate"><span class="pre">config_adf_tutorial.yaml</span></code> (copy of config_cam_baseline_example.yaml):
# 
# Under the subset `diag_basic_info`:
# 
# <p style="margin-top: -5px;">&ensp; use_defaults: <code class="docutils literal notranslate"><span class="pre">false</span></code></p>
# 
# <p style="margin-top: -5px;">&ensp; defaults_file: <code class="docutils literal notranslate"><span class="pre">lib/your_variable_defaults.yaml</span></code></p>
# :::
# ::::
# 
# 
# <p>After the new file <code class="docutils literal notranslate"><span class="pre">lib/your_variable_defaults.yaml</span></code> has been created, open the file with your favorite editor</p>
# 
# Example of `U` 
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
# Example of variable `VAR` with custom observation dataset path 
# ```
# VAR:
#   obs_file: "OBS_for_VAR.nc"
#   obs_name: "/path/to/your/ADF_obs/SOME_OBS"
#   obs_var_name: "OBS_VAR"
#   category: "VAR_category"
# ```
::::{important}
:::{note}
This text is **standard** _Markdown_
:::
::::
# 

# 

# 

# 

# ### Running in the Terminal
# 
# Open a Cheyenne terminal window on your machine and navigate to the root directory of the ADF
# 
#     cd /glade/work/{user}/ADF/ 
#     
# Now we can run the ADF with our new config file `config_cam_vs_obs.yaml`
# 
#     time ./run_adf_diag config_cam_vs_obs.yaml
#     
# NOTE: the `time` command will give us a readout of the wall and user time for the ADF to run this configuration

# This will take a while, why don't you stretch your legs and get a snack :)
If the ADF finishes: 

```{admonition} Success?
<p id="box">Check output data/images:

Navigate to the diagnostic plots directory: `/glade/scratch/{user}/ADF/plots`

Then go to `f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001_1995_2000_vs_f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001_1995_2000/`
</p>
```

Navigate to the diagnostic plots directory: `/glade/scratch/{user}/ADF/plots`

Then go to `f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001_1995_2000_vs_f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001_1995_2000/`
# In[ ]:





#  ```{admonition} Did the ADF finish?
# <div id="box">
# <p>Check output data/images:</p>
# 
# <p style="margin-top: -5px;">Navigate to the diagnostic plots directory: <code class="docutils literal notranslate"><span class="pre">/glade/scratch/{user}/ADF/plots</span></code></p>
# 
# <p style="margin-top: -5px;">Then go to <code class="docutils literal notranslate"><span class="pre">f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001_1995_2000_vs_f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001_1995_2000/</span></code></p>
# </div>
# ```

#  ```{admonition} Did the ADF fail?
# :class: error
# Check config files   Check error/logs   Check data/paths
# ```

# <h4>End single CAM vs obs case</h4>
# 
# Hope everything went well...
# 
# ---

#  

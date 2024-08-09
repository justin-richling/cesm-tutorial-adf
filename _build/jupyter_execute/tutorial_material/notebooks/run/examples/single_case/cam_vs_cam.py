#!/usr/bin/env python
# coding: utf-8

# ## CAM vs CAM

# For this example we will run the ADF diagnostics for two different f-case CAM simulations for 5 years, 1995-2000:
# 
# <p>The test (experiment) case is <code class="docutils literal notranslate"><span class="pre">f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001</span></code></p>
# <p style="margin-top: -15px;">The baseline (control) case is <code class="docutils literal notranslate"><span class="pre">f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001</span></code></p>
# 
# Recall <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/intro/intro.html#adf-setup" target="_blank">the steps</a> we will take are to:
# 
# <s>&emsp; 0. Run CAM simulation to get history ( h0* ) file(s) 
#            *or other history files</s>
#                                    
# <p>&emsp; 1. Configure yaml file(s) for the history files<br>
# 
# &emsp; &emsp; <code class="docutils literal notranslate"><span class="pre">config_cam_baseline_example.yaml</span></code>  (necessary, must copy and change!)<br>
# &emsp; &emsp; &ensp;  Please refer back to the <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/intro/yaml/config_cam_baseline_example.html" target="_blank">run-time</a> section for any hints or descriptions of variables.<br>
# 
# &emsp; &emsp; <code class="docutils literal notranslate"><span class="pre">lib/adf_variable_defaults.yaml</span></code>   (necessary, but optional to copy and change)<br>
# &emsp; &emsp; &ensp;  For this example we <strong>will not</strong> be editing the variable defaults yaml file<br>
# </p>
# 
# <p>&emsp; 2. Run the ADF!</p>
# 
# 
# ---
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

# From the ADF root directory as set in the <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/install/setup.html#cloning-the-adf" target="_blank">cloning section</a> (/glade/work/&#60;user&#62;/ADF/), let's make a copy of the run-time config file:
# 
#     cp config_cam_baseline_example.yaml config_cam_vs_cam.yaml
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
# Open the new `config_cam_vs_cam.yaml` file with your favorite editor
# 
# The global variables will be set above the subsections.

#<section id="sidebars-within-content">

margin: 0 0 0.5em 1em;
    /*border: 1px solid #ddb;*/
    padding: 7px;
    background-color: #ffe;
    width: 40%;
    float: right;
    clear: right;
    overflow-x: auto;
    
<aside class="sidebar">


style="margin: 0 0 0.5em 1em; padding: 20px; width: 60%; float: right; clear: right; overflow-x: auto;"
# <section id="sidebar-content">
# <aside style="margin: 0 0 0.5em 1em; padding: 7px; width: 60%; float: right; clear: right; overflow-x: auto;">
# <div class="admonition note">
# <p class="admonition-title">Notezies</p>
# <p>Change only the ones listed in each subsection below and leave all the other variables in the conifg file as they are by default</p>
# </div>
# </aside>
# 
# 
# 
# * <p style="margin-top: -5px;">Global Variables</p>
# 
# The following subsections have variables that will be changed for this example:
# 
# * <p style="margin-top: -5px;">diag_basic_info</p>
# * <p style="margin-top: -5px;">diag_cam_climo</p>
# * <p style="margin-top: -5px;">diag_cam_baseline_climo</p>
# 
# </section>
Open the new `config_cam_vs_cam.yaml` file with your favorite editor

The global variables will be set above the subsections.

* <p style="margin-top: -5px;">Global Variables</p>

The following subsections have variables that will be changed for this example:

** Change only the ones listed in each subsection below and leave all the other variables in the conifg file as they are by default **

* <p style="margin-top: -5px;">diag_basic_info</p>
* <p style="margin-top: -5px;">diag_cam_climo</p>
* <p style="margin-top: -5px;">diag_cam_baseline_climo</p>
# ---

# ###### Global Variables
# 
# In the yaml file, let's set global variables. These variables will be set above all the subsections so that they can be easily called in anywhere in the file.
# 
# Set the user name that will be help set all paths later in the yaml file
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">user</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">richling (YOUR-USER-NAME)</span></code></p>
# 
# Create a new variable `adf_path` for the root ADF path. This will be used to house the different directories for the time series, climo, and regridded files as well as where the plots and websites will go
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">adf_path</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">/glade/scratch/${user}/ADF</span></code></p>
# 
# Also create a variable `hist_path` for the path to the sample history files
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">hist_path</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">/glade/scratch/richling/ADF/tutorials/data</span></code></p>
# 
# <div class="admonition attention">
# <p class="admonition-title">Attention</p>
# <p>This is meerly a suggestion of how to configure the locations of all the files and diagnostic plots. We will stick to this convention for this tutorial, but please feel free to setup your ADF diagnsotics paths/hieracrhy in anyway that makes sense for your actual needs!</p>    
# </div>
# 
# 
# 
# ###### diag_basic_info
# This subsection defines necessary variables for the overall ADF run
# 
# We can change the paths for the regridded data and plot locations
# 
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">cam_regrid_loc</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">${adf_path}/regrid</span></code></p>
# 
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">cam_diag_plot_loc</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">${adf_path}/plots</span></code></p>
# 
# ###### diag_cam_climo
# 
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">cam_case_name</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001</span></code></p>
# 
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">cam_hist_loc</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">${hist_path}/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001</span></code></p>
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">cam_climo_loc</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">${adf_path}/climo/{diag_cam_climo.cam_case_name}</span></code></p>
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">start_year</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">1995</span></code></p>
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">end_year</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">2000</span></code></p>
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">cam_ts_loc</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">${adf_path}/ts/{diag_cam_climo.cam_case_name}</span></code></p>
# 
# ###### diag_cam_baseline_climo
# 
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">cam_case_name</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001</span></code></p>
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">cam_hist_loc</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">${hist_path}/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001</span></code></p>
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">cam_climo_loc</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">${adf_path}/climo/{diag_cam_baseline_climo.cam_case_name}</span></code></p>
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">start_year</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">1995</span></code></p>
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">end_year</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">2000</span></code></p>
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">cam_ts_loc</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">${adf_path}/ts/{diag_cam_baseline_climo.cam_case_name}</span></code></p>

# ---
````{div} full-width
f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001_1995_2000_vs_f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001_1995_2000/
````
# <style>
#     #box {
#     word-wrap:normal;
#     overflow:scroll;
# }
# </style>
# 
# ````{div} full-width
# 
# <h5>With all these variables now set, let's take a quick catalogue of the different paths:</h5>
# 
# 
# Regridded file location:
# <div>
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">/glade/scratch/&#60;user&#62;/ADF/regrid</span></code></p>
# 
# Diagnostic plot location:
# 
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">/glade/scratch/&#60;user&#62;/ADF/plots</span></code></p>
# 
# <p>&emsp; &ensp;The ADF will output a new directory in the above location named:</p>
# 
# <p style="margin-top: -20px;"><code class="docutils literal notranslate"><span class="pre">&emsp; &ensp; f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001_1995_2000_vs_f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001_1995_2000/</span></code></p>
# 
# Climatology file locations:
# 
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">/glade/scratch/&#60;user&#62;/ADF/climo/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001</span></code></p>
# 
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">/glade/scratch/&#60;user&#62;/ADF/climo/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001</span></code></p>
# 
# Timeseries locations:
#     
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">/glade/scratch/&#60;user&#62;/ADF/ts/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001</span></code></p>
# 
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">/glade/scratch/&#60;user&#62;/ADF/ts/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001</span></code></p>
#     
# </div>
# 
# ````

# In[ ]:





# ---
#### adf_variable_defaults.yaml

Location for many plotting, unit, etc defualts for any/all CAM output variables

#### ADF Default Set

<p>If you want to use the ADF default values you need to set <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/configs/yaml/runtime.html#use-defaults"><code class="docutils literal notranslate"><span class="pre">use_defaults</span></code></a> in your copy of the config_yaml to true
</p>###### Custom Set

<p>If you plan on using a modified file for your custom values you need to set <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/configs/yaml/runtime.html#use-defaults"><code class="docutils literal notranslate"><span class="pre">use_defaults</span></code></a> in your copy of the config_yaml to false and set the path to the custom variable default file with <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/configs/yaml/runtime.html#defaults-file"><code class="docutils literal notranslate"><span class="pre">defaults_file</span></code></a>
</p>

::::{Warning}
<strong>Please do not modify this file unless you plan to push your changes back to the ADF repo!</strong>
             
If you would like to modify this file for your personal ADF runs then it is recommended to make a copy of this file, make modifications in that copy, and then point the ADF to it using the `defaults_file` config variable in the <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/configs/yaml/runtime.html#defaults-file"><code class="docutils literal notranslate"><span class="pre">config_adf_tutorial.yaml</span></code> (copy of config_cam_baseline_example.yaml)</a>.


:::{admonition} Example
:class: seealso
From the ADF root directory

    cp lib/adf_variable_defaults.yaml lib/my_variable_defaults.yaml


In <code class="docutils literal notranslate"><span class="pre">config_adf_tutorial.yaml</span></code> (copy of config_cam_baseline_example.yaml):

Under the subset `diag_basic_info`:

<p style="margin-top: -5px;">&ensp; use_defaults: <code class="docutils literal notranslate"><span class="pre">false</span></code></p>

<p style="margin-top: -5px;">&ensp; defaults_file: <code class="docutils literal notranslate"><span class="pre">lib/your_variable_defaults.yaml</span></code></p>
:::
::::


<p>After the new file <code class="docutils literal notranslate"><span class="pre">lib/your_variable_defaults.yaml</span></code> has been created, open the file with your favorite editor</p>

Example of `U` 
```
U:
  colormap: "Blues"
  contour_levels_range: [-10, 90, 5]
  diff_colormap: "BrBG"
  diff_contour_range: [-15, 15, 2]
  scale_factor: 1
  add_offset: 0
  new_unit: "ms$^{-1}$"
  mpl:
    colorbar:
      label : "ms$^{-1}$"
  obs_file: "U_ERA5_monthly_climo_197901-202112.nc"
  obs_name: "ERA5"
  obs_var_name: "U"
  vector_pair: "V"
  vector_name: "Wind"
  category: "State"
```


Example of custom variable `VAR` 
```
VAR:
  colormap: "Blues"
  contour_levels_range: [-10, 90, 5]
  diff_colormap: "BrBG"
  diff_contour_range: [-15, 15, 2]
  scale_factor: 1
  add_offset: 0
  new_unit: "ms$^{-1}$"
  mpl:
    colorbar:
      label : "ms$^{-1}$"
  obs_file: "U_ERA5_monthly_climo_197901-202112.nc"
  obs_name: "ERA5"
  obs_var_name: "U"
  vector_pair: "V"
  vector_name: "Wind"
  category: "State"
```::::{important}
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
#     cd /glade/work/<user>/ADF/ 
#     
# <p>Now we can run the ADF with our new config file `config_cam_vs_cam.yaml`<a class="headerlink" href="#adf-run" title="Permalink to this heading">#</a></p>
# 
#     time ./run_adf_diag config_cam_vs_cam.yaml
#     
# NOTE: the `time` command will give us a readout of the wall and user time for the ADF to run this configuration

# ```{Attention}
# This will take a while, why don't you stretch your legs and get a snack :)
# ```
If the ADF finishes: 

```{admonition} Success?
<p id="box">Check output data/images:

Navigate to the diagnostic plots directory: `/glade/scratch/&#60;user&#62;/ADF/plots`

Then go to `f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001_1995_2000_vs_f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001_1995_2000/`
</p>
```

Navigate to the diagnostic plots directory: `/glade/scratch/&#60;user&#62;/ADF/plots`

Check to see if this directory exists: `f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001_1995_2000_vs_f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001_1995_2000/`
# 

# <br><br><br><h4>End single CAM vs CAM case</h4>
# 
# <h6>Hope everything went well...</h6>
# 
# ````{div} full-width
# ```{admonition} Did the ADF finish?
# <div>
# <p>Check output data/images:</p>
# 
# <p style="margin-top: -5px;">Navigate to the diagnostic plots directory: <code class="docutils literal notranslate"><span class="pre">/glade/scratch/&#60;user&#62;/ADF/plots</span></code></p>
# 
# <p style="margin-top: -5px;">Check to see if this directory exists: <code class="docutils literal notranslate"><span class="pre">f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001_1995_2000_vs_f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001_1995_2000/</span></code></p>
# </div>
# ```
# ````
# 
# ```{admonition} Did the ADF fail?
# :class: error
# Check config files<br>
# Check error/logs<br>
# Check data/paths<br>
# ```
# 
# If you want to explore the ADF in a Jupyter environment, you can skip to the <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/run/Jupyter.html">ADF in Jupyter</a> chapter at the end of this section
# 
# ---

#  

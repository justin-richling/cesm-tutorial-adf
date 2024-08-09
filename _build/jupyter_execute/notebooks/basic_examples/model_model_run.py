#!/usr/bin/env python
# coding: utf-8
<section id="sidebar-content">
<aside style="margin: 0 0 0 1em; padding: 7px; width: 60%; float: right; clear: right; overflow-x: auto;">
<div class="admonition warning">
<p class="admonition-title">Note</p>
<p>Change only the variables listed in each subsection below and leave all the other variables in the conifg file as they are by default</p>
</div>
</aside>

<h4>We will be editing the following sections:</h4>

* <p style="margin-top: -5px;">Global Variables</p>
* <p style="margin-top: -5px;">diag_basic_info</p>
* <p style="margin-top: -5px;">diag_cam_climo</p>
* <p style="margin-top: -5px;">diag_cam_baseline_climo</p>

</section>
# # CAM vs CAM
# 
# <h5>This will be a simple guided demo of running the ADF with sample data for CAM vs CAM comparison.</h5>
# 
# For this example we will run the ADF diagnostics for two different f-case CAM simulations for 5 years, 1995-2000:
# 
# <p>The test (experiment) case is <code class="docutils literal notranslate"><span class="pre">f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001</span></code></p>
# <p style="margin-top: -15px;">The baseline (control) case is <code class="docutils literal notranslate"><span class="pre">f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001</span></code></p>
# 
# 
# 
# 
# ---
# 
# 
# 
# <h5>Use this as a follow along as you work locally for this example ADF run.</h5>
# 
# Navigate to where you cloned the ADF:
# 
# - If you followed our instructions earlier, you should have the ADF root directory at: `/glade/work/<user>/ADF/`
# 
# 
# 
# ### Configure Run-Time yaml file
# 
# ###### Introduction
# 
# Look for the conifuration yaml file that will be used to run the ADF: `config_baseline_example.yaml`
# 
# This is probably the most important file for the ADF. This stores all the necessary information that the ADF needs to run as well as all the relevant information about the case and baseline/observation/cmip runs.
# 
# 
# As a quick refresher from the intro to yaml section, we can utilize the `${}` notation to reference already declared variables elsewhere in the yaml files.
# 
# We will copy the provided configuration yaml file `config_baseline_example.yaml` and will do small edits to that copy and we will run an example ADF with some sample data.
# 
#     cp config_baseline_example.yaml config_model_vs_model_example.yaml
# 
# 
# 
# ###### Modify the Copy
# 
# <p>Next open this new copy in your favorite editor:
#     
#     emacs config_model_vs_model_example.yaml
# 
# Here we will do just a couple of changes for the output paths and cases/climo years
# </p>
# 
# 
# ##### <u>Subsections</u>
# 
# <style>
# mark { 
#   background-color: yellow;
#   color: black;
# }
# </style>
# 
# A quick refresher of the different sections in this yaml file. The highlighted scetions will be ones we will change variables in for this example.
# 
# <div class="admonition warning">
# <p class="admonition-title">Note</p>
# <p>Change only the variables listed in each highlighted subsection below and leave all the other variables in the conifg file as they are by default</p>
# </div>
# 
# * <mark>diag_basic_info</mark>
#     - Basic overall run variables
#     
# * <mark>diag_cam_climo</mark>
#     - Test (experiment) case variables
#     
# * <mark>diag_cam_baseline_climo</mark>
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
# <br>
# 
# ###### Global Variables
# 
# In the yaml file, above the `diag_basic_info` subsections let's set global variables. These variables will be set above all the subsections so that they can be easily called in anywhere in the file. Make sure there is no indentation between the variable name and the left margin of the file!
# 
# Set the user name that will be help set all paths later in the yaml file
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">user</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">richling (YOUR-USER-NAME)</span></code></p>
# 
# Set the variable `diag_loc` for the root ADF diagnostic data/plots paths. This will be used to house the different directories for the time series, climo, and regridded files as well as where the plots and websites will go
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">diag_loc</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">/glade/scratch/${user}/ADF</span></code></p>
# 
# Also set the variable `hist_path` for the path to the sample history files
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
# This subsection defines necessary variables for the overall ADF run. hange the following variables:
# 
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">cam_regrid_loc</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">${diag_loc}/regrid</span></code></p>
# 
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">cam_diag_plot_loc</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">${diag_loc}/plots</span></code></p>
# 
# ###### diag_cam_climo
# 
# This subsection follows the `diag_basic_info` and is used for the test (experiment) case run and diagnostics details. Change the following variables:
# 
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">cam_case_name</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001</span></code></p>
# 
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">cam_hist_loc</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">${hist_path}/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001</span></code></p>
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">cam_climo_loc</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">${diag_loc}/climo/{diag_cam_climo.cam_case_name}</span></code></p>
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">start_year</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">1995</span></code></p>
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">end_year</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">2000</span></code></p>
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">cam_ts_loc</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">${diag_loc}/ts/{diag_cam_climo.cam_case_name}</span></code></p>
# 
# ###### diag_cam_baseline_climo
# 
# This subsection follows the `diag_cam_climo` and is used for the baseline (control/target) case run and diagnostics details. Change the following variables:
# 
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">cam_case_name</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001</span></code></p>
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">cam_hist_loc</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">${hist_path}/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001</span></code></p>
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">cam_climo_loc</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">${diag_loc}/climo/{diag_cam_baseline_climo.cam_case_name}</span></code></p>
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">start_year</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">1995</span></code></p>
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">end_year</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">2000</span></code></p>
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">cam_ts_loc</span></code>: <code class="docutils literal notranslate"><span class="pre" style="color: black">${diag_loc}/ts/{diag_cam_baseline_climo.cam_case_name}</span></code></p>
# 
# 
# ---
# 
# <br><br>
# 
# <style>
#     #box {
#     word-wrap:normal;
#     overflow:scroll;
# }
# </style>
# 
# ````{div} full-width
# 
# <h3>With all these variables now set, let's take a quick catalogue of the different paths:</h3>
# 
# 
# <strong>Regridded file location:</strong>
# <div>
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre" style="color:black;">/glade/scratch/&#60;user&#62;/ADF/adf_tutorial/data/regrid/</span></code></p>
# 
# <strong>Diagnostic plot location:</strong>
# 
# <p style="margin-top: -5px; color:black;">&ensp; <code class="docutils literal notranslate"><span class="pre" style="color:black;">/glade/scratch/&#60;user&#62;/ADF/adf_tutorial/plots</span></code></p>
# 
# <p>&emsp; &ensp;The ADF will output a new directory in the above location named:</p>
# 
# <p style="margin-top: -20px;"><code class="docutils literal notranslate"><span class="pre" style="color:black;">&emsp; &ensp; f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001_1995_2000_vs_f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001_1995_2000/</span></code></p>
# 
# <strong>Climatology file locations:</strong>
# 
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre" style="color:black;">/glade/scratch/&#60;user&#62;/ADF/adf_tutorial/data/climo/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001</span></code></p>
# 
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre" style="color:black;">/glade/scratch/&#60;user&#62;/ADF/adf_tutorial/data/climo/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001</span></code></p>
# 
# <strong>Timeseries locations:</strong>
#     
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre" style="color:black;">/glade/scratch/&#60;user&#62;/ADF/adf_tutorial/data/ts/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001</span></code></p>
# 
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre" style="color:black;">/glade/scratch/&#60;user&#62;/ADF/adf_tutorial/data/ts/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001</span></code></p>
#     
# </div>
# 
# ````

# ### Run the ADF via terminal
# 
# With the run-time config file setup, the next step is to actaully run the ADF, oh boy! The most basic ADF run is through tthe terminal (although it can be run via Jupyter too, please see the <strong><a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/basic_examples/jupyter.html">ADF in Jupyter</a></strong> chapter in this <strong>Guided Examples</strong> section).
# 
# Make sure you are still in the root directory of the ADF .
# 
# From here, you just need to call the command line script `run_adf_diag` followed by the run-time config file we just editied `config_model_vs_model_example.yaml`
# 
#     ./run_adf_diag config_model_vs_model_example.yaml
#<aside style="margin: 0 0 0 1em; padding: 7px; width: 60%; float: right; clear: right; overflow-x: auto;">
<div class="admonition error" style="width: 60%;">
<p class="admonition-title">Did the ADF fail?</p>
Check config files<br>
Check error/logs<br>
Check data/paths<br>
</div>
# ### End single CAM vs CAM case
# 
# <h6>Hope everything went well...</h6>
# 
# ```{admonition} Did the ADF fail?
# :class: error
# Check config files<br>
# Check error/logs<br>
# Check data/paths<br>
# ```
# 
# 
````{div} full-width
```{admonition} Did the ADF finish?
<div>
<p>Check output data/images:</p>

<p style="margin-top: -5px;">Navigate to the diagnostic plots directory (<code class="docutils literal notranslate"><span class="pre">cam_diag_plot_loc</span></code>): <code class="docutils literal notranslate"><span class="pre">/glade/scratch/&#60;user&#62;/ADF/plots</span></code></p>

<p style="margin-top: -5px;">Check to see if this directory exists: <code class="docutils literal notranslate"><span class="pre">f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001_1995_2000_vs_f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001_1995_2000/</span></code></p>
</div>
```
````
If you want to explore the ADF in a Jupyter environment, you can skip to the <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/run/Jupyter.html">ADF in Jupyter</a> chapter at the end of this section

---
# ### Check the outputs!
# 
# 
# We can now check the output diagnostics from a couple ways:
# 
# <h4>Locally</h4>
# 
# If the ADF ran successfully, we can navigate to where we set the diagnostic plots output:
# 
# `````{div} full-width
# 
# &ensp;On a CISL machine, navigate to the root ADF directory
# 
# <code class="docutils literal notranslate"><span class="pre" style="color:black">&emsp;/glade/scratch/&#60;user&#62;/ADF/plots/</span></code>
# 
# &ensp;Then go to where you assigned the `cam_diag_plot_loc` location in the run-time config file
# 
# <code class="docutils literal notranslate"><span class="pre" style="color:black">&emsp;f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001_1995_2000_vs_f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001_1995_2000/</span></code>
# 
# `````
# 

# <h4>JupyterHub</h4>
# 
# apidfjwd

# <h4>Website</h4>
# 
# If you choose to create HTML files you can publish those to a web server. In the diagnostics plotting location (<code class="docutils literal notranslate"><span class="pre">cam_diag_plot_loc</span></code>) you set in the run-time config file, a `website` directory exists where all the html and css files are saved.
# 
# `````{div} full-width
#     .
#     ├── plots
#     │   └── f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001_1995_2000_vs_f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001_1995_2000
#     │       └── website
#     │           ├── assets
#     │           ├── html_img
#     │           ├── html_table
#     │           └── templates
# `````

# Example: If you have a project page on a CGD machine like Tungsten, it is a simple secure copy of files to the server:
# 
# <style>
#     #box {
#     word-wrap:normal;
#     overflow:scroll;
# }
# </style>
# 
# 
# &ensp;Navigate to the `cam_diag_plot_loc` location and copy all the files from the `website` directory to the server address:
# 
# &emsp;For Tungsten:
# &emsp;    <code class="docutils literal notranslate"><span class="pre" style="color: black;">scp -r website/* tungsten.cgd.ucar.edu:/path/to/your/project/page/</span></code>)
# 

# 
# 
# <div class="admonition tip" style="padding-right: 7px">
# <div><h6>A sample website:</h6></div>
# <p><a href="https://project.cgd.ucar.edu/projects/ADF/examples/single-case/cam_vs_cam/" target="_blank">https://project.cgd.ucar.edu/projects/ADF/examples/single-case/cam_vs_cam/</a></p>
# </div>
# 
# 

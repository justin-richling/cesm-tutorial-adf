#!/usr/bin/env python
# coding: utf-8

# # CAM vs Model Intercomparison
# 
# This will be a simple guided demo of running the ADF with sample data for CAM vs model intercomparison simulations (ie AMIP, CMIP etc).
# 
# Use this as a follow along as you work locally for this example ADF run.
# 
# Navigate to where you cloned the ADF:
# 
# - If you followed our instructions earlier, you should have the ADF root directory at: `/glade/work/<user>/ADF/`
# 
# 
# 
# For this guided demo we will first make a copy of the run-time config file and make some changes in that copy.
# 
# 
# 
# ### Configure Run-Time yaml file
# 
# ###### Introduction
# 
# <p>Look for the conifuration yaml file that will be used to run the ADF, `config_baseline_example.yaml`
# 
# This is probably the most important file for the ADF. This stores all the necessary information that the ADF needs to run as well as all the relevant information about the case and baseline/observation/cmip runs.</p>
# 
# Each section of the yaml file represent grouped subsets of information sent to the ADF and each have variable names that get fed into the ADF in a specific fashion.
# 
# We will copy the provided configuration yaml file `config_baseline_example.yaml` and will do small edits to run an example ADF with sample data.
# 
#     cp config_baseline_example.yaml config_tutorial_example.yaml
# 
# </p>
# 
# ###### Modify the Copy
# 
# <p>Next open this new copy in your favorite editor:
#     
#     emacs config_tutorial_example.yaml
# 
# Here we will do just a couple of changes for the output paths and cases/climo years
# </p>
# 
# 
# ##### <u>Subsections</u>
# 
# A quick refresher of the different sections on this yaml file
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
# <section id="sidebar-content">
# <aside style="margin: 0 0 0 1em; padding: 7px; width: 60%; float: right; clear: right; overflow-x: auto;">
# <div class="admonition warning">
# <p class="admonition-title">Note</p>
# <p>Change only the variables listed in each subsection below and leave all the other variables in the conifg file as they are by default</p>
# </div>
# </aside>
# 
# <h4>We will be editing the following sections:</h4>
# 
# * <p style="margin-top: -5px;">Global Variables</p>
# * <p style="margin-top: -5px;">diag_basic_info</p>
# * <p style="margin-top: -5px;">diag_cam_climo</p>
# 
# </section>
# 
# <br><br><br>
# 
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
# <p style="margin-top: -20px;"><code class="docutils literal notranslate"><span class="pre">&emsp; &ensp; f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001_1995_2000_vs_Obs/</span></code></p>
# 
# Climatology file locations:
# 
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">/glade/scratch/&#60;user&#62;/ADF/climo/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001</span></code></p>
# 
# 
# 
# Timeseries locations:
#     
# <p style="margin-top: -5px;">&ensp; <code class="docutils literal notranslate"><span class="pre">/glade/scratch/&#60;user&#62;/ADF/ts/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001</span></code></p>
# 
# 
#     
# </div>
# 
# ````

#!/usr/bin/env python
# coding: utf-8

# # Running ADF Basics
# 
# Now that the environment is setup with the required modules loaded and the ADF cloned let's put it all together and do a CAM vs CAM comparison!

# ## How to run the ADF
# 
# There are two ways to run the ADF, the first and most stright forward is runnning the ADF in the terminal and the second is via Jupyter.
# 
# The first steps are to set the desired (and required) variables in the config yaml file(s). In this demo, we will run the ADF standard variable defaults file (`adf_variable_defaults.yaml`), but feel free to explore making your own, please refer back to the <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/intro/yaml/adf_variable_defaults.html" target="_blank">Variable Defaults</a> yaml section.
# 
# 
# 
# 
# ## Types of ADF Comparisons
# 
# There are a couple different ADF runs one can do:
# 
# <p>Single Case Comparison</p>
# <p>Multiple Case Comparison**</p>
# <p style="margin-top: -15px;">&ensp; ** In progress, will not be part of this tutorial currently :(</p>
# 
# ## Available Comparison Cases
# 
# There are essentially 3 types of comparisons:
# 
# * CAM vs CAM
# * CAM vs Observations/Reanalysis
# * CAM vs CMIP
# 
# Each have their own requirements for the run-time config file (eg `config_cam_baseline_example`). The requirements for each type of comparison will be addressed in their respective sections of this tutorial.
# 

# ### Single Case Comparison
# 
# By default the ADF will run a single CAM test simulation (experiment) case vs baseline (control) case.

# ---

# First step: Setup the Run-time config file
# 
# Navigate to the ADF root directory if you're not already there.
# 
# ADF/

# #### CAM vs CAM
# 
# 

# 
# Make a copy of the <code class="docutils literal notranslate"><span class="pre">config_cam_baseline_example.yaml</span></code> file
# 
# ```
# cp config_cam_baseline_example.yaml config_cam_vs_cam_demo.yaml
# 
# ```
# 
# Then, open <code class="docutils literal notranslate"><span class="pre">config_cam_vs_cam_demo.yaml</span></code> in your favorite editor.
# 
# We will do a simple run of two CAM siumulations, with the sample data living at:
# 

# test case: f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001 (1995-2012)
# <code class="docutils literal notranslate"><span class="pre">/glade/work/richling/ADF/adf-tutorials/data/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001</span></code>
# 
# baseline case: f.cam6_3_105.FLTHIST_v0a.ne30.001 (1979-2002)
# <code class="docutils literal notranslate"><span class="pre">/glade/work/richling/ADF/adf-tutorials/data/f.cam6_3_105.FLTHIST_v0a.ne30.001</span></code>
# 
# Let's pick a couple of years that are in common with these two datasets.
# 
# NOTE: it is not necessary that the climo years match between cases, which is typical, especially when comparing against obs or AMIP/CMIP cases.
<div class="admonition">
<p>config_cam_vs_cam_demo.yaml</p>
  <div class="admonition error">
  <div class="title">Oh jeez, I hope this worked...</div>
  <p>Paragraph 1</p>
  <p>Paragraph 2</p>
  </div>
    
  <div class="admonition tip">
  <div class="title">A *title*</div>
  <p>Paragraph 1</p>
  <p>Paragraph 2</p>
    </div>
</div>
# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# <h3><strong>config_cam_vs_cam_demo.yaml</strong></h3>
# <div class="admonition">
#     
# <p># This file doesn't (yet) read environment variables, so the user must<br>
# # set this themselves. It is also a good idea to search the doc for 'user'<br>
# # to see what default paths are being set for output/working files.<br>
# #<br>
# # Note that the string 'USER-NAME-NOT-SET' is used in the jupyter script<br>
# # to check for a failure to customize<br>
# #</p>
# <div class="admonition attention">
# <p><strong>user:</strong> 'USER-NAME-NOT-SET' -> <font color="red">CHANGE ME!</font></p>
# </div>
# 
# <p>#This first set of variables specify basic info used by all diagnostic runs:<br>
# <strong><a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/intro/yaml/config_cam_baseline_example.html#strong-diag-basic-info-strong" target="_blank">diag_basic_info:</a></strong></p>
# 
# 
# <p>&emsp;#History file string to match (eg. cam.h0 or ocn.pop.h.ecosys.nday1)<br>
# &emsp;# Only affects timeseries as everything else uses timeseries <br>
# &emsp;# Leave off trailing '.'<br>
# &emsp;#Default: cam.h0<br>
# &emsp;<strong>hist_str:</strong> cam.h0 </p>          
# 
# <p>&emsp;#Is this a model vs observations comparison?<br>
# &emsp;#If "false" or missing, then a model-model comparison is assumed:<br>
# &emsp;<strong>compare_obs:</strong> false</p>
# 
# <p>&emsp;#Generate HTML website (assumed false if missing):<br>
# &emsp;#Note:  The website files themselves will be located in the path<br>
# &emsp;#specified by "cam_diag_plot_loc", under the "diag_run/website" subdirectory,<br>
# &emsp;#where "diag_run" is the subdirectory created for this particular diagnostics run<br>
# &emsp;#(usually "case_vs_obs_XXX" or "case_vs_baseline_XXX").<br>
# &emsp;<strong>create_html:</strong> true</p>
# 
# <p>&emsp;#Location of observational datasets:<br>
# &emsp;#Note: this only matters if "compare_obs" is true and the path<br>
# &emsp;#isn't specified in the variable defaults file.<br>
# &emsp;<strong>obs_data_loc:</strong> /glade/work/nusbaume/SE_projects/model_diagnostics/ADF_obs</p>
# 
# <div class="admonition attention">
# <p>&emsp;#Location where re-gridded and interpolated CAM climatology files are stored:<br>
# &emsp;<strong>cam_regrid_loc:</strong> /glade/scratch/${user}/ADF/regrid -> <span style="color:red">Change if desired!</span></p>
# </div>
# 
# <p>&emsp;#Overwrite CAM re-gridded files?<br>
# &emsp;<strong>cam_overwrite_regrid</strong>: false</p>
# 
# <div class="admonition attention">
# <p>&emsp;#Location where diagnostic plots are stored:<br>
# &emsp;<strong>cam_diag_plot_loc:</strong> /glade/scratch/${user}/ADF/plots -> <span style="color:red">Change if desired!</span></p>
# </div>
# 
# <p>&emsp;#Use default variable plot settings?<br>
# &emsp;#If "true", then variable-specific plotting attributes as defined in<br>
# &emsp;#ADF/lib/adf_variable_defaults.yaml will be used:<br>
# &emsp;<strong>use_defaults:</strong> true</p>
# 
# <p>&emsp;#Location of ADF variable plotting defaults YAML file<br>
# &emsp;#if not using the one in ADF/lib:<br>
# &emsp;<strong>#defaults_file:</strong> /some/path/to/defaults/file</p>
# 
# <p>&emsp;#Vertical pressure levels (in hPa) on which to plot 3-D variables<br>
# &emsp;#when using horizontal (e.g. lat/lon) map projections.<br>
# &emsp;#If this config option is missing, then no 3-D variables will be plotted on<br>
# &emsp;#horizontal maps.  Please note too that pressure levels must currently match<br>
# &emsp;#what is available in the observations file in order to be plotted in a<br>
# &emsp;#model vs obs run:<br>
# &emsp;<strong>plot_press_levels:</strong> [200,850]</p>
# 
# <p>&emsp;#Longitude line on which to center all lat/lon maps.<br>
# &emsp;#If this config option is missing then the central<br>
# &emsp;#longitude will default to 180 degrees E.<br>
# &emsp;<strong>central_longitude:</strong> 180</p>
# 
# <p>&emsp;#Number of processors on which to run the ADF.<br>
# &emsp;#If this config variable isn't present then<br>
# &emsp;#the ADF defaults to one processor.  Also, if<br>
# &emsp;#you set it to "*" then it will default<br>
# &emsp;#to all of the processors available on a<br>
# &emsp;#single node/machine:<br>
# &emsp;<strong>num_procs:</strong> 8</p>
# 
# <p>&emsp;#If set to true, then redo all plots even if they already exist.<br>
# &emsp;#If set to false, then if a plot is found it will be skipped:<br>
# &emsp;<strong>redo_plot:</strong> false</p>
# 
# 
#     
#     
#     
#     
#     
#     
#     
#     
#     
# <p>#This second set of variables provides info for the CAM simulation(s) being diagnosed:<br>
# <strong><a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/intro/yaml/config_cam_baseline_example.html#strong-diag-cam-climo-strong" target="_blank">diag_cam_climo:</a></strong></p>
# 
# <p>&emsp;#Calculate climatologies?<br>
# &emsp;#If false, the climatology files will not be created:<br>
# &emsp;<strong>calc_cam_climo:</strong> true</p>
# 
# <p>&emsp;#Overwrite CAM climatology files?<br>
# &emsp;#If false, or not prsent, then already existing climatology files will be skipped:<br>
# &emsp;<strong>cam_overwrite_climo:</strong> false</p>
# 
# <div class="admonition attention">
# <p>&emsp;#Name of CAM case (or CAM run name):<br>
# &emsp;<strong>cam_case_name:</strong> b.e20.BHIST.f09_g17.20thC.297_05</p>
# </div>
# 
# <p>&emsp;#Case nickname<br>
# &emsp;#NOTE: if nickname starts with '0' - nickname must be in quotes!<br>
# &emsp;# ie '026a' as opposed to 026a<br>
# &emsp;#If missing or left blank, will default to cam_case_name<br>
# &emsp;<strong>case_nickname:</strong> #cool nickname</p>
# 
# <div class="admonition attention">
# <p>&emsp;#Location of CAM history (h0) files:<br>
# &emsp;#Example test files<br>
# &emsp;<strong>cam_hist_loc:</strong> /glade/p/cesm/ADF/${diag_cam_climo.cam_case_name}</p>
# </div>
# 
# <div class="admonition attention">
# <p>&emsp;#Location of CAM climatologies (to be created and then used by this script)<br>
# &emsp;<strong>cam_climo_loc:</strong> /glade/scratch/${user}/ADF/${diag_cam_climo.cam_case_name}/climo</p>
# </div>
# 
# <div class="admonition attention">
# <p>&emsp;#model year when time series files should start:<br>
# &emsp;#Note:  Leaving this entry blank will make time series<br>
# &emsp;#       start at earliest available year.<br>
# &emsp;<strong>start_year:</strong> 1990</p>
# </div>
# 
# <div class="admonition attention">
# <p>&emsp;#model year when time series files should end:<br>
# &emsp;#Note:  Leaving this entry blank will make time series<br>
# &emsp;#       end at latest available year.<br>
# &emsp;<strong>end_year:</strong> 1999</p>
# </div>
# 
# <p>&emsp;#Do time series files exist?<br>
# &emsp;#If True, then diagnostics assumes that model files are already time series.<br>
# &emsp;#If False, or if simply not present, then diagnostics will attempt to create<br>
# &emsp;#time series files from history (time-slice) files:<br>
# &emsp;<strong>cam_ts_done:</strong> false</p>
# 
# <p>&emsp;#Save interim time series files?<br>
# &emsp;#WARNING:  This can take up a significant amount of space,<br>
# &emsp;#          but will save processing time the next time<br>
# &emsp;<strong>cam_ts_save:</strong> true</p>
# 
# <p>&emsp;#Overwrite time series files, if found?<br>
# &emsp;#If set to false, then time series creation will be skipped if files are found:<br>
# &emsp;<strong>cam_overwrite_ts:</strong> false</p>
# 
# <div class="admonition attention">
# <p>&emsp;#Location where time series files are (or will be) stored:<br>
# &emsp;<strong>cam_ts_loc:</strong> /glade/scratch/${user}/ADF/${diag_cam_climo.cam_case_name}/ts</p>
# </div>
#     
#     
#     
#     
# 
# </div>

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




<h3><strong>config_cam_vs_cam_demo.yaml</strong></h3>
<div class="admonition">

<p>#Change to your user name!<br>user: 'richling'<br>
#This first set of variables specify basic info used by all diagnostic runs:<br>
<strong>diag_basic_info:</strong></p>

<div class="admonition attention">
<p>&ensp;<strong>diag_loc:</strong> /glade/scratch/${user}/ADF_output/TEST/ -> <font color="red">CHANGE ME!</font></p>
</div>

<p>&ensp;climo_loc: /glade/scratch/richling/ADF/tutorials/data/output/climos/<br>
&ensp;<strong>ts_loc:</strong> /glade/scratch/richling/ADF/tutorials/data/output/timeseries/</p>

<p>&ensp;#History file string to match (eg. cam.h0 or ocn.pop.h.ecosys.nday1)<br>
&ensp;# Only affects timeseries as everything else uses timeseries <br>
&ensp;# Leave off trailing '.'<br>
&ensp;#Default: cam.h0<br>
&ensp;<strong>hist_str:</strong> cam.h0 </p>          

<p>&ensp;#Is this a model vs observations comparison?<br>
&ensp;#If "false" or missing, then a model-model comparison is assumed:<br>
&ensp;<strong>compare_obs:</strong> false</p>

<p>&ensp;#Generate HTML website (assumed false if missing):<br>
&ensp;#Note:  The website files themselves will be located in the path<br>
&ensp;#specified by "cam_diag_plot_loc", under the "diag_run/website" subdirectory,<br>
&ensp;#where "diag_run" is the subdirectory created for this particular diagnostics run<br>
&ensp;#(usually "case_vs_obs_XXX" or "case_vs_baseline_XXX").<br>
&ensp;<strong>create_html:</strong> true</p>

<p>&ensp;#Location of observational datasets:<br>
&ensp;#Note: this only matters if "compare_obs" is true and the path<br>
&ensp;#isn't specified in the variable defaults file.<br>
&ensp;<strong>obs_data_loc:</strong> /glade/work/nusbaume/SE_projects/model_diagnostics/ADF_obs</p>

<div class="admonition attention">
    <p>&ensp;#Location where re-gridded and interpolated CAM climatology files are stored:<br>
    &ensp;<strong>cam_regrid_loc:</strong> /glade/scratch/richling/ADF/tutorials/data/output/regrid/ -> <span style="color:red">CHANGE ME!</span></p>
</div>
    
<p>&ensp;#Overwrite CAM re-gridded files?<br>
&ensp;<strong>cam_overwrite_regrid</strong>: false</p>

<div style="padding-top: -30px" class="admonition attention">
    <p>&ensp;#Location where diagnostic plots are stored:<br>
        &ensp;<strong>cam_diag_plot_loc:</strong> ${diag_loc}diag-plot/ -> <span style="color:red">CHANGE ME!</span></p>
</div>
<p>&ensp;#Use default variable plot settings?<br>
&ensp;#If "true", then variable-specific plotting attributes as defined in<br>
&ensp;#ADF/lib/adf_variable_defaults.yaml will be used:<br>
&ensp;<strong>use_defaults:</strong> true</p>

<p>&ensp;#Location of ADF variable plotting defaults YAML file<br>
&ensp;#if not using the one in ADF/lib:<br>
&ensp;<strong>#defaults_file:</strong> /some/path/to/defaults/file</p>

<p>&ensp;#Vertical pressure levels (in hPa) on which to plot 3-D variables<br>
&ensp;#when using horizontal (e.g. lat/lon) map projections.<br>
&ensp;#If this config option is missing, then no 3-D variables will be plotted on<br>
&ensp;#horizontal maps.  Please note too that pressure levels must currently match<br>
&ensp;#what is available in the observations file in order to be plotted in a<br>
&ensp;#model vs obs run:<br>
&ensp;<strong>plot_press_levels:</strong> [200,850]</p>

<p>&ensp;#Longitude line on which to center all lat/lon maps.<br>
&ensp;#If this config option is missing then the central<br>
&ensp;#longitude will default to 180 degrees E.<br>
&ensp;<strong>central_longitude:</strong> 180</p>

<p>&ensp;#Apply monthly weights to seasonal averages.<br>
&ensp;#If False or missing, then all months are<br>
&ensp;#given the same weight:<br>
&ensp;<strong>weight_season:</strong> True</p>

<p>&ensp;#Number of processors on which to run the ADF.<br>
&ensp;#If this config variable isn't present then<br>
&ensp;#the ADF defaults to one processor.  Also, if<br>
&ensp;#you set it to "*" then it will default<br>
&ensp;#to all of the processors available on a<br>
&ensp;#single node/machine:<br>
&ensp;<strong>num_procs:</strong> 8</p>

<p>&ensp;#If set to true, then redo all plots even if they already exist.<br>
&ensp;#If set to false, then if a plot is found it will be skipped:<br>
&ensp;<strong>redo_plot:</strong> false</p>

</div>
# In[ ]:





# In[ ]:





# In[ ]:





# 

# In[ ]:





# In[ ]:





# In[ ]:




#==============================
#config_cam_baseline_example.yaml

#This is the main CAM diagnostics config file
#for doing comparisons of a CAM run against
#another CAM run, or a CAM baseline simulation.

#Currently, if one is on NCAR's Casper or
#Cheyenne machine, then only the diagnostic output
#paths are needed, at least to perform a quick test
#run (these are indicated with "MUST EDIT" comments).
#Running these diagnostics on a different machine,
#or with a different, non-example simulation, will
#require additional modifications.
#
#Config file Keywords:
#--------------------
#
#1.  Using ${xxx} will substitute that text with the
#    variable referenced by xxx. For example:
#
#    cam_case_name: cool_run
#    cam_climo_loc: /some/where/${cam_case_name}
#
#    will set "cam_climo_loc" in the diagnostics package to:
#    /some/where/cool_run
#
#    Please note that currently this will only work if the
#    variable only exists in one location in the file.
#
#2.  Using ${<top_level_section>.xxx} will do the same as
#    keyword 1 above, but specifies which sub-section the
#    variable is coming from, which is necessary for variables
#    that are repeated in different subsections.  For example:
#
#    diag_basic_info:
#      cam_climo_loc:  /some/where/${diag_cam_climo.start_year}
#
#    diag_cam_climo:
#      start_year: 1850
#
#    will set "cam_climo_loc" in the diagnostics package to:
#    /some/where/1850
#
#Finally, please note that for both 1 and 2 the keywords must be lowercase.
#This is because future developments will hopefully use other keywords
#that are uppercase. Also please avoid using periods (".") in variable
#names, as this will likely cause issues with the current file parsing
#system.
#--------------------
#
##==============================
#
# This file doesn't (yet) read environment variables, so the user must
# set this themselves. It is also a good idea to search the doc for 'user'
# to see what default paths are being set for output/working files.
#
# Note that the string 'USER-NAME-NOT-SET' is used in the jupyter script
# to check for a failure to customize
#

#Change to your user name!
user: 'richling'


#This first set of variables specify basic info used by all diagnostic runs:
diag_basic_info:

    # Change this to a path on your machine!
    # This is just a suggestion
    diag_loc: /glade/scratch/${user}/ADF_output/TEST/

    climo_loc: /glade/scratch/richling/ADF/tutorials/data/output/climos/
    ts_loc: /glade/scratch/richling/ADF/tutorials/data/output/timeseries/

    #History file string to match (eg. cam.h0 or ocn.pop.h.ecosys.nday1)
    # Only affects timeseries as everything else uses timeseries 
    # Leave off trailing '.'
    #Default: cam.h0
    hist_str: cam.h0           

    #Is this a model vs observations comparison?
    #If "false" or missing, then a model-model comparison is assumed:
    compare_obs: false

    #Generate HTML website (assumed false if missing):
    #Note:  The website files themselves will be located in the path
    #specified by "cam_diag_plot_loc", under the "<diag_run>/website" subdirectory,
    #where "<diag_run>" is the subdirectory created for this particular diagnostics run
    #(usually "case_vs_obs_XXX" or "case_vs_baseline_XXX").
    create_html: true

    #Location of observational datasets:
    #Note: this only matters if "compare_obs" is true and the path
    #isn't specified in the variable defaults file.
    obs_data_loc: /glade/work/nusbaume/SE_projects/model_diagnostics/ADF_obs

    #Location where re-gridded and interpolated CAM climatology files are stored:
    cam_regrid_loc: /glade/scratch/richling/ADF/tutorials/data/output/regrid/

    #Overwrite CAM re-gridded files?
    #If false, or missing, then regridding will be skipped for regridded variables
    #that already exist in "cam_regrid_loc":
    cam_overwrite_regrid: false

    #Location where diagnostic plots are stored:
    cam_diag_plot_loc: ${diag_loc}diag-plot/

    #Use default variable plot settings?
    #If "true", then variable-specific plotting attributes as defined in
    #ADF/lib/adf_variable_defaults.yaml will be used:
    use_defaults: true

    #Location of ADF variable plotting defaults YAML file
    #if not using the one in ADF/lib:
  #  defaults_file: /some/path/to/defaults/file

    #Vertical pressure levels (in hPa) on which to plot 3-D variables
    #when using horizontal (e.g. lat/lon) map projections.
    #If this config option is missing, then no 3-D variables will be plotted on
    #horizontal maps.  Please note too that pressure levels must currently match
    #what is available in the observations file in order to be plotted in a
    #model vs obs run:
    plot_press_levels: [200,850]

    #Longitude line on which to center all lat/lon maps.
    #If this config option is missing then the central
    #longitude will default to 180 degrees E.
    central_longitude: 180

    #Apply monthly weights to seasonal averages.
    #If False or missing, then all months are
    #given the same weight:
    weight_season: True

    #Number of processors on which to run the ADF.
    #If this config variable isn't present then
    #the ADF defaults to one processor.  Also, if
    #you set it to "*" then it will default
    #to all of the processors available on a
    #single node/machine:
    num_procs: 8

    #If set to true, then redo all plots even if they already exist.
    #If set to false, then if a plot is found it will be skipped:
    redo_plot: false


#This second set of variables provides info for the CAM simulation(s) being diagnosed:
diag_cam_climo:

    #Calculate climatologies?
    #If false, neither the climatology or time-series files will be created:
    calc_cam_climo: true

    #Overwrite CAM climatology files?
    #If false, or not prsent, then already existing climatology files will be skipped:
    cam_overwrite_climo: false

    #Name of CAM case (or CAM run name):
    cam_case_name: f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001
    
    #Case nickname
    case_nickname: ${diag_cam_climo.cam_case_name}

    #Location of CAM history (h0) files:
    #Example test files
    cam_hist_loc: /glade/scratch/richling/ADF/tutorials/data/${diag_cam_climo.cam_case_name}/

    #Location of CAM climatologies (to be created and then used by this script)
    cam_climo_loc: ${climo_loc}${diag_cam_climo.cam_case_name}/

    #model year when time series files should start:
    #Note:  Leaving this entry blank will make time series
    #       start at earliest available year.
    start_year: 1995

    #model year when time series files should end:
    #Note:  Leaving this entry blank will make time series
    #       end at latest available year.
    end_year: 2012

    #Do time series files need to be generated?
    #If True, then diagnostics assumes that model files are already time series.
    #If False, or if simply not present, then diagnostics will attempt to create
    #time series files from history (time-slice) files:
    cam_ts_done: false

    #Save interim time series files?
    #WARNING:  This can take up a significant amount of space,
       #          but will save processing time the next time
    cam_ts_save: true

    #Overwrite time series files, if found?
    #If set to false, then time series creation will be skipped if files are found:
    cam_overwrite_ts: false

    #Location where time series files are (or will be) stored:
    cam_ts_loc: ${ts_loc}${diag_cam_climo.cam_case_name}/


#This third set of variables provide info for the CAM baseline climatologies.
#This only matters if "compare_obs" is false:
diag_cam_baseline_climo:

    #Calculate cam baseline climatologies?
    #If false, neither the climatology or time-series files will be created:
    calc_cam_climo: true

    #Overwrite CAM climatology files?
    #If false, or not present, then already existing climatology files will be skipped:
    cam_overwrite_climo: false

    #Name of CAM baseline case:
    cam_case_name: f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001
    
    #Case nickname
    case_nickname: ${diag_cam_baseline_climo.cam_case_name} 

    #Location of CAM baseline history (h0) files:
    #Example test files
    cam_hist_loc: /glade/scratch/richling/ADF/tutorials/data/${diag_cam_baseline_climo.cam_case_name}/

    #Location of baseline CAM climatologies:
    cam_climo_loc: ${climo_loc}${diag_cam_baseline_climo.cam_case_name}/

    #model year when time series files should start:
    #Note:  Leaving this entry blank will make time series
    #       start at earliest available year.
    start_year: 1995

    #model year when time series files should end:
    #Note:  Leaving this entry blank will make time series
    #       end at latest available year.
    end_year: 2012

    #Do time series files need to be generated?
    #If True, then diagnostics assumes that model files are already time series.
    #If False, or if simply not present, then diagnostics will attempt to create
    #time series files from history (time-slice) files:
    cam_ts_done: false

    #Save interim time series files for baseline run?
    #WARNING:  This can take up a significant amount of space:
    cam_ts_save: true

    #Overwrite baseline time series files, if found?
    #If set to false, then time series creation will be skipped if files are found:
    cam_overwrite_ts: false

    #Location where time series files are (or will be) stored:
    cam_ts_loc: ${ts_loc}${diag_cam_baseline_climo.cam_case_name}/

#This fourth set of variables provides settings for calling the Climate Variability
# Diagnostics Package (CVDP). If cvdp_run is set to true the CVDP will be set up and
# run in background mode, likely completing after the ADF has completed.
# If CVDP is to be run PSL, TREFHT, TS and PRECT (or PRECC and PRECL) should be listed
# in the diag_var_list variable listing.
# For more CVDP information: https://www.cesm.ucar.edu/working_groups/CVC/cvdp/
diag_cvdp_info:

    # Run the CVDP on the listed run(s)?
    cvdp_run: false

    # CVDP code path, sets the location of the CVDP codebase
    #  CGD systems path = /home/asphilli/CESM-diagnostics/CVDP/Release/v5.2.0/
    #  CISL systems path = /glade/u/home/asphilli/CESM-diagnostics/CVDP/Release/v5.2.0/
    #  github location = https://github.com/NCAR/CVDP-ncl
    cvdp_codebase_loc: /glade/u/home/asphilli/CESM-diagnostics/CVDP/Release/v5.2.0/

    # Location where cvdp codebase will be copied to and diagnostic plots will be stored
    cvdp_loc: /glade/scratch/asphilli/ADF-Sandbox/cvdp/      #MUST EDIT!

    # tar up CVDP results?
    cvdp_tar: false


#+++++++++++++++++++++++++++++++++++++++++++++++++++
#These variables below only matter if you are using
#a non-standard method, or are adding your own
#diagnostic scripts.
#+++++++++++++++++++++++++++++++++++++++++++++++++++

#Note:  If you want to pass arguments to a particular script, you can
#do it like so (using the "averaging_example" script in this case):
# - {create_climo_files: {kwargs: {clobber: true}}}

#Name of time-averaging scripts being used to generate climatologies.
#These scripts must be located in "scripts/averaging":
time_averaging_scripts:
    - create_climo_files

#Name of regridding scripts being used.
#These scripts must be located in "scripts/regridding":
regridding_scripts:
    - regrid_and_vert_interp

#List of analysis scripts being used.
#These scripts must be located in "scripts/analysis":
analysis_scripts:
    - amwg_table

#List of plotting scripts being used.
#These scripts must be located in "scripts/plotting":
plotting_scripts:
    - global_latlon_map
    #- global_latlon_vect_map
    - zonal_mean
    #- meridional_mean
    #- polar_map
    #- cam_taylor_diagram
    #- qbo
    #- regional_map_multicase #To use this please un-comment and fill-out
                              #the "region_multicase" section below

#List of CAM variables that will be processesd:
#If CVDP is to be run PSL, TREFHT, TS and PRECT (or PRECC and PRECL) should be listed
diag_var_list:
   #- CLDHGH
   #- CLDICE
   #- CLDLIQ
   #- CLDLOW
   #- CLDMED
   #- CLDTOT
   #- CLOUD
   #- FLNS
   - FLNT
   #- FLNTC
   #- FSNS
   - FSNT
   #- FSNTC
   #- LHFLX
   - LWCF
   #- OMEGA500
   - PBLH
   #- PRECL
   #- PRECT
   #- PRECSL
   #- PRECSC
   #- PRECSC
   #- PRECC
   - PS
   - PSL
   #- QFLX
   - Q
   - RELHUM
   #- SHFLX
   - SST
   - SWCF
   - T
   #- TAUX
   #- TAUY
   #- TGCLDIWP
   #- TGCLDLWP
   #- TMQ
   #- TREFHT
   - TS
   - U
   #- U10
   #- ICEFRAC
   #- OCNFRAC
   #- LANDFRAC

#<Add more variables here.>

# Options for multi-case regional contour plots (./plotting/regional_map_multicase.py)
# region_multicase:
#     region_spec: [slat, nlat, wlon, elon]
#     region_time_option: <calendar | zeroanchor>  # If calendar, will look for specified years. If zeroanchor will use a nyears starting from year_offset from the beginning of timeseries
#     region_start_year:
#     region_end_year:
#     region_nyear:
#     region_year_offset:
#     region_month: <NULL means look for season>
#     region_season: <NULL means use annual mean>
#     region_variables: <list of variables to try to use; allows for a subset of the total diag variables>


#END OF FILE

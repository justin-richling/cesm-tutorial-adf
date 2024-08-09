#!/usr/bin/env python
# coding: utf-8

# # Setting up <strong>your</strong> ADF run - optional
# 
# If you have a case or cases you want to run the ADF with, this section will help with a quick setup. This will include basic information about the configuration yaml files and how to run the ADF for your cases!
# 
# Instead, if you would like a guided demo of how to use the ADF with sample data, please skip to the <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/basic_examples/readme.html">GUIDED EXAMPLES</a> section.
# 

# 

# 0. Make sure your ADF clone is the most up to date version
# 
# * Go to where you installed the ADF, make sure you're on the main branch and run `git pull origin main`
# 
# 1. make a copy of the config_cam_baseline_example.yaml file, feel free to name it something that makes sense to you. The yaml files are in the root folder of where you installed the ADF.
# 
# 2. open that copied file and the main sections you'll want to change are:
# <p>user - use your NCAR username
# <p>diag_basic_info - this is where you'll set some main run variables, the ones I usually change are:
# <p>compare_obs - set true/false depending which run you want
# <p>cam_regrid_loc - where the regridded files for the cases in this ADF run will be saved, you can change or use the default location, just take note
# <p>cam_diag_loc - where the diagnostic plots will be saved, again, you can change or use default
# <p>diag_cam_climo - for the experiment case (test), the ones I change are:
# <p>cam_case_name - just the name of the case run
# <p>cam_hist_loc - where the h# history files live
# <p>case_nickname - anything that would be easier than the case name if you want, it will default to the case name if left blank
# <p>start/end_years - climo years desired
# <p>cam_climo_loc - where you want climo files saved
# <p>cam_ts_loc  - where you want time series files saved
# 
# <p>diag_cam_baseline_climo - same exact variables as the diag_cam_climo above, just set for the control (baseline) case. If using Obs, just ignore this section</p>
# 
# Then at the end of the config file are the plots and variables, set these as you like!
# 
# 3. To run the ADF (from the ADF root path) in a terminal just run: ./run_adf_diag your_new_yaml_file.yaml

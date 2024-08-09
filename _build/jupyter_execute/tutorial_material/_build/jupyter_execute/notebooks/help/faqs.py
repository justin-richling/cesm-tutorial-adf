#!/usr/bin/env python
# coding: utf-8

# # FAQS
# 
# Frequently Asked Qestions
# 
# ### ADF on compute or login nodes?
# 
# It is generally a good idea to run the ADF on compute nodes. If the ADF runs are relatively small, climo years < 20 years and/or non-coupled cases can be run on login nodes, but please be considerate of others on login nodes. It is preferred to run a model vs obs ADF run on compute nodes as some of the ADF features can be quite resource intensive when comparing to observations.
# 
# ### Re-Running the ADF
# 
# What happens if I re-run the ADF after I change something?
# 
# Well that really depends. So common problems are:
# 
# - Plots don't change when they should be
# 
# -> Is the website images staying the same, or are the actual local plots not changing?
# 
# --> if you said only website images, than you need to delete the html files in website dir and re-run. We are working on having it do this automatically in the next version.
# 
# ### ADF freezing/performance issues
# 
# It is well known there are bottle necks in the current version of the ADF. We are aware of this and are taking the next step of the ADF to focus on performance issues
# 
# - Regridded CAM vs Obs seems to freeze/takes forever
# -> this will definitely happen and is suggested to run on a compute node if on NCAR/CISL machines. Depending on the simulation case, it can take several hours, so beware!
# 
# ### Temporal Frequency
# 
# Can the ADF handle different temporal files other than monthly?
# 
# -> Currently the ADF can only compute files for monthly time steps, but we are considering expanding this to others: daily, 3/6-hourly, etc.
# 
# ### ADF with SE or FV CAM output
# 
# The ADF will run without issue on finite volume (FV) output, but in order to run the ADF diagnositcs on spectral element (SE) output, the output data must be flagged to produce gridded data.
# 
# ### MPAS data in the ADF?
# 
# Currently the ADF can analyze MPAS atmosphere data
# 
# ### Can I contribute to the ADF?
# 
# If you have some diagnostics that would fit well in the ADF, please reach out to us and we can help get your script(s) integrated in. In that case, it would be best to <strong>fork</strong> the ADF. If your diagnsotics are better suited as a useful but not something we decide to go into the main branch of the ADF, we have a <a href="https://github.com/NCAR/AMP_toolbox">AMP "toolbox"</a> GitHub repo for scientists to drop scripts/diagnostics to share with others in the community. NOTE: this repo is not consitently monitored, but we will check it occassionally.
# 
# 
# ### Logging Errors
# 
# You can run the ADF with a debug flag tht will output any errors to a log file

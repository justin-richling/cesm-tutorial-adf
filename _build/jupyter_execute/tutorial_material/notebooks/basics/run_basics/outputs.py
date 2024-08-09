#!/usr/bin/env python
# coding: utf-8

# # Exploring <strong>your</strong> ADF outputs

# ### Check the ADF output
# 
# If your ADF run completes there are a couple ways to explore the output plots
# 
# ###### Locally
# 
# If the ADF ran successfully, we can navigate to where we set the diagnostic plots output:
# 
# `````{div} full-width
# 
# &ensp;On a CISL machine, navigate to the root ADF directory
# 
# Example:
# <code class="docutils literal notranslate"><span class="pre">&emsp;/glade/scratch/&#60;user&#62;/ADF/plots/</span></code>
# 
# &ensp;Then go to where you assigned the `cam_diag_plot_loc` location in the run-time config file
# 
# <code class="docutils literal notranslate"><span class="pre" style="color:black">&emsp;<test case>_<start year>_<end year>_vs_<baseline case>_<start year>_<end year>/</span></code>
# 
# `````
# 

# ###### JupyterHub
# 
# apidfjwd

# ###### Website
# 
# If you choose to create HTML files you can publish those to a web server. In the diagnostics plotting location (<code class="docutils literal notranslate"><span class="pre">cam_diag_plot_loc</span></code>) you set in the run-time config file, a `website` directory exists where all the html and css files are saved.
# 
# 
#     .
#     ├── plots
#     │   └── <test case>_<start year>_<end year>_vs_<baseline case>_<start year>_<end year>
#     │       └── website
#     │           ├── assets
#     │           ├── html_img
#     │           ├── html_table
#     │           └── templates
# 
# 
# 

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
# &emsp;    <code class="docutils literal notranslate"><span class="pre" style="color: black;">scp -r website/* tungsten.cgd.ucar.edu:/path/to/your/project/page/</span></code>
# 
# <div class="admonition tip" style="padding-right: 7px">
# <div><h6>A sample website:</h6></div>
# <p><a href="https://webext.cgd.ucar.edu/FLTHIST/f.cam6_3_132.FLTHIST_ne30.001/atm/f.cam6_3_132.FLTHIST_ne30.001_1995_2011_vs_f.cam6_3_119.FLTHIST_ne30.r328_gamma0.33_soae.001_1995_2011/index.html" target="_blank">f.cam6_3_132.FLTHIST_ne30.001 vs f.cam6_3_119.FLTHIST_ne30.r328_gamma0.33_soae.001</a></p>
# </div>
# 
# ---

# ````{tip} If this worked for you and are happy, you can finish up the tutorial here!
# :class: tip
# 
# Feel free to explore more guided and detailed examples to highlight the different ADF setups in the <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/basic_examples/readme.html"><strong>GUIDED EXAMPLES</strong></a> section for step by step setup for provided sample data.
# 
# ````

# 

# 

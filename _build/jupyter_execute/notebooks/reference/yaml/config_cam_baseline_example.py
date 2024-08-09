#!/usr/bin/env python
# coding: utf-8

# # Run Time - config_cam_baseline_example.yaml
# 
# ###### Introduction
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
# <p>This is probably the most important file for the ADF. This stores all the necessary information that the ADF needs to run as well as all the relevant information about the case and baseline/observation/cmip runs.</p>
# 
# Each section of the yaml file represent grouped subsets of information sent to the ADF and each have variable names that get fed into the ADF in a specific fashion. In this yaml file variables can be set and called with the `${}` syntax. 
# 
# IE if we set a `user` variable `user: richling` we can call this by `${user}` and `richling` wil be used where ever it is referenced.
# 
# BIG CAVEAT:<br>
# In this particular yaml file, we have built subsections in which variables set in a subsection are only callable by referencing the subsection first with a "`.`" then variable name.
# 
# <p>IE: Say we want to set the climo years in the test <strong>case</strong> subsection `diag_cam_climo` and call them in the <strong>baseline</strong> subsection `diag_cam_baseline_climo`<br> 
# 
# diag_cam_climo:<br>
# 
# &emsp;&ensp; start_year: 1995  -> we would reference this with diag_cam_climo.start_year<br>
# &emsp;&ensp; end_year: 2000  -> we would reference this with diag_cam_climo.end_year<br>
# 
# Now if we wanted to reference these climo years in the <strong>baseline</strong> subsection:<br>
# 
# diag_cam_baseline_climo:<br>
# 
# &emsp;&ensp; start_year:  &dollar;{diag_cam_climo.start_year}<br>
# &emsp;&ensp; end_year:  &dollar;{diag_cam_climo.end_year}
# </p>
# 
# 
# 
# 
# ::::{Warning}
# <strong>Please do not modify this file!</strong>
#              
# It is recommended to make a copy of this file, make modifications in that copy, and then run that with the ADF.
# 
# :::{admonition} Example
# :class: seealso
# From the ADF root directory
# 
#     cp config_cam_example.yaml config_your_run.yaml
# 
# Then do your editing in `config_your_run.yaml`
# :::
# ::::
# 
# 
# Nested listed variables:
# &ensp;&ensp;Variables <strong>cannot</strong> be used in nested varaibles lists. The multi-case setup is one example of nested listign for variables.<br>
# 
# `````{admonition} ** does not work **
# :class: error
# <p><strong>user:</strong> richling<br>
# <strong>case:</strong> some_run<br>
# <strong>some_path:</strong><br>
# &ensp;&ensp;&ensp;- /glade/u/home/${user}<br>
# &ensp;&ensp;&ensp;- /glade/u/home/${user}/${case}
# </p>
# `````
# 
# ```{admonition} ** works **
# <p><strong>some_path:</strong><br>
# &ensp;&ensp;&ensp;- /glade/u/home/richling<br>
# &ensp;&ensp;&ensp;- /glade/u/home/richling/some_run
# </p>
# ```

# # <u>Subsections</u>
# 
# The subsections that may need to be customized for your run are:
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
## $\color{#117284}{\textit{diag_basic_info}}$## $\color{#117284}{diag_basic_info}$
# ```{warning}
# If variable strings start with a <strong>zero</strong>, the quantity must be in quotes in this yaml file.
# 
# <ul>
#     <li><p>example: desired nick name 026b</p></li>
# </ul>
# <p>case_nickname: "026b" (notice the quotes for a leading zero)</p>
# 
# ```

# ## <strong>diag_basic_info</strong> 
## <a style='color: #117284'><strong>diag_basic_info</strong></a>###### &ensp; <code class="docutils literal notranslate"><span class="pre">compare_obs</span></code>
# 
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">compare_obs</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&ensp; Is this a model vs observations comparison? - <code class="docutils literal notranslate"><span class="pre">true/false</span></code></p>
# <ul>
# <li><p>If <code class="docutils literal notranslate"><span class="pre">false</span></code> or missing, then a model-model comparison is assumed</p></li>
# </ul>
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">obs_data_loc</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&ensp; Location of observational datasets. NOTE: you can override this on a variable by variable basis in the variable defaults file</p>
# <ul>
# <li><p>Note: this only matters if <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/configs/yaml/runtime.html#compare-obs"><code class="docutils literal notranslate"><span class="pre">compare_obs</span></code></a> is <code class="docutils literal notranslate"><span class="pre">true</span></code> and the path isn't specified in the <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/configs/yaml/variable.html" target="_blank">variable defaults file</a>.</p></li>
# <li><p>default: <code class="docutils literal notranslate"><span class="pre">/glade/work/nusbaume/SE_projects/model_diagnostics/ADF_obs</span></code></p></li>
# <li><p>example: <code class="docutils literal notranslate"><span class="pre">/path/to/your/obs/files/</span></code></p></li>
# </ul>
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">cam_regrid_loc</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&ensp; Location where re-gridded and interpolated CAM climatology files are stored</p>
# <p style="margin-top: -5px;">&emsp;&ensp; Required if regridding is desired and </p>
# <ul>
# <li><p>example: <code class="docutils literal notranslate"><span class="pre">/glade/scratch/${user}/ADF/regrid</span></code></p></li>
# </ul>
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">cam_overwrite_regrid</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&ensp; Overwrite CAM re-gridded files? - <code class="docutils literal notranslate"><span class="pre">true/false</span></code></p>
# <ul>
# <li><p>If <code class="docutils literal notranslate"><span class="pre">false</span></code>, or missing, then regridding will be skipped for regridded variables that already exist in <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/configs/yaml/runtime.html#cam-regrid-loc"><code class="docutils literal notranslate"><span class="pre">cam_regrid_loc</span></code></a></p></li>
# </ul>
# 
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">cam_diag_plot_loc</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&ensp; Location where diagnostic plots are stored<br>The ADF will create a directory for the plots in this directory in the form of {cam_case_name}_{YYYY}_{YYYY}_vs_{baseline_name}_{YYYY}_{YYYY}
# </p>
# <ul>
# <li><p>example: <code class="docutils literal notranslate"><span class="pre">/glade/scratch/${user}/ADF/plots</span></code></p></li>
# </ul>
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">hist_num</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&ensp; CAM history file number to use (h0, h1, h2, etc)</p>
# <ul>
# <li><p>Currently only affects timeseries generation, as everything else uses the timeseries files themselves.</p></li>
# <li><p>If this variable is not present then it will default to "cam.h0"</p></li>
# <li><p>example: cam.h4</p></li>
# </ul>
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">defaults_file</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&ensp; Location of ADF variable plotting defaults YAML file if not using ADF default file: <code class="docutils literal notranslate"><span class="pre"> lib/adf_variable_defaults.yaml</span></code></p>
# <ul>
# <li><p>example: <code class="docutils literal notranslate"><span class="pre">/path/to/custom/defaults/file/my_variable_defaults.yaml</span></code></p>
# </li>
# </ul>
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">plot_press_levels</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&ensp; Vertical pressure levels (in hPa) on which to plot 3-D variables when using horizontal (e.g. lat/lon) map projections
# 
# <ul>
# <li><p>If this config option is missing, then no 3-D variables will be plotted on horizontal maps.  Please note too that pressure levels must currently match what is available in the observations file in order to be plotted in a model vs obs run:</p></li>
# <li><p>example: [200,850]</p></li>
# </ul>
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">central_longitude</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&ensp; Longitude line on which to center all lat/lon maps</p>
# <ul>
# <li><p>If missing, then the central longitude will default to 180 degrees E.</p></li>
# <li><p>example: 0</p></li>
# </ul>
# 
#     
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">num_procs</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&ensp; Number of processors on which to run the ADF</p>
# 
# <ul>
# <li><p>If this config variable isn't present then the ADF defaults to one processor.</p></li>
# <li><p>If you set it to <code class="docutils literal notranslate"><span class="pre"> * </span></code> then it will default to all of the processors available on a single node/machine</p></li>
# <li><p>default: 8</p></li>
# </ul>
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">redo_plot</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&ensp; Remake plots? - <code class="docutils literal notranslate"><span class="pre">true/false</span></code></p>
# 
# <ul>
# <li><p>If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, redo all plots even if they already exist</p></li>
# <li><p>If set to <code class="docutils literal notranslate"><span class="pre">false</span></code>, a plot will be skipped if found</p></li>
# <li><p>default: false</p></li>
# </ul>
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">create_html</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&ensp; Generate HTML website - <code class="docutils literal notranslate"><span class="pre">true/false</span></code></p>
# 
# <ul>
#     <li><p>If <code class="docutils literal notranslate"><span class="pre">false</span></code> or missing, no html pages will be made</p></li>
# <li><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code> The website files themselves will be located in the path specified by <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/configs/yaml/runtime.html#cam-diag-plot-loc"><code class="docutils literal notranslate"><span class="pre">cam_diag_plot_loc</span></code></a>, under the <code class="docutils literal notranslate"><span class="pre">{diag_run}/website</span></code> subdirectory, where <code class="docutils literal notranslate"><span class="pre">{diag_run}</span></code> is the subdirectory created for this particular diagnostics run (usually <code class="docutils literal notranslate"><span class="pre">{case}_YYYY_YYYY_vs_obs</span></code> or <code class="docutils literal notranslate"><span class="pre">{case}_YYYY_YYYY_vs_{baseline}_YYYY_YYYY</span></code>)</p>
#     </li>
#     
# </ul>

# ---
## $\color{#117284}{\textit{diag_cam_climo}}$
# ## <strong>diag_cam_climo</strong> 

# <script>
#     p2 {margin-top: -10px;}
# </script>
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">calc_cam_climo</span></code>
# 
# <p2>&emsp;&ensp;  Calculate climatology files? - <code class="docutils literal notranslate"><span class="pre">true/false</span></code></p2>
# 
# <ul>
# <li><p>If <code class="docutils literal notranslate"><span class="pre">false</span></code>, the climatology files will not be created</p></li>
# <li><p>default: true</p></li>
# </ul>
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">cam_overwrite_climo</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&ensp; Overwrite CAM climatology files? - <code class="docutils literal notranslate"><span class="pre">true/false</span></code></p>
# <ul>
# <li><p>If <code class="docutils literal notranslate"><span class="pre">false</span></code>, or not present, then already existing climatology files will be skipped</p></li>
# <li><p>default: false</p></li>
# </ul>
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">cam_case_name</span><a style="color: red; font-size: 10"><strong> - ** Required **</strong></a></code>
# 
# <p style="margin-top: -5px; color: red">&emsp;&ensp; <strong>** Required **</strong></p>
# <p style="margin-top: -5px;">&emsp;&ensp; Name of CAM run</p>
# <ul>
# <li><p>example: b.e20.BHIST.f09_g17.20thC.297_05</p></li>
# </ul>
#     
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">case_nickname</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&ensp; Case nickname to be used for plotting purposes as well as any custom place in the diagnsotics output if desired</p>
# 
# <ul>
#     <li><p>If left blank, it will default to cam_case_name</p></li>
#     <li><p>example: cool_nickname</p></li>
# </ul>
# 
# 
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">cam_hist_loc</span></code>
# 
# <p style="margin-top: -5px; color: red">&emsp;&ensp; <strong>** Required **</strong></p>
# <p style="margin-top: -5px;">&emsp;&ensp; Location of CAM history (h0) files</p>
# <ul>
# <li><p>&ensp; example: <code class="docutils literal notranslate"><span class="pre">/glade/p/cesm/ADF/${diag_cam_climo.cam_case_name}</span></code></p></li>
# </ul>
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">cam_climo_loc</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&ensp; Location of CAM climatologies (to be created and then used by this script)</p>
# <ul>
# <li><p>&ensp; example: <code class="docutils literal notranslate"><span class="pre">/glade/scratch/${user}/ADF/${diag_cam_climo.cam_case_name}/climo</span></code></p></li>
# </ul>
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">start_year</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&ensp; Model year when time series files should start</p>
# <ul>
# <li><p>Note:  Leaving this entry blank will make time series start at earliest available year</p></li>
# <li><p>example: 1990</p></li>
# <li><p>example: 10</p></li>
# <li><p>example: 0010??</p></li>
# </ul>
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">end_year</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&ensp; Model year when time series files should end</p>
# <ul>
# <li><p>Note:  Leaving this entry blank will make time series end at latest available year</p></li>
# <li><p>example: 1999</p></li>
# <li><p>example: 15</p></li>
# </ul>
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">cam_ts_done</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&ensp; Do time series files need to be generated? - <code class="docutils literal notranslate"><span class="pre">true/false</span></code></p>
# <ul>
# <li><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, then diagnostics assumes that model files are already time series</p></li>
# <li><p>If <code class="docutils literal notranslate"><span class="pre">false</span></code>, or if simply not present, then diagnostics will attempt to create time series files from history (time-slice) files</p></li>
# <li><p>default: false</p></li>
# </ul>
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">cam_ts_save</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&ensp; Save interim time series files? - <code class="docutils literal notranslate"><span class="pre">true/false</span></code></p>
# 
# 
# <ul class="adom">
# <div class="admonition warning">
# <p class="admonition-title">Warning</p>
# <p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, this can take up a significant amount of space</p>
# </div>
# </ul>
# 
# <ul>
#     <li><p>default: true</p></li>
# </ul>
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">cam_overwrite_ts</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&ensp; Overwrite time series files, if found? - <code class="docutils literal notranslate"><span class="pre">true/false</span></code></p>
# <ul>
# <li><p>If set to <code class="docutils literal notranslate"><span class="pre">false</span></code>, then time series creation will be skipped if files are found</p></li>
# <li><p>default: false</p></li>
# </ul>
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">cam_ts_loc</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&ensp; Location where time series files are (or will be) stored</p>
# <ul>
# <li><p>example: <code class="docutils literal notranslate"><span class="pre">/glade/scratch/${user}/ADF/${diag_cam_climo.cam_case_name}/ts</span></code></p></li>
# </ul>
# 
# <ul class="adom">
# 
# <div class="admonition warning">
# <p class="admonition-title">Warning</p>
# <p>If this is a CMIP-like case, this should be set to the same location as <code class="docutils literal notranslate"><span class="pre">cam_hist_loc</span></code></p>
# </div>
# 
# </ul>
## $\color{#117284}{\textit{diag_cam_baseline_climo}}$
# ## <strong>diag_cam_baseline_climo</strong> 
# 
# ```{note}
# These are the same variable names as [diag_cam_climo](https://justin-richling.github.io/ADF-Tutorial/notebooks/configs/yaml/runtime.html#color-117284-textit-diag-cam-climo) above, but for the baseline case
# 
# They are not necessary if comapring against observations, and will be skipped
# ```

# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">calc_cam_climo</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&ensp; Calculate climatology files? - <code class="docutils literal notranslate"><span class="pre">true/false</span></code></p>
# <ul>
#     <li><p>If <code class="docutils literal notranslate"><span class="pre">false</span></code>, the climatology files will not be created</p></li>
#     <li><p>default: true</p></li>
# </ul>
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">cam_overwrite_climo</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&ensp; Overwrite CAM climatology files? - <code class="docutils literal notranslate"><span class="pre">true/false</span></code></p>
# <ul>
#     <li><p>If <code class="docutils literal notranslate"><span class="pre">false</span></code>, or not present, then already existing climatology files will be skipped</p></li>
#     <li><p>default: false</p></li>
# </ul>
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">cam_case_name</span></code>
# 
# <p style="margin-top: -5px; color: red">&emsp;&ensp; <strong>** Required **</strong></p>
# <p style="margin-top: -5px;">&emsp;&ensp; Name of baseline case (or CAM/other run name)</p>
# <ul>
#     <li><p>example: b.e20.BHIST.f09_g16.20thC.125.02</p></li>
# </ul>
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">case_nickname</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&emsp;&ensp; Baseline nickname to be used for plotting purposes as well as any custom place in the diagnsotics output if desired</p>
# 
# <ul>
#     <li><p>If left blank, it will default to cam_case_name</p></li>
#     <li><p>example: cool_nickname</p></li>
# </ul>
# 
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">cam_hist_loc</span></code>
# 
# <p style="margin-top: -5px; color: red">&emsp;&ensp; <strong>** Required **</strong></p>
# <p style="margin-top: -5px;">&emsp;&ensp; Location of baseline history (h0) files</p>
# <ul>
#     <li><p>&ensp; example: <code class="docutils literal notranslate"><span class="pre">/glade/p/cesm/ADF/${diag_cam_baseline_climo.cam_case_name}</span></code></p></li>
# </ul>
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">cam_climo_loc</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&ensp; Location of baseline climatologies (to be created and then used by this script)</p>
# <ul>
#     <li><p>&ensp; example: <code class="docutils literal notranslate"><span class="pre">/glade/scratch/${user}/ADF/${diag_cam_baseline_climo.cam_case_name}/climo</span></code></p></li>
# </ul>
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">start_year</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&ensp; Baseline year when time series files should start</p>
# <ul>
#     <li><p>Note:  Leaving this entry blank will make time series start at earliest available year</p></li>
#     <li><p>example: 1990</p></li>
#     <li><p>example: 10</p></li>
#     <li><p>example: 0010??</p></li>
# </ul>
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">end_year</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&ensp; Baseline year when time series files should end</p>
# <ul>
#     <li><p>Note:  Leaving this entry blank will make time series end at latest available year</p></li>
#     <li><p>example: 1999</p></li>
#     <li><p>example: 15</p></li>
# </ul>
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">cam_ts_done</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&ensp; Do time series files need to be generated? - <code class="docutils literal notranslate"><span class="pre">true/false</span></code></p>
# <ul>
#     <li><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, then diagnostics assumes that baseline files are already time series</p></li>
#     <li><p>If <code class="docutils literal notranslate"><span class="pre">false</span></code>, or if simply not present, then diagnostics will attempt to create time series files from history (time-slice) files</p></li>
#     <li><p>default: false</p></li>
# </ul>
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">cam_ts_save</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&ensp; Save interim time series files? - <code class="docutils literal notranslate"><span class="pre">true/false</span></code></p>
# 
# <ul class="adom">
# <div class="admonition warning">
# <p class="admonition-title">Warning</p>
# <p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, this can take up a significant amount of space</p>
# </div>
# </ul>
# 
# <ul>
#     <li><p>default: true</p></li>
# </ul>
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">cam_overwrite_ts</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&ensp; Overwrite time series files, if found? - <code class="docutils literal notranslate"><span class="pre">true/false</span></code></p>
# <ul>
#     <li><p>If set to <code class="docutils literal notranslate"><span class="pre">false</span></code>, then time series creation will be skipped if files are found</p></li>
#     <li><p>default: false</p></li>
# </ul>
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">cam_ts_loc</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&ensp; Location where time series files are (or will be) stored</p>
# <ul>
#     <li><p>example: <code class="docutils literal notranslate"><span class="pre">/glade/scratch/${user}/ADF/${diag_cam_baseline_climo.cam_case_name}/ts</span></code></p></li>
# </ul>
# 
# <ul class="adom">
# <div class="admonition warning">
# <p class="admonition-title">Warning</p>
# <p>If this is a CMIP-like case, this should be set to the same location as <code class="docutils literal notranslate"><span class="pre">cam_hist_loc</span></code><p>
# </div>
# </ul>
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ---
## $\color{#117284}{\textit{diag_cvdp_info}}$
# ## <strong>diag_cvdp_info</strong> 
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">cvdp_run</span></code>
# 
# 
# <p style="margin-top: -5px;">&emsp;&ensp; Run the CVDP in the background? - <code class="docutils literal notranslate"><span class="pre">true/false</span></code></p>
# <ul>
#     <li><p>default: <code class="docutils literal notranslate"><span class="pre">false</span></code></p></li>
# </ul>
# 
# 
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">cvdp_codebase_loc</span></code>
# <p style="margin-top: -5px;">&emsp;&ensp; Set location of CVDP codebase</p>
# <ul>
#     <li><p>CGD systems path = /home/asphilli/CESM-diagnostics/CVDP/Release/v5.2.0/</p></li>
#     <li><p>CISL systems path = /glade/u/home/asphilli/CESM-diagnostics/CVDP/Release/v5.2.0/</p></li>
#     <li><p>github location = https://github.com/NCAR/CVDP-ncl</p></li>
#     <li><p>default: <code class="docutils literal notranslate"><span class="pre">/glade/u/home/asphilli/CESM-diagnostics/CVDP/Release/v5.2.0/</span></code></p></li>
# </ul>
# 
# 
# 
# ###### &ensp; <code class="docutils literal notranslate"><span class="pre">cvdp_loc</span></code>
# 
# <p style="margin-top: -5px;">&emsp;&ensp; Location where the CVDP files will be stored</p>
# <ul>
#     <li><p>example: <code class="docutils literal notranslate"><span class="pre">/glade/scratch/${user}/cvdp/</span></code></p></li>
# </ul>

# ## Diagnostic Scripts "Subsections"
# 
# <p>Each of the following sets are also considered subsections. These are all components of the actual diagnostics workflow of the ADF.</p>
## $\color{#117284}{\textit{time_averaging_scripts}}$

# ### <strong>time_averaging_scripts</strong> 

# This section allows for any time averaging scripts
# 
# * Must be located in scripts/averaging within the ADF root directory:
# 
#       scripts/averaging/create_climo_files.py
#       scripts/averaging/create_TEM_files.py
#       
# * In this yaml file they would be listed as:
# 
# time_averaging_scripts:<br>
# &emsp; - create_climo_files<br>
# &emsp; - create_TEM_files
## $\color{#117284}{\textit{regridding_scripts}}$

# ### <strong>regridding_scripts</strong> 

# This section allows for any regridding scripts
# 
# * Must be located in scripts/regridding!
# 
#       - scripts/regridding/regrid_and_vert_interp.py
# 
# In this yaml file they would be listed as:
# 
# regridding_scripts:<br>
# &emsp; - create_climo_files<br>
# 
## $\color{#117284}{\textit{analysis_scripts}}$

# ### <strong>analysis_scripts</strong> 

# This section allows for a broad spectra of data analysis scripts
# 
# * Must be located in scripts/analysis!
#     
#       - scripts/analysis/amwg_table.py
#       
#       Possible addition examples:
#       - scripts/analysis/amwg_chem_table.py
#       - scripts/analysis/amwg_aerosol_table.py
# 
# In this yaml file they would be listed as:
# 
# analysis_scripts:<br>
# &emsp; - amwg_table<br>
# Possible addition examples:<br>
# &emsp; - amwg_chem_table<br>
# &emsp; - amwg_aerosol_table
## $\color{#117284}{\textit{plotting_scripts}}$

# ### <strong>plotting_scripts</strong> 

# Set of plotting scripts, both ADF default as well as any custom scripts
# 
# * Must be located in scripts/plotting!
# 
#      - scripts/plotting/cam_taylor_diagram.py
#      - scripts/plotting/global_latlon_map.py
#      - scripts/plotting/…
# 
#      Possible addition examples:
#      - scripts/plotting/time_series.py
# 
# 
# In this yaml file they would be listed as:
# 
# plotting_scripts:<br>
# &emsp; - global_latlon_map<br>
# &emsp; - zonal_mean<br>
# &emsp; - meridional_mean<br>
# &emsp; - polar_map<br>
# &emsp; - global_latlon_vect_map<br>
# &emsp; - cam_taylor_diagram<br>
# &emsp; - qbo<br>
# &emsp; - tem -> requires more setup info with <code class="docutils literal notranslate"><span class="pre"><a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/intro/yaml/config_cam_baseline_example.html#strong-tem-info-strong">tem_info</a></span></code><br>
# &emsp; - regional_map_multicase -> requires more setup info with <code class="docutils literal notranslate"><span class="pre"><a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/intro/yaml/config_cam_baseline_example.html#strong-region-multicase-strong">region_multicase</a></span></code>
## $\color{#117284}{\textit{diag_var_list}}$

# ### <strong>diag_var_list</strong> 

# List of variables to be executed in the ADF
# 
# These usually are the CAM variables, but nocesessarily the only ones, ie RESTOM can be added to this list and the ADF will attempt to calculate based off constituents. 
# 
# If the ADF searches for time series/climo/regridded/tem, etc. files for a given variable from this list and does not find one in the data files, it will skip that variable with an explaination in most cases. The ADF will not crash, but continue on to the next variable in the list.
# 
## $\color{#117284}{\textit{region_multicase}}$

# ### <strong>tem_info</strong> 
# 
# <p>Options for TEM diagnostics (./averaging/create_TEM_files.py and ./plotting/temp.py)<br>
# tem_info:<br>
# &emsp; #Location where TEM files are stored:<br>
# &emsp; #If path not specified or commented out, skip TEM calculation<br>
# &emsp; tem_loc: /glade/scratch/richling/adf-output/ADF-data/TEM/TEST/<br>
# &emsp; #TEM history file number<br>
# &emsp; hist_num: h4<br>
#     
# &emsp; #Overwrite TEM files, if found?<br>
# &emsp; overwrite_tem_case: false<br>
# 
# &emsp; #For multiple test cases<br>
# &emsp; #overwrite_tem_case<br>
# &emsp; #    - false<br>
# &emsp; #    - true<br>
# 
# &emsp; overwrite_tem_base: false

# ### <strong>region_multicase</strong> 

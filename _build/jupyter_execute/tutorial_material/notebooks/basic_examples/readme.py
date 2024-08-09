#!/usr/bin/env python
# coding: utf-8

# # ADF Demo Setup
# 
# This section is meant to allow users to run the ADF if you want to have an ADF run that produces all the outputs.
# 
# * Variables needed for plots like the QBO or TEM diagnsotcis may not be in your actual run, so this will allow you to see some of the full output the ADF is capable of!
# 
# Now we will walk through two common ADF setups:
# 
# <ul>
# <li><a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/basic_examples/model_model_run.html">CAM simulation vs CAM simulation</a></li>
# <li><a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/basic_examples/model_obs_run.html">CAM simulation vs Observations/Reanalysis</a></li>
# </ul>
# 
# ```{admonition} Note
# :class: attention
# Some of the setups will look almost identical, but pay attention to the small differences!
# ```
# 
# Additionally, here are some common customizations we can do with the ADF:
# 
# <ul>    
# <li><a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/exercises/custom_defaults.html">Customizing variable defaults settings</a></li>
# <li><a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/exercises/custom_observations.html">Using custom set of Observations</a></li>
# <li><a href="">Adding custom script to your ADF</a></li>
# <li><a href="">Running the ADF in Jupyter</a></li>
# </ul>
# 
# 
# These will be quick demos and are meant to show different simple setups for running the ADF.
# 
# 
# 
# 
# 
# 
<li><a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/basic_examples/model_cmip_run.html">CAM simulation vs Model Intercomparisons</a> (CMIP, AMIP)</li>#### Ground Rules

Let's go over some helpful tips/hints for some of the ADF parts.

<strong>YAML file:</strong> As mentioned in the intro section, the ADF utilizes two YAML files for it's configuration. If you aren't familiar with YAML files, please check the reference section of this tutorial.Recall <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/basics/adf.html#adf-setup" target="_blank">the steps</a> we will take are to:

<p>&emsp; <s>0. Run CAM simulation to get history ( h0* ) file(s) 
           *or other history files</s></p>
                                   
<p>&emsp; 1. Configure yaml file(s) for the history files<br>

&emsp; &emsp; <code class="docutils literal notranslate"><span class="pre">config_cam_baseline_example.yaml</span></code>  (necessary, must copy and change!)<br>
&emsp; &emsp; &ensp;  Please refer back to the <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/intro/yaml/config_cam_baseline_example.html" target="_blank">run-time</a> section for any hints or descriptions of variables.<br>

&emsp; &emsp; <s><code class="docutils literal notranslate"><span class="pre">lib/adf_variable_defaults.yaml</span></code>   (necessary, but optional to copy and change)</s><br>
&emsp; &emsp; &ensp;  For this example we <strong>will not</strong> be editing the variable defaults yaml file<br>
</p>

<p>&emsp; 2. Run the ADF!</p>
# In[ ]:





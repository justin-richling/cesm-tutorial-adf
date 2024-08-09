#!/usr/bin/env python
# coding: utf-8

# # Running <strong>your</strong> ADF
# 
# If you have a set of cases you want to run the ADF with, this section will help with a quick setup.
# 
# Instead, if you would like a guided demo of how to use the ADF with sample data or if your case is not as straight forward, please browse the <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/basic_examples/readme.html">GUIDED EXAMPLES</a> section.
# 

# After the config yaml file set up, running the ADF is fairly straight forward with two options:
# 
# 1) ADF via terminal
# 2) ADF via Jupyter

# In[ ]:





# In[ ]:





# ##### ADF via Terminal
# 
# `````{div} full-width
# If simplicity is your game, running the ADF in the terminal is the quickest and most straight forward way. All that is needed is to be in the path where you installed the ADF. There is an executable script called `run_adf_diag`. 
# 
# Simply run this command with the run-time config yaml file we set in the previous page:
# 
# <code class="docutils literal notranslate"><span class="pre">&emsp;./run_adf_diag your_conifg_file.yaml</span></code>
# 
# That's it!
# `````

# In[ ]:





# ##### ADF via Jupyter
# 
# `````{div} full-width
# Running the ADF via Jupyter has a few more steps than through the terminal, but it has several advantages over running it via terminal.
# 
# Most importantly, it is much more flexible inside a Jupyter notebook; a couple of examples:
# 
# - the user can pull out specific pieces of the ADF like only time series creation, etc.
# 
# - the user can also piggy back custom diagnostics in the same notebook as the ADF run.
# 
# 
# This last point is powerful because once the ADF has run in the notebook, the user has access to all the ojects that come out of the ADF, such as file locations, case names, climo years, etc.
# `````
# 
# ---

# ##### Outputs
# 
# Once the ADF finishes regardless of how it was run, you can now explore the outputs. Please skip to the <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/basics/run_basics/outputs.html">Exploring <strong>your</strong> ADF outputs</a> section!

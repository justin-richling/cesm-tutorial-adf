#!/usr/bin/env python
# coding: utf-8

# # ADF in Jupyter
# 
# Now that we have seen how to run the ADF via terminal, let's take a look at how to run the ADF through Jupyter.
# 
# ### Why Jupyter?
# 
# If you are looking to use the ADF in a more developmental or interactive way, using Jupyter will offer a lot more flexibility than running through the terminal.
# 
# One major advantage of this way of running the ADF will allow the user to immediately have access to output data in a Jupyter notebook which can allow for further development or use of diagnostics that aren't in the ADF by defualt.
# 
# One scenario to highlight this flexibility could be for tuning specific parameters of your model run that need a specific diagnostics set of tools that maybe only good for this tune. Now the user can build custom diagnostics code within the same Jupyter notebook that the ADF was run in!
# 
# If you need help with navigating Jupyter Nobeooks or NCAR's JupyterHub, please see the <a>reference section</a> of this tutorial.

# ### Step 1: Run ADF
# 
# This will simulate running the ADF in the terminal, so nothing will be different here. In order to run the ADF, any of the NPL conda environments will suffice in Jupyter. NCAR has a couple to choose from (as of this tutorial):
# 
#     NPL 2023a
#     NPL 2023b

# If you are not up tp date or familiar with JupyterHub/Jupyter Notebooks, to change the kernel (environment) from the default Python3 (or None) to a different kerenel, at the top right of the notebook is an option to switch kernels:
# 
# ![kernel location](kernel_location.png)
# 
# Click on the kernel and it will bring up a dropdown box with available kernels:
# 
# ![kernel dropdown](kernel_dropdown.png)
# 
# Find one of the NPL environments and select that:
# 
# <strong>NOTE:</strong> your available kernels may not be same as the ones displayed here.
# 
# ![kernel options](kernel_options.png)
<html>
   <body>
      <h3> Using the <em> download attribute of a tag </em> to create file download button using JavaScript. </h3>
      <p> Click the below button to download this Jupyter Notebook</p>
      <a href = "notebooks/basic_examples/run/jupyter.ipynb"
      Download = "test_image">
         <button type = "button"> Download </button>
      </a>
      <br>
   </body>
</html>
# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')

import os.path
from pathlib import Path
import sys


# In[4]:


# Determine ADF directory path
# If it is in your cwd, set adf_path = local_path, 
# otherwise set adf_path appropriately

local_path = os.path.abspath('')


# In[5]:


#adf_path = "/glade/work/{user}/ADF" # <-- uncomment and use your username
adf_path = "/glade/work/richling/ADF/ADF/" # <-- then comment out

print(f"current working directory = {local_path}")
print(f"ADF path                  = {adf_path}")


# In[6]:


#set path to ADF lib
lib_path = os.path.join(adf_path,"lib")
print(f"The lib scripts live here, right? {lib_path}")

#set path to ADF plotting scripts directory
plotting_scripts_path = os.path.join(adf_path,"scripts","plotting")
print(f"The plotting scripts live here, right? {plotting_scripts_path}")

#Add paths to python path:
sys.path.append(lib_path)
sys.path.append(plotting_scripts_path)


# In[7]:


#import ADF diagnostics object
from adf_diag import AdfDiag

# If this fails, check your paths output in the cells above,
# and that you are running the NPL (conda) Kernel
# You can see all the paths being examined by un-commenting the following:
#sys.path


# ##### Load the run-time config file into the ADF module
# 
# This will create the ADF python object

# In[8]:


# Set path for config YAML file
#config_path = "/path/to/your/yaml/file/"
config_path = "/glade/work/richling/ADF/adf-demo/config_files/"

# Set name of config YAML file:
config_fil_str = "config_single_model_vs_model.yaml"

# Make full path to config file
config_file=os.path.join(config_path,config_fil_str)


# In[9]:


#Initialize ADF object with config file
adf = AdfDiag(config_file)
adf


# The following functions are what get called under the hood when the ADF is run through the terminal

# ##### Create Time Series Files
# 
# Create model time series

# In[ ]:


get_ipython().run_cell_magic('time', '', 'adf.create_time_series()\n')


# Output:

#       Generating CAM time series files...
#          Processing time series for case 'f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001' :
#          - time series for CLDHGH
#          - time series for CLDICE
#     Adding PS to file
#          - time series for CLDLIQ
#     Adding PS to file
#          - time series for CLDLOW
#          - time series for CLDMED
#          - time series for CLDTOT
#          - time series for CLOUD
#     Adding PS to file
#          - time series for FLNS
#          - time series for FLNT
#          - time series for FLNTC
#          - time series for FSNS
#          - time series for FSNT
#          - time series for FSNTC
#          - time series for LHFLX
#          - time series for LWCF
#          - time series for OMEGA500
#          - time series for PBLH
#          - time series for PRECL
#          - time series for PRECT
#          - time series for PRECSL
#          - time series for PRECSC
#          - time series for PRECSC
#          - time series for PRECC
#          - time series for PS
#          - time series for PSL
#          - time series for QFLX
#          - time series for Q
#     Adding PS to file
#          - time series for RELHUM
#     Adding PS to file
#          - time series for SHFLX
#          - time series for SST
#          - time series for SWCF
#          - time series for T
#     Adding PS to file
#          - time series for TAUX
#          - time series for TAUY
#          - time series for TGCLDIWP
#          - time series for TGCLDLWP
#          - time series for TMQ
#          - time series for TREFHT
#          - time series for TS
#          - time series for U
#     Adding PS to file
#          - time series for U10
#          - time series for ICEFRAC
#          - time series for OCNFRAC
#          - time series for LANDFRAC
#       ...CAM time series file generation has finished successfully.
#     CPU times: user 256 ms, sys: 40.5 ms, total: 297 ms
#     Wall time: 1min 5s

# In[ ]:


get_ipython().run_cell_magic('time', '', '#Create model baseline time series (if needed):\n\n# Since we are doing model vs model\nif not adf.compare_obs:\n    adf.create_time_series(baseline=True)\n')


# Output:

#       Generating CAM time series files...
#          Processing time series for case 'f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001' :
#          - time series for CLDHGH
#          - time series for CLDICE
#     Adding PS to file
#          - time series for CLDLIQ
#     Adding PS to file
#          - time series for CLDLOW
#          - time series for CLDMED
#          - time series for CLDTOT
#          - time series for CLOUD
#     Adding PS to file
#          - time series for FLNS
#          - time series for FLNT
#          - time series for FLNTC
#          - time series for FSNS
#          - time series for FSNT
#          - time series for FSNTC
#          - time series for LHFLX
#          - time series for LWCF
#          - time series for OMEGA500
#          - time series for PBLH
#          - time series for PRECL
#          - time series for PRECT
#          - time series for PRECSL
#          - time series for PRECSC
#          - time series for PRECSC
#          - time series for PRECC
#          - time series for PS
#          - time series for PSL
#          - time series for QFLX
#          - time series for Q
#     Adding PS to file
#          - time series for RELHUM
#     Adding PS to file
#          - time series for SHFLX
#          - time series for SST
#          - time series for SWCF
#          - time series for T
#     Adding PS to file
#          - time series for TAUX
#          - time series for TAUY
#          - time series for TGCLDIWP
#          - time series for TGCLDLWP
#          - time series for TMQ
#          - time series for TREFHT
#          - time series for TS
#          - time series for U
#     Adding PS to file
#          - time series for U10
#          - time series for ICEFRAC
#          - time series for OCNFRAC
#          - time series for LANDFRAC
#       ...CAM time series file generation has finished successfully.
#     CPU times: user 180 ms, sys: 141 ms, total: 321 ms
#     Wall time: 1min 6s

# ##### Create Climo Files
# 
# This will run the creation of both test and baseline cases

# In[ ]:


get_ipython().run_cell_magic('time', '', '#Create model climatology (climo) files.\nadf.create_climo()\n')


# Output:

#       Calculating CAM climatologies...
#          Calculating climatologies for case 'f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001' :
#             /glade/scratch/richling/ADF/adf_tutorial/data/climo/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001 not found, making new directory
#          Calculating climatologies for case 'f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001' :
#             /glade/scratch/richling/ADF/adf_tutorial/data/climo/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001 not found, making new directory
#       ...CAM climatologies have been calculated successfully.
#     CPU times: user 226 ms, sys: 307 ms, total: 533 ms
#     Wall time: 5min 13s

# ##### Regrdding Climo Files
# 
# Regrid model climatology files to match either observations or CAM baseline climatologies.
# 
# This call uses the `regridding_scripts` specified in the run-time config file

# In[ ]:





# In[ ]:





# In[ ]:


get_ipython().run_cell_magic('time', '', 'adf.regrid_climo()\n')


# Output:

#       Regridding CAM climatologies...
#         /glade/scratch/richling/ADF/adf_tutorial/data/regrid not found, making new directory
#          Regridding case 'f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001' :
#          - regridding PS (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding LANDFRAC (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding OCNFRAC (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding CLDHGH (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding CLDICE (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#     Please ignore the interpolation warnings that follow!
#     Interpolation point out of data bounds encountered
#     Please ignore the interpolation warnings that follow!
#     Interpolation point out of data bounds encountered
#          - regridding CLDLIQ (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#     Please ignore the interpolation warnings that follow!
#     Interpolation point out of data bounds encountered
#     Please ignore the interpolation warnings that follow!
#     Interpolation point out of data bounds encountered
#          - regridding CLDLOW (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding CLDMED (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding CLDTOT (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding CLOUD (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#     Please ignore the interpolation warnings that follow!
#     Interpolation point out of data bounds encountered
#     Please ignore the interpolation warnings that follow!
#     Interpolation point out of data bounds encountered
#          - regridding FLNS (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding FLNT (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding FLNTC (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding FSNS (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding FSNT (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding FSNTC (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding LHFLX (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding LWCF (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding OMEGA500 (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding PBLH (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding PRECL (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding PRECT (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding PRECSL (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding PRECSC (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding PRECSC (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          Regridded file already exists, so skipping...
#          - regridding PRECC (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding PSL (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding QFLX (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding Q (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#     Please ignore the interpolation warnings that follow!
#     Interpolation point out of data bounds encountered
#     Please ignore the interpolation warnings that follow!
#     Interpolation point out of data bounds encountered
#          - regridding RELHUM (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#     Please ignore the interpolation warnings that follow!
#     Interpolation point out of data bounds encountered
#     Please ignore the interpolation warnings that follow!
#     Interpolation point out of data bounds encountered
#          - regridding SHFLX (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding SST (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding SWCF (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding T (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#     Please ignore the interpolation warnings that follow!
#     Interpolation point out of data bounds encountered
#     Please ignore the interpolation warnings that follow!
#     Interpolation point out of data bounds encountered
#          - regridding TAUX (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding TAUY (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding TGCLDIWP (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding TGCLDLWP (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding TMQ (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding TREFHT (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding TS (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding U (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#     Please ignore the interpolation warnings that follow!
#     Interpolation point out of data bounds encountered
#     Please ignore the interpolation warnings that follow!
#     Interpolation point out of data bounds encountered
#          - regridding U10 (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#          - regridding ICEFRAC (known targets: ['f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001'])
#       ...CAM climatologies have been regridded successfully.
#     CPU times: user 1min 42s, sys: 9.85 s, total: 1min 52s
#     Wall time: 2min 11s

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ##### Run Analysis Scripts
# 
# Perform analyses on the simulation(s).
# This call uses the `analysis_scripts` specified in the run-time config file

# In[ ]:


adf.perform_analyses()


# Output:

#       Calculating AMWG variable table...
#             /glade/scratch/richling/ADF/adf_tutorial/plots/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001_1995_2000_vs_f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001_1995_2000 not found, making new directory
#          - Variable 'LANDFRAC' being added to table
#          - Variable 'OCNFRAC' being added to table
#          - Variable 'CLDHGH' being added to table
#          - Variable 'CLDICE' being added to table
#            Variable 'CLDICE' has a vertical dimension, which is currently not supported for the AMWG Table. Skipping...
#          - Variable 'CLDLIQ' being added to table
#            Variable 'CLDLIQ' has a vertical dimension, which is currently not supported for the AMWG Table. Skipping...
#          - Variable 'CLDLOW' being added to table
#          - Variable 'CLDMED' being added to table
#          - Variable 'CLDTOT' being added to table
#          - Variable 'CLOUD' being added to table
#            Variable 'CLOUD' has a vertical dimension, which is currently not supported for the AMWG Table. Skipping...
#          - Variable 'FLNS' being added to table
#          - Variable 'FLNT' being added to table
#          - Variable 'FLNTC' being added to table
#          - Variable 'FSNS' being added to table
#          - Variable 'FSNT' being added to table
#          - Variable 'FSNTC' being added to table
#          - Variable 'LHFLX' being added to table
#          - Variable 'LWCF' being added to table
#          - Variable 'OMEGA500' being added to table
#          - Variable 'PBLH' being added to table
#          - Variable 'PRECL' being added to table
#          - Variable 'PRECT' being added to table
#          - Variable 'PRECSL' being added to table
#          - Variable 'PRECSC' being added to table
#          - Variable 'PRECSC' being added to table
#          - Variable 'PRECC' being added to table
#          - Variable 'PS' being added to table
#          - Variable 'PSL' being added to table
#          - Variable 'QFLX' being added to table
#          - Variable 'Q' being added to table
#            Variable 'Q' has a vertical dimension, which is currently not supported for the AMWG Table. Skipping...
#          - Variable 'RELHUM' being added to table
#            Variable 'RELHUM' has a vertical dimension, which is currently not supported for the AMWG Table. Skipping...
#          - Variable 'SHFLX' being added to table
#          - Variable 'SST' being added to table
#          - Variable 'SWCF' being added to table
#          - Variable 'T' being added to table
#            Variable 'T' has a vertical dimension, which is currently not supported for the AMWG Table. Skipping...
#          - Variable 'TAUX' being added to table
#          - Variable 'TAUY' being added to table
#          - Variable 'TGCLDIWP' being added to table
#          - Variable 'TGCLDLWP' being added to table
#          - Variable 'TMQ' being added to table
#          - Variable 'TREFHT' being added to table
#          - Variable 'TS' being added to table
#          - Variable 'U' being added to table
#            Variable 'U' has a vertical dimension, which is currently not supported for the AMWG Table. Skipping...
#          - Variable 'U10' being added to table
#          - Variable 'ICEFRAC' being added to table
#          - Variable 'RESTOM' being added to table
#          - Variable 'LANDFRAC' being added to table
#          - Variable 'OCNFRAC' being added to table
#          - Variable 'CLDHGH' being added to table
#          - Variable 'CLDICE' being added to table
#            Variable 'CLDICE' has a vertical dimension, which is currently not supported for the AMWG Table. Skipping...
#          - Variable 'CLDLIQ' being added to table
#            Variable 'CLDLIQ' has a vertical dimension, which is currently not supported for the AMWG Table. Skipping...
#          - Variable 'CLDLOW' being added to table
#          - Variable 'CLDMED' being added to table
#          - Variable 'CLDTOT' being added to table
#          - Variable 'CLOUD' being added to table
#            Variable 'CLOUD' has a vertical dimension, which is currently not supported for the AMWG Table. Skipping...
#          - Variable 'FLNS' being added to table
#          - Variable 'FLNT' being added to table
#          - Variable 'FLNTC' being added to table
#          - Variable 'FSNS' being added to table
#          - Variable 'FSNT' being added to table
#          - Variable 'FSNTC' being added to table
#          - Variable 'LHFLX' being added to table
#          - Variable 'LWCF' being added to table
#          - Variable 'OMEGA500' being added to table
#          - Variable 'PBLH' being added to table
#          - Variable 'PRECL' being added to table
#          - Variable 'PRECT' being added to table
#          - Variable 'PRECSL' being added to table
#          - Variable 'PRECSC' being added to table
#          - Variable 'PRECSC' being added to table
#          - Variable 'PRECC' being added to table
#          - Variable 'PS' being added to table
#          - Variable 'PSL' being added to table
#          - Variable 'QFLX' being added to table
#          - Variable 'Q' being added to table
#            Variable 'Q' has a vertical dimension, which is currently not supported for the AMWG Table. Skipping...
#          - Variable 'RELHUM' being added to table
#            Variable 'RELHUM' has a vertical dimension, which is currently not supported for the AMWG Table. Skipping...
#          - Variable 'SHFLX' being added to table
#          - Variable 'SST' being added to table
#          - Variable 'SWCF' being added to table
#          - Variable 'T' being added to table
#            Variable 'T' has a vertical dimension, which is currently not supported for the AMWG Table. Skipping...
#          - Variable 'TAUX' being added to table
#          - Variable 'TAUY' being added to table
#          - Variable 'TGCLDIWP' being added to table
#          - Variable 'TGCLDLWP' being added to table
#          - Variable 'TMQ' being added to table
#          - Variable 'TREFHT' being added to table
#          - Variable 'TS' being added to table
#          - Variable 'U' being added to table
#            Variable 'U' has a vertical dimension, which is currently not supported for the AMWG Table. Skipping...
#          - Variable 'U10' being added to table
#          - Variable 'ICEFRAC' being added to table
#          - Variable 'RESTOM' being added to table
#       ...AMWG variable table has been generated successfully.
# 
#       Making comparison table...
#       ... Comparison table has been generated successfully

# In[ ]:





# ##### Run Plotting Scripts
# 
# Create plots.
# This call uses the `plotting_scripts` specified in the run-time config file
# 
# ```{admonition} Attention!
# :class: warning
# This will take some time so please be patient!
# ```

# In[ ]:


get_ipython().run_cell_magic('time', '', 'adf.create_plots()\n')


# Output:

#       Generating lat/lon maps...
#          NOTE: Plot type is set to png
#          NOTE: redo_plot is set to False
#          - lat/lon maps for CLDHGH
#          - lat/lon maps for CLDICE
#          - lat/lon maps for CLDLIQ
#          - lat/lon maps for CLDLOW
#          - lat/lon maps for CLDMED
#          - lat/lon maps for CLDTOT
#          - lat/lon maps for CLOUD
#          - lat/lon maps for FLNS
#          - lat/lon maps for FLNT
#          - lat/lon maps for FLNTC
#          - lat/lon maps for FSNS
#          - lat/lon maps for FSNT
#          - lat/lon maps for FSNTC
#          - lat/lon maps for LHFLX
#          - lat/lon maps for LWCF
#          - lat/lon maps for OMEGA500
#          - lat/lon maps for PBLH
#          - lat/lon maps for PRECL
#          - lat/lon maps for PRECT
#          - lat/lon maps for PRECSL
#          - lat/lon maps for PRECSC
#          - lat/lon maps for PRECSC
#          - lat/lon maps for PRECC
#          - lat/lon maps for PS
#          - lat/lon maps for PSL
#          - lat/lon maps for QFLX
#          - lat/lon maps for Q
#          - lat/lon maps for RELHUM
#          - lat/lon maps for SHFLX
#          - lat/lon maps for SST
#          - lat/lon maps for SWCF
#          - lat/lon maps for T
#          - lat/lon maps for TAUX
#          - lat/lon maps for TAUY
#          - lat/lon maps for TGCLDIWP
#          - lat/lon maps for TGCLDLWP
#          - lat/lon maps for TMQ
#          - lat/lon maps for TREFHT
#          - lat/lon maps for TS
#          - lat/lon maps for U
#          - lat/lon maps for U10
#          - lat/lon maps for ICEFRAC
#          - lat/lon maps for OCNFRAC
#          - lat/lon maps for LANDFRAC
#       ...lat/lon maps have been generated successfully.
# 
#       Generating lat/lon vector maps...
#          NOTE: redo_plot is set to False
#          - lat/lon vector maps for TAUX,TAUY
#     Some vectors at source domain corners may not have been transformed correctly
#     Some vectors at source domain corners may not have been transformed correctly
#          - lat/lon vector maps for U,V
#          ERROR: Did not find any oclim_fils. Will try to skip.
#          INFO: Data Location, dclimo_loc is /glade/scratch/richling/ADF/adf_tutorial/data/regrid
#          INFO: The glob is: f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001_V_*.nc
#       ...lat/lon vector maps have been generated successfully.
# 
#       Generating zonal mean plots...
#          NOTE: Plot type is set to png
#          NOTE: redo_plot is set to False
#          - zonal mean plots for CLDHGH
#          - zonal mean plots for CLDICE
#            CLDICE has lev dimension.
#          - zonal mean plots for CLDLIQ
#            CLDLIQ has lev dimension.
#          - zonal mean plots for CLDLOW
#          - zonal mean plots for CLDMED
#          - zonal mean plots for CLDTOT
#          - zonal mean plots for CLOUD
#            CLOUD has lev dimension.
#          - zonal mean plots for FLNS
#          - zonal mean plots for FLNT
#          - zonal mean plots for FLNTC
#          - zonal mean plots for FSNS
#          - zonal mean plots for FSNT
#          - zonal mean plots for FSNTC
#          - zonal mean plots for LHFLX
#          - zonal mean plots for LWCF
#          - zonal mean plots for OMEGA500
#          - zonal mean plots for PBLH
#          - zonal mean plots for PRECL
#          - zonal mean plots for PRECT
#          - zonal mean plots for PRECSL
#          - zonal mean plots for PRECSC
#          - zonal mean plots for PRECSC
#          - zonal mean plots for PRECC
#          - zonal mean plots for PS
#          - zonal mean plots for PSL
#          - zonal mean plots for QFLX
#          - zonal mean plots for Q
#            Q has lev dimension.
#          - zonal mean plots for RELHUM
#            RELHUM has lev dimension.
#          - zonal mean plots for SHFLX
#          - zonal mean plots for SST
#          - zonal mean plots for SWCF
#          - zonal mean plots for T
#            T has lev dimension.
#          - zonal mean plots for TAUX
#          - zonal mean plots for TAUY
#          - zonal mean plots for TGCLDIWP
#          - zonal mean plots for TGCLDLWP
#          - zonal mean plots for TMQ
#          - zonal mean plots for TREFHT
#          - zonal mean plots for TS
#          - zonal mean plots for U
#            U has lev dimension.
#          - zonal mean plots for U10
#          - zonal mean plots for ICEFRAC
#          - zonal mean plots for OCNFRAC
#          - zonal mean plots for LANDFRAC
#       ...Zonal mean plots have been generated successfully.
# 
#       Generating meridional mean plots...
#          NOTE: Plot type is set to png
#          NOTE: redo_plot is set to False
#          - meridional mean plots for CLDHGH
#          - meridional mean plots for CLDICE
#            CLDICE has lev dimension.
#          - meridional mean plots for CLDLIQ
#            CLDLIQ has lev dimension.
#          - meridional mean plots for CLDLOW
#          - meridional mean plots for CLDMED
#          - meridional mean plots for CLDTOT
#          - meridional mean plots for CLOUD
#            CLOUD has lev dimension.
#          - meridional mean plots for FLNS
#          - meridional mean plots for FLNT
#          - meridional mean plots for FLNTC
#          - meridional mean plots for FSNS
#          - meridional mean plots for FSNT
#          - meridional mean plots for FSNTC
#          - meridional mean plots for LHFLX
#          - meridional mean plots for LWCF
#          - meridional mean plots for OMEGA500
#          - meridional mean plots for PBLH
#          - meridional mean plots for PRECL
#          - meridional mean plots for PRECT
#          - meridional mean plots for PRECSL
#          - meridional mean plots for PRECSC
#          - meridional mean plots for PRECSC
#          - meridional mean plots for PRECC
#          - meridional mean plots for PS
#          - meridional mean plots for PSL
#          - meridional mean plots for QFLX
#          - meridional mean plots for Q
#            Q has lev dimension.
#          - meridional mean plots for RELHUM
#            RELHUM has lev dimension.
#          - meridional mean plots for SHFLX
#          - meridional mean plots for SST
#          - meridional mean plots for SWCF
#          - meridional mean plots for T
#            T has lev dimension.
#          - meridional mean plots for TAUX
#          - meridional mean plots for TAUY
#          - meridional mean plots for TGCLDIWP
#          - meridional mean plots for TGCLDLWP
#          - meridional mean plots for TMQ
#          - meridional mean plots for TREFHT
#          - meridional mean plots for TS
#          - meridional mean plots for U
#            U has lev dimension.
#          - meridional mean plots for U10
#          - meridional mean plots for ICEFRAC
#          - meridional mean plots for OCNFRAC
#          - meridional mean plots for LANDFRAC
#       ...Meridional mean plots have been generated successfully.
# 
#       Generating polar maps...
#          NOTE: Plot type is set to png
#          NOTE: redo_plot is set to False
#          - polar maps for CLDHGH
#          - polar maps for CLDICE
#          - polar maps for CLDLIQ
#          - polar maps for CLDLOW
#          - polar maps for CLDMED
#          - polar maps for CLDTOT
#          - polar maps for CLOUD
#          - polar maps for FLNS
#          - polar maps for FLNT
#          - polar maps for FLNTC
#          - polar maps for FSNS
#          - polar maps for FSNT
#          - polar maps for FSNTC
#          - polar maps for LHFLX
#          - polar maps for LWCF
#          - polar maps for OMEGA500
#          - polar maps for PBLH
#          - polar maps for PRECL
#          - polar maps for PRECT
#          - polar maps for PRECSL
#          - polar maps for PRECSC
#          - polar maps for PRECSC
#          - polar maps for PRECC
#          - polar maps for PS
#          - polar maps for PSL
#          - polar maps for QFLX
#          - polar maps for Q
#          - polar maps for RELHUM
#          - polar maps for SHFLX
#          - polar maps for SST
#          - polar maps for SWCF
#          - polar maps for T
#          - polar maps for TAUX
#          - polar maps for TAUY
#          - polar maps for TGCLDIWP
#          - polar maps for TGCLDLWP
#          - polar maps for TMQ
#          - polar maps for TREFHT
#          - polar maps for TS
#          - polar maps for U
#          - polar maps for U10
#          - polar maps for ICEFRAC
#          - polar maps for OCNFRAC
#          - polar maps for LANDFRAC
#       ...polar maps have been generated successfully.
# 
#       Generating Taylor Diagrams...
#     Ambiguous plotting location since all cases go on same plot. Will put them in first location: /glade/scratch/richling/ADF/adf_tutorial/plots/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001_1995_2000_vs_f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001_1995_2000
#          NOTE: Plot type is set to png
#          NOTE: redo_plot is set to False
#          - Plotting Taylor Diagram, ANN
#          Taylor Diagram: completed ANN. 
#          File: /glade/scratch/richling/ADF/adf_tutorial/plots/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001_1995_2000_vs_f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001_1995_2000/TaylorDiag_ANN_Special_Mean.png
#          - Plotting Taylor Diagram, DJF
#          Taylor Diagram: completed DJF. 
#          File: /glade/scratch/richling/ADF/adf_tutorial/plots/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001_1995_2000_vs_f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001_1995_2000/TaylorDiag_DJF_Special_Mean.png
#          - Plotting Taylor Diagram, JJA
#          Taylor Diagram: completed JJA. 
#          File: /glade/scratch/richling/ADF/adf_tutorial/plots/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001_1995_2000_vs_f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001_1995_2000/TaylorDiag_JJA_Special_Mean.png
#          - Plotting Taylor Diagram, MAM
#          Taylor Diagram: completed MAM. 
#          File: /glade/scratch/richling/ADF/adf_tutorial/plots/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001_1995_2000_vs_f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001_1995_2000/TaylorDiag_MAM_Special_Mean.png
#          - Plotting Taylor Diagram, SON
#          Taylor Diagram: completed SON. 
#          File: /glade/scratch/richling/ADF/adf_tutorial/plots/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001_1995_2000_vs_f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001_1995_2000/TaylorDiag_SON_Special_Mean.png
#       ...Taylor Diagrams have been generated successfully.
# 
#       Generating qbo plots...
#          NOTE: redo_plot is set to False
#          QBO plots will be saved here: /glade/scratch/richling/ADF/adf_tutorial/plots/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001_1995_2000_vs_f.cam6_3_106.FLTHIST_v0a.ne30.dcs_non-ogw.001_1995_2000
#       ...QBO plots have been generated successfully.
#     CPU times: user 30min 24s, sys: 30.9 s, total: 30min 55s
#     Wall time: 33min 22s

# <h4>Run Website Generation Scripts</h4>
# 
# Create website if requested in the run-time config file

# In[ ]:


if adf.create_html:
    adf.create_website()


# <p>Output:</p>

#       Generating Diagnostics webpages...
#       ...Webpages have been generated successfully.

# ---

# ### Step 2: Analyze ADF Output
# 
# Once the ADF has completed (either here in Jupyter or previously from terminal run) we can use the `adf` object to gain access to everything available in the ADF. This could be very useful if you want to develop diagsnostics separate from the ADF in a Jupyter Notebook
<code class="docutils literal notranslate"><span class="pre" style="color: #076E85;">&emsp;config_cam_baseline_example.yaml</span></code>
# The `adf` object can be searched for any quantity of interest. Using the dot, `.` and tab function in Jupyter, we can get a list of all the available instances, classes, functions, etc:
# 
# ![adf objects](../../images/adf_dir.png)
# 
# Or calling the <code class="docutils literal notranslate"><span class="pre">dir</span></code> command on the ADF object will print a list of all available objects:

# In[24]:


dir(adf)


# <h5>Grab the case name instances:</h5>

# In[10]:


case_names = adf.get_cam_info("cam_case_name",required=True)
print(case_names)
base_name = adf.get_baseline_info("cam_case_name",required=True)
print(base_name)


# <h5>Grab the case climo years instances:</h5>

# In[11]:


adf.climo_yrs


# <h5>Grab the listed CAM variables from the config file:</h5>

# In[13]:


var_list = adf.diag_var_list
list(var_list)


# <h5>Let's build a custom diagnsotics plot!</h5>

# #### Stratocumulus Over California Example
# 
# Now that we have the ADF done and still have access to all the information contained in the ADF, let's run a custom routine to calculate and plot stratocumulus clouds over California. 
# 
# The point of this example is to highlight using a script not contained in the ADF to simulate custom analysis (that may be a one off diagnsotics need), all within the same notebook as our ADF run.
# 
# Again, this can be very helpful becasue the ADF object has all the paths for the input/output data and case information already saved for convienence.

# In[18]:


# Get the location of the climo files
case_climo_loc = adf.get_cam_info('cam_climo_loc', required=True)
data_loc = adf.get_baseline_info("cam_climo_loc", required=True)


# In[12]:


import matplotlib as mpl
# change color for each case
case_colors = [mpl.cm.tab20(i) for i, case in enumerate(case_names)]


# In[25]:


import geocat.comp as gc  # use geocat's interpolation

def process_case(climo_loc, latitude, longitude, pressurelevels):
    fils = sorted(list(Path(climo_loc).glob(f"*_T_*.nc")))
    temperature = xr.open_mfdataset(fils)['T'].sel(lat=latitude, lon=longitude).compute()
    fils = sorted(list(Path(climo_loc).glob(f"*_Q_*.nc")))
    vapor = xr.open_mfdataset(fils)['Q'].sel(lat=latitude, lon=longitude).compute()
    fils = sorted(list(Path(climo_loc).glob(f"*_CLDLIQ_*.nc")))
    liquid = xr.open_mfdataset(fils)['CLDLIQ'].sel(lat=latitude, lon=longitude).compute()
    # In one of these, we also need the hybrid-sigma coefficients
    fils = sorted(list(Path(climo_loc).glob(f"*_PS_*.nc")))
    ps_ds = xr.open_mfdataset(fils)
    ps = ps_ds['PS'].sel(lat=latitude, lon=longitude).compute()
    hyam = ps_ds['hyam'].isel(time=0).compute() # drop redundant time dimension
    hybm = ps_ds['hybm'].isel(time=0).compute()
    ps.name = "PS"
    
    # we aren't done. Interpolate to pressure levels here:
    t_plev = gc.interp_hybrid_to_pressure(temperature, ps, hyam, hybm, new_levels=pressurelevels, lev_dim='lev').compute()
    q_plev = gc.interp_hybrid_to_pressure(vapor, ps, hyam, hybm, new_levels=pressurelevels, lev_dim='lev').compute()
    liq_plev = gc.interp_hybrid_to_pressure(liquid, ps, hyam, hybm, new_levels=pressurelevels, lev_dim='lev').compute()
    
    t_plev.name = "T"
    q_plev.name = "Q"
    liq_plev.name = 'CLDLIQ'
    
    # But hold on, we actually want theta, not T:
    p = xr.DataArray(pressurelevels, dims='plev', coords={'plev': t_plev.plev})
    # pressurelevels expected in Pa!
    theta_plev = t_plev * ((100000. / p)**0.2854)  # https://glossary.ametsoc.org/wiki/Potential_temperature &  https://glossary.ametsoc.org/wiki/Poisson_constant
    
    # Still not done -- average over the area:
    w = np.cos(np.radians(temperature.lat))  # area weighting
    theta_aave = theta_plev.weighted(w).mean(dim=("lat","lon"))  # (12months x pressurelevels.shape[0])
    theta_aave.name = "THETA"
    q_aave = q_plev.weighted(w).mean(dim=("lat","lon"))
    liq_aave = liq_plev.weighted(w).mean(dim=("lat","lon"))
    ps_aave = ps.weighted(w).mean(dim=("lat","lon"))
    return xr.merge([theta_aave, q_aave, liq_aave, ps_aave])


# In[14]:


import matplotlib.pyplot as plt
from cycler import cycler

def make_plot(ds1, ds2, caselabels):
    fig, ax = plt.subplots(figsize=(9,4), ncols=3, sharey=True, constrained_layout=True)
    custom_cycler = (cycler(color=['k', 'r', 'y', 'y']) +
                 cycler(lw=[2, 2, 1, 1]))
    [a.set_prop_cycle(custom_cycler) for a in ax]
    if ds1['Q'].max() < 0.1:
        qscale = 1000. # kg/kg -> mg/kg
    else:
        qscale = 1
    if ds1['CLDLIQ'].max() < 0.001:
        lscale = 1000.*1000.  # kg/kg -> ug/kg
    else:
        lscale = 1

    ax[0].plot(ds1['Q']*qscale, ds1['plev']/100, label=caselabels[0])
    ax[0].plot(ds2['Q']*qscale, ds2['plev']/100, label=caselabels[1])
    ax[0].set_xlim([0,25])
    ax[0].set_xlabel("Specific Humidity [g/kg]")
    ax[1].plot(ds1['THETA'], ds1['plev']/100)
    ax[1].plot(ds2['THETA'], ds2['plev']/100)
    ax[1].set_xlabel("Potential Temperature [K]")
    ax[1].set_xlim([275, 325])
    ax[2].plot(ds1['CLDLIQ']*lscale, ds1['plev']/100)
    ax[2].plot(ds2['CLDLIQ']*lscale, ds2['plev']/100)
    ax[2].set_xlabel("Cloud Liquid [$\mu$g/kg]")
    ax[2].set_xlim([0,150])
    ax[2].invert_yaxis()
    ax[0].set_ylabel("Pressure")
    [a.spines['top'].set_visible(False) for a in ax]
    [a.spines['right'].set_visible(False) for a in ax]
    fig.legend(loc='upper left', bbox_to_anchor=(0.0, -0.01))
    return fig, ax


# In[16]:


from pathlib import Path
import xarray as xr
import numpy as np

# define domain
latslice = slice(20,30)
lonslice = slice(230,240) # Klein&Hartmann 1993, Table 1
levels = 100.*np.arange(600.0, 1015., 15)  # chosen for convenience. Go finer if native grid is finer.


# In[19]:


ref_ds = process_case(data_loc, latslice, lonslice, levels)

for i, c in enumerate(case_names):
    case_ds = process_case(case_climo_loc[i], latslice, lonslice, levels)
    print("case ready")
    for s in seasons:
        ref_season = ref_ds.sel(time=seasons[s]).mean(dim='time')
        case_season = case_ds.sel(time=seasons[s]).mean(dim='time')
        # ** Ready to make plot **
        labels = [data_name, c]
        casefig, caseax = make_plot(ref_season, case_season, labels)
        casefig.suptitle(f"California Stratocumulus, {s}")
        plt.show()


# In[ ]:





# In[ ]:





# 

# 

# 

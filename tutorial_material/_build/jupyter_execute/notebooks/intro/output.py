#!/usr/bin/env python
# coding: utf-8

# ## What do you get?
# 
# ##### Available Output Data Files
# 
# <ul>
# <li><h6> Time series</h6></li>
# <li><h6> Climotology files</h6></li>
# <li><h6> Regridded (Climo) files</h6></li>
# <li><h6> Transformed Eulerian Mean (TEM) files</h6></li>
# </ul>
# 
# ##### Available Plots:
# 
# Click on the image for a larger version
# 
# ###### AMWG statistics tables
# 
# 
# ```{figure} ./amwg_table_subset.png
# ---
# width: 1000px
# name: directive-fig
# ---
# Here is my figure caption!
# ```
# 
# 
# ###### Global lat/lon plots
# 
# ```{figure} ./PRECT_ANN_LatLon_Mean.png
# ---
# height: 450px
# name: directive-fig
# ---
# Here is my figure caption!
# ```
# 
# ###### Global lat/lon vector plots
# 
# ```{figure} ./Surface_Wind_Stress_ANN_LatLon_Vector_Mean.png
# ---
# height: 450px
# name: directive-fig
# ---
# Here is my figure caption!
# ```
# 
# 
# ###### Zonal plots
# 
# ```{figure} ./OMEGA500_ANN_Zonal_Mean.png
# ---
# height: 450px
# name: directive-fig
# ---
# Here is my figure caption!
# ```
# 
# 
# ```{figure} ./RELHUM_ANN_Zonal_logp_Mean.png
# ---
# height: 450px
# name: directive-fig
# ---
# Here is my figure caption!
# ```
# 
# 
# ###### Meridional plots
# 
# ```{figure} ./PRECT_ANN_LatLon_Mean.png
# ---
# height: 450px
# name: directive-fig
# ---
# Here is my figure caption!
# ```
# 
# ###### SH and NH polar plots
# 
# ```{figure} ./PS_DJF_SHPolar_Mean.png
# ---
# height: 450px
# name: directive-fig
# ---
# Here is my figure caption!
# ```
# 
# ```{figure} ./PS_DJF_NHPolar_Mean.png
# ---
# height: 450px
# name: directive-fig
# ---
# Here is my figure caption!
# ```
# 
# 
# 
# 
# 
# 
# 
# ###### Quasi-Biaennial Oscillation (QBO) plots
# 
# ```{figure} ./QBOts.png
# ---
# width: 650px
# name: directive-fig
# ---
# Here is my figure caption!
# ```
# 
# ```{figure} ./QBOamp.png
# ---
# height: 450px
# name: directive-fig
# ---
# Here is my figure caption!
# ```
# 
# 
# 
# 
# 
# 
# ###### Taylor diagrams
# 
# 
# 
# ```{figure} ./TaylorDiag_ANN_Special_Mean.png
# ---
# height: 450px
# name: directive-fig
# ---
# Here is my figure caption!
# ```
# 
# ###### Transformed Eulerian Mean (TEM) plots
# 
# ```{figure} ./ANN_TEM_Mean_smaller.png
# ---
# height: 450px
# name: directive-fig
# ---
# Here is my figure caption!
# ```
# 
# ###### Time Series plots (under development)
# 
# ```{figure} ./TimeSeries_w26h_ANN.png
# ---
# height: 450px
# name: directive-fig
# ---
# Here is my figure caption!
# ```
# 
# ###### Tape Recorder plots of Q (under development)
# 
# ```{figure} ./Q_tape_recorder_FCLTHIST_vs_FLTHIST_2000_2011.png
# ---
# width: 850px
# 
# name: directive-fig
# ---
# Here is my figure caption!
# ```
# 
# ##### Your custom plots!
# 
# ```{figure} ./strato_ann.png
# ---
# width: 850px
# 
# name: directive-fig
# ---
# Here is my figure caption!
# ```
# 
# ##### Website Generation
# 
# Host your diagnostics to a webpage for easy viewing of plots!
# 
# ```{figure} ../../images/home_page.png
# ---
# width: 850px
# 
# name: directive-fig
# ---
# Here is my figure caption!
# ```
# 
# ---
<style>
/* Three image containers (use 25% for four, and 50% for two, etc) */
.column {
  float: left;
  width: 33.33%;
  padding: 5px;
}

/* Clear floats after image containers */
.row::after {
  content: "";
  clear: both;
  display: table;
}

img[alt=polar] { width: 400px; }

</style>

<div class="row">
<div class="column">
      
![polar](PS_DJF_NHPolar_Mean.png)

</div>
<div class="column">

![polar](PS_DJF_SHPolar_Mean.png)

</div>
</div>


<style>
.img-hover-zoom {
  height: 300px;
  overflow: hidden;
}


.img-hover-zoom img {
  transition: transform .5s ease;
}

.img-hover-zoom:hover img {
  transform: scale(1.5);
}
</style>
<div class="img-hover-zoom">
<img src="amwg_table_subset.png" alt="tables">
</div><img src="amwg_table_subset.png" alt="This zooms-in really well and smooth">
![image](U_ANN_Zonal_Mean.png)<style>
/* Three image containers (use 25% for four, and 50% for two, etc) */
.column {
  float: left;
  width: 33.33%;
  padding: 5px;
}

/* Clear floats after image containers */
.row::after {
  content: "";
  clear: both;
  display: table;
}

</style>

<div class="row">
<div class="column">
      
![image](U_ANN_Zonal_Mean.png)

</div>
<div class="column">

![image](QBOamp.png)

</div>
</div><img src='AODVISdn_ANN_LatLon_Mean.png' onclick='this.src="full_size.gif"' /><style>
    table, tr, th, td{
        border: 2px solid black;
        border-collapse: collapse;
        padding: 8px;
        text-align: center;
    }
    th{
        background-color: #f5f5f5;
    }
</style>


<table width="50%">
    <tr>
        <th>Plot Type</th>
        <th>Example</th>
        <!--<th>Category</th>-->
    </tr>
    <tr>
        <td>Taylor Diagram</td>
        <td>```{figure} ./TaylorDiag_ANN_Special_Mean.png
---
height: 450px
name: directive-fig
---
Here is my figure caption!
```</td>
    </tr>
    <tr>
        <td>Global Lat/Lon</td>
        <td><div><img src="./PRECT_ANN_LatLon_Mean.png" alt="lat/lon" width="400"/></div></td>
    </tr>
    <tr>
        <td>Rabbit</td>
        <td>![](PRECT_ANN_LatLon_Mean.png)</td>
    </tr>
    <tr>
        <td>Parrot</td>
        <td><img src="parrot.jpg" alt="Tiger" width="100px"></td>
    </tr>
</table>
# In[ ]:




::::{attention}
Depending on how many years, plot types and variables you configure, the more time it takes

* Rough average for all default plots, 10-20 years for 30 variables is ~45 minutes

:::{note}
This is an active area of development; there are potential ways of cutting time/processes
:::
::::
# <p style="font-size:18px">This was a quick intro to the ADF, please refer to the <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/reference/intro.html">reference section</a> for detailed information for each part of the ADF!</p>

# 

# 

# 

# 

# In[ ]:





# In[ ]:





# In[ ]:





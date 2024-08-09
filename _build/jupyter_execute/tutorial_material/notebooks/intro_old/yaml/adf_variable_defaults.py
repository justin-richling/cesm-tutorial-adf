#!/usr/bin/env python
# coding: utf-8

# # Variable Defaults - adf_variable_defaults.yaml
# 
# Location for many plotting, unit, etc defualts for any/all CAM output variables
# 

# ## Variable Default Settings
# 
# ###### Custom Set <p>*</p>
# 
# <p>If you plan on using a modified file for your custom values you need to set the path to the custom variable default file with <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/intro/yaml/config_cam_baseline_example.html#code-class-docutils-literal-notranslate-span-class-pre-defaults-file-span-code"><code class="docutils literal notranslate"><span class="pre">defaults_file</span></code></a>
# </p>
# 
# ::::{Warning}
# <strong>Please do not modify this file unless you plan to push your changes back to the ADF repo!</strong>
#              
# If you would like to use a custom file for your personal ADF runs then it is recommended to make a copy of this file, make modifications in that copy, and then point the ADF to it using the `defaults_file` config variable in the <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/configs/yaml/runtime.html#defaults-file"><code class="docutils literal notranslate"><span class="pre">config_your_run.yaml</span></code> (copy of config_cam_baseline_example.yaml)</a>.
# 
# 
# :::{admonition} Example
# :class: seealso
# From the ADF root directory
# 
#     cp lib/adf_variable_defaults.yaml lib/my_variable_defaults.yaml
# 
# In <code class="docutils literal notranslate"><span class="pre">config_your_run.yaml</span></code>:
# 
# Under the subset `diag_basic_info`:
# 
# <p style="margin-top: -5px;">&ensp; defaults_file: <code class="docutils literal notranslate"><span class="pre">/path/to/your_variable_defaults.yaml</span></code></p>
# :::
# ::::
If you want to use default obs files from a set location, you do this through config_cam_baseline_example.yaml. You can also change any individual path on the adf_variable_defaults file. Please see the documentation if you're confused. 
# These are the values that can be set for each variable. None are required.
<h3>compare_obs2<a class="headerlink" href="#compare_obs2" title="Permalink to this heading">#</a></h3>
# ### Plotting
# 
# <h4><code class="docutils literal notranslate"><span class="pre">colormap</span></code><a class="headerlink" href="#colormap" title="Permalink to this heading">#</a></h4>
# <ul>
# <li><p>The colormap that will be used for filled contour plots.</p></li>
# </ul>
# 
# <h4><code class="docutils literal notranslate"><span class="pre">contour_levels</span></code></h4>
# <ul>
# <li><p>A list of the specific contour values that will be used for contour plots.</p></li>
# <li><p>Cannot be used with "contour_levels_range".</p></li>
# </ul>
# 
# <h4><code class="docutils literal notranslate"><span class="pre">contour_levels_range</span></code></h4>
# <ul>
# <li><p>The contour range that will be used for plots.</p></li>
# <li><p>Values are min, max, and stride.</p></li>
# <li><p>Cannot be used with "contour_levels".</p></li>
# </ul>
# 
# <h4><code class="docutils literal notranslate"><span class="pre">diff_colormap</span></code></h4>
# <ul>
# <li><p>The colormap that will be used for filled contour different plots</p></li>
# </ul>
# 
# <h4><code class="docutils literal notranslate"><span class="pre">diff_contour_levels</span></code></h4>
# <ul>
# <li><p>A list of the specific contour values thta will be used for difference plots.</p></li>
# <li><p>Cannot be used with "diff_contour_range".</p></li>
# </ul>
# 
# <h4><code class="docutils literal notranslate"><span class="pre">diff_contour_range</span></code></h4>
# <ul>
# <li><p>The contour range that will be used for difference plots.</p></li>
# <li><p>Values are min, max, and stride. Cannot be used with "diff_contour_levels".</p></li>
# </ul>
# 
# <h4><code class="docutils literal notranslate"><span class="pre">scale_factor</span></code></h4>
# <ul>
# <li><p>Amount to scale the variable (relative to its "raw" model values).</p></li>
# </ul>
# 
# <h4><code class="docutils literal notranslate"><span class="pre">add_offset</span></code></h4>
# <ul>
# <li><p>Amount of offset to add to the variable (relatie to its "raw" model values).</p></li>
# </ul>
# 
# <h4><code class="docutils literal notranslate"><span class="pre">new_unit</span></code></h4>
# <ul>
# <li><p>Variable units (if not using the  "raw" model units).</p></li>
# </ul>
# 
# <h4><code class="docutils literal notranslate"><span class="pre">mpl</span></code></h4>
# <ul>
# <li><p>Dictionary that contains keyword arguments explicitly for matplotlib</p></li>
# </ul>
# 
# <h4><code class="docutils literal notranslate"><span class="pre">mask</span></code></h4>
# <ul>
# <li><p>Setting that specifies whether the variable should be masked.</p></li>
# <li><p>Currently only accepts "ocean", which means the variable will be masked everywhere that isn't open ocean.</p></li>
# </ul>

```{attention} This admonition was styled...
If only the file name is given, then the file is assumed to exist in the path specified by `obs_data_loc` in the config file.
```
    
# ### Observations
# 
# <p>If you want to use observation files that are not in the same location as the ones set in <code class="docutils literal notranslate"><span class="pre">obs_data_loc</span></code> config variable in the <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/intro/yaml/config_cam_baseline_example.html#code-class-docutils-literal-notranslate-span-class-pre-obs-data-loc-span-code"><code class="docutils literal notranslate"><span class="pre">config_your_run.yaml</span></code> (copy of config_cam_baseline_example.yaml)</a> file, you can set them on a variable by variable basis here.</p>
# 
# <h4><code class="docutils literal notranslate"><span class="pre">obs_file</span></code><a class="headerlink" href="#obs_file" title="Permalink to this heading">#</a></h4>
# <ul>
# <li><p>Path to observations file.</p></li>
# </ul>
# 
# <ul class="adom">
# <div class="admonition attention">
# <p class="admonition-title">Attention</p>
# <p>If only the file name is given (<strong>some_OBS.nc</strong>), then the file is assumed to exist in the path specified by <code class="docutils literal notranslate"><span class="pre">obs_data_loc</span></code> in the <a class="reference internal" href="https://justin-richling.github.io/ADF-Tutorial/notebooks/intro/yaml/config_cam_baseline_example.html#obs_data_loc"><span class="std std-ref">config file</span></a>.</p><br>
# <p>Otherwise, if a path is supllied with a file name (<strong>/path/to/some_OBS.nc</strong>), the ADF will search that instead of what is supplied in the <code class="docutils literal notranslate"><span class="pre">obs_data_loc</span></code> location</p>
# </div>
# </ul>
# 
# <h4><code class="docutils literal notranslate"><span class="pre">obs_name</span></code></h4>
# <ul>
# <li><p>Name of the observational dataset (mostly used for plotting and generated file naming).</p></li>
# <li><p>If this isn't present then the <code class="docutils literal notranslate"><span class="pre">obs_file</span></code> file name is used.</p></li>
# </ul>
# 
# <h4><code class="docutils literal notranslate"><span class="pre">obs_var_name</span></code></h4>
# <ul>
# <li><p>Variable in the observations file to compare against.</p></li>
# <li><p>If this isn't present then the variable name is assumed to be the same as the model variable name.</p></li>
# </ul>

# ### Vector
# 
# <h4><code class="docutils literal notranslate"><span class="pre">vector_pair</span></code></h4>
# <ul>
# <li><p>Another variable that when combined with the given variable makes up a vector pair.</p></li>
# <li><p>If this default is not present then it is assumed the given variable is not a vector component, and will thus be skipped during the vector plotting phase.</p></li>
# </ul>
# 
# <h4><code class="docutils literal notranslate"><span class="pre">vector_name</span></code></h4>
# <ul>
# <li><p>The name of the vector the variable is associated with, which will be used to title the respective vector plot(s).</p></li>
# </ul>

# ### Website
# 
# <h4><code class="docutils literal notranslate"><span class="pre">category</span></code></h4>
# <ul>
# <li><p>The website category the variable will be placed under.</p>
# </ul>

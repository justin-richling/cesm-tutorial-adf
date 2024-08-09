#!/usr/bin/env python
# coding: utf-8

# # YAML Config Files
# 
# The ADF requires 2 different yaml configuration files: 
# 
# `config_cam_baseline_example.yaml` and `adf_variable_defaults.yaml`
# 
# If yaml files are new to you, they are just specialized text files that python (and other languages) can read in and use as configuration files. 
# 
# 
# 
# 
# In the case of the ADF, the variables set in the yaml files will be parsed into Python dictionaries and will accessable throughout the ADF workflow.
# 
# A couple of notes about using the ADF yaml files:
# &ensp;&ensp;Variables can be referenced within the yaml file<br>
# &ensp;&ensp;Variables <strong>cannot</strong> be used in nested varaibles lists<br>
# &ensp;&ensp;&ensp;&ensp;ie: 
# 
# 
# 
# 
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
<div class="admonition tip">
<p>** works **</p>
<p>user: richling<br>some_path: /glade/u/home/${user}</p>
</div>

<div class="admonition error">
<p>** does not work **</p>
<p>user: richling<br>
case: some_run<br>some_path:<br>
&ensp;&ensp;&ensp;- /glade/u/home/${user}<br>
&ensp;&ensp;&ensp;- /glade/u/home/${user}/${case}
</p>
  <div class="admonition tip">
  <div class="title">** works **</div>
  <p>some_path:<br>
&ensp;&ensp;&ensp;- /glade/u/home/richling<br>
&ensp;&ensp;&ensp;- /glade/u/home/richling/some_run
</p>
  </div>
</div>



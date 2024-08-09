#!/usr/bin/env python
# coding: utf-8

# # YAML File Basics
# 
# Basic tips and tricks for using the yaml file in the ADF config files

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

# 

# 

# 

# 

# 

#!/usr/bin/env python
# coding: utf-8

# # YAML File Basics
# 
# Basic tips and tricks for using the yaml file in the ADF config files

# A couple of notes about using the ADF yaml files:<br>
# <ul>
# <li>&ensp;&ensp;Variables can be referenced within the yaml file</li>
# <li>&ensp;&ensp;Variables <strong>cannot</strong> be used in nested varaibles lists</li>
# 
# <div style="margin-top: -2em;">
# <section id="sidebar-content">
# <div>
# <h4></h4>
# <aside style="margin: 0 0 0.5em 3em; padding: 1px; width: 46%; float: left; clear: left; overflow-x: auto;">
# <div class="admonition">
# <p class="admonition-title">** works **</p>
# <p><strong>some_path:</strong><br>
# &ensp;&ensp;&ensp;- /glade/u/home/richling<br>
# &ensp;&ensp;&ensp;- /glade/u/home/richling/some_run
# </p>
# </div>
# </aside>
# </div>
#     
# <div>
# <aside style="margin: 0 0 0.5em 0; padding: 1px; width: 46%; float: right; clear: right; overflow-x: auto;">
# <div class="admonition error">
# <p class="admonition-title">** does not work **</p>
# <p><strong>user:</strong> richling<br>
# <strong>case:</strong> some_run<br>
# <strong>some_path:</strong><br>
# &ensp;&ensp;&ensp;- /glade/u/home/${user}<br>
# &ensp;&ensp;&ensp;- /glade/u/home/${user}/${case}
# </p>
# </div>
# </aside>
# </div>
# 
# </section>
# </div>
# 
# <li><p>AHAHAHAHAHAHAH<br><br><br></p></li>
# </ul>

# 

# 

# 

# 

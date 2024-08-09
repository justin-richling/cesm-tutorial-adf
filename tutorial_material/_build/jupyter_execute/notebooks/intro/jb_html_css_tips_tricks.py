#!/usr/bin/env python
# coding: utf-8

# # Jupyter Book/HTML/CSS Tips and Tricks

# **<u>AMWG</u>** (Atmospheric Model Working Group) <u>**D**</u>iagnostics <u>**F**</u>ramework

# This package is meant to be an update/upgrade to the much used and beloved AMWG diagnostics package used by the atmospheric/chemistry CESM community.

# The ADF is a collection of analysis plots and data derived from CAM history output files. 
# 
# It is a multipurpose tool that has been built to be somewhat flexible.
# 
# What do you get?
# 
# * Time series
# * Climotology files
# * Regridded (Climo) files
# 
# Plots:
# 
# * 

# * <p style="margin-top: -5px;">Global Variables</p>
# * <p style="margin-top: -5px;">diag_basic_info</p>
# * <p style="margin-top: -5px;">diag_cam_climo</p>
# * <p style="margin-top: -5px;">diag_cam_baseline_climo</p>
# 

# `````{admonition} Conda cheat sheet for reference
# :class: tip, dropdown
# [conda](conda-cheatsheet.pdf)
# `````

# The ADF is still under active development and is near it's first major version. 

# <div class="admonition">
# <p>Some **content**</p>
#   <div class="admonition tip">
#   <div class="title">A *title*</div>
#   <p>Paragraph 1</p>
#   <p>Paragraph 2</p>
#   </div>
# </div>

# <div class="admonition">
# <p>Some **content**</p>
#   <div class="admonition error">
#   <div class="title">Oh jeez, I hope this worked...</div>
#   <p>Paragraph 1</p>
#   <p>Paragraph 2</p>
#   </div>
# </div>

# ```{success}
# s-u-c-c-e-s-s that's the way you spell success...
# ```

# ```{tip}
# Arrrrgggg.....
# ```

# ```{hint}
# :class: dropdown
# wakkawakka
# ```

# ```{error}
# What color is this going to be?
# ```

# ```{warning}
# Uh, where's his car dude
# ```
# 
# ```{admonition} Life Tip
# <p>Change your bed sheets every week</p>
# <p>Don't be gross</p>
# ```
# 
# ```{admonition} Here's your admonition
# Here's the admonition content
# ```

# ```{attention}
# Depending on how many years, plot types and variables you configure, the more time it takes
# 
# * Rough average for all default plots, 10-20 years for 30 variables is ~45 minutes
# 
# ````{note}
# This is an active area of development; there are potential ways of cutting time/processes
# ````
# 
# ```

# ::::{important}
# :::{note}
# This text is **standard** _Markdown_
# :::
# ::::

# ::::{attention}
# Depending on how many years, plot types and variables you configure, the more time it takes
# 
# * Rough average for all default plots, 10-20 years for 30 variables is ~45 minutes
# 
# :::{note}
# This is an active area of development; there are potential ways of cutting time/processes
# :::
# ::::

# ## Third set in yaml file:&ensp; $\color{#117284}{\textit{diag\_cam\_baseline\_climo}}$

# | Syntax      | Description |
# | ----------- | ----------- |
# | Header      | Title       |
# | Paragraph   | Text        |

# |       |  |       |
# | :---        |    :----:   |          ---: |
# | Header      | Title       | Here's this   |
# | Paragraph   | Text        | And more      |

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

# `````{admonition} Conda cheat sheet for reference
# :class: tip, dropdown
# [conda](conda-cheatsheet.pdf)
# `````
# 
# 

# <div><p style="font-size: 25px; font-weight: bold; color: #076E85;">Alright here we go</p></div>

# # Single Case Comparison
# 
# <p>Let's now put it all together and do a CAM vs CAM comparison.</p>
# <p>Revisit (or reopen) your copy of the runtime configure file (ie )</p>

# `````{admonition} Wowsie
# :class: important
# This is really helpful, thank you.
# `````

# <section id="sidebar-content">
# <span id="layout-sidebar"></span><h2>Sidebar content<a class="headerlink" href="#sidebar-content" title="Permalink to this heading">#</a></h2>
# <p>Adding sidebar elements allow you to provide contextual information that doesn’t break
# up the flow of your main content. It is one of the main patterns recommended in the
# <a class="reference external" href="https://edwardtufte.github.io/tufte-css/">Tufte style guide</a>.</p>
# <p>There are two kinds of sidebars supported by Jupyter Book. We’ll
# describe them below.</p>
# <div class="admonition note">
# <p class="admonition-title">Note</p>
# <p>Some sidebar content behaves differently depending on the screen size. If the screen is narrow
# enough, the sidebar content will exist in-line with your content. Make the screen
# wider and it’ll pop out to the right.</p>
# </div>
# <section id="sidebars-within-content">
# <h3>Sidebars within content<a class="headerlink" href="#sidebars-within-content" title="Permalink to this heading">#</a></h3>
# <aside class="sidebar">
# <p class="sidebar-title">Here is some sidebar content</p>
# <p>It spans a bit of your main content, as well as the margin, as seen by the
# note block below:</p>
# <div class="admonition note">
# <p class="admonition-title">Note</p>
# <p>Here’s a note block within the sidebar!</p>
# </div>
# </aside>
# <p>If you use a sidebar within your content, the sidebar will stay in-line with your page’s content. However, it will be
# placed to the right, allowing your content to wrap around it. This prevents
# the sidebar from breaking up the flow of your content. This is particularly
# useful if you’ve got tall-and-long blocks of content or images that you would
# like to provide context to throughout your content.</p>
# <p>To add a sidebar to your content, use the following syntax:</p>
# <div class="highlight-md notranslate"><div class="highlight"><pre id="codecell1"><span></span>```{sidebar} My sidebar title
# My sidebar content
# ```
# </pre><button class="copybtn o-tooltip--left" data-tooltip="Copy" data-clipboard-target="#codecell1">
#       <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-copy" width="44" height="44" viewBox="0 0 24 24" stroke-width="1.5" stroke="#000000" fill="none" stroke-linecap="round" stroke-linejoin="round">
#   <title>Copy to clipboard</title>
#   <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
#   <rect x="8" y="8" width="12" height="12" rx="2"></rect>
#   <path d="M16 8v-2a2 2 0 0 0 -2 -2h-8a2 2 0 0 0 -2 2v8a2 2 0 0 0 2 2h2"></path>
# </svg>
#     </button></div>
# </div>
# </section>
# <section id="margin-content">
# <h3>Margin content<a class="headerlink" href="#margin-content" title="Permalink to this heading">#</a></h3>
# <p>To add content to the margin with MyST Markdown, use this syntax:</p>
# <div class="highlight-md notranslate"><div class="highlight"><pre id="codecell2"><span></span>```{margin} An optional title
# My margin content
# ```
# </pre><button class="copybtn o-tooltip--left" data-tooltip="Copy" data-clipboard-target="#codecell2">
#       <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-copy" width="44" height="44" viewBox="0 0 24 24" stroke-width="1.5" stroke="#000000" fill="none" stroke-linecap="round" stroke-linejoin="round">
#   <title>Copy to clipboard</title>
#   <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
#   <rect x="8" y="8" width="12" height="12" rx="2"></rect>
#   <path d="M16 8v-2a2 2 0 0 0 -2 -2h-8a2 2 0 0 0 -2 2v8a2 2 0 0 0 2 2h2"></path>
# </svg>
#     </button></div>
# </div>
# 
# 
#     
# 
# <aside class="margin sidebar">
# <p class="sidebar-title"><strong>For example</strong></p>
# <p>Here’s some margin content! It was created by using the</p>
# <div class="highlight-default notranslate"><div class="highlight"><pre id="codecell3"><span></span>```{margin}
# ```
# </pre><button class="copybtn o-tooltip--left" data-tooltip="Copy" data-clipboard-target="#codecell3">
# <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-copy" width="44" height="44" viewBox="0 0 24 24" stroke-width="1.5" stroke="#000000" fill="none" stroke-linecap="round" stroke-linejoin="round">
# <title>Copy to clipboard</title>
# <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
# <rect x="8" y="8" width="12" height="12" rx="2"></rect>
# <path d="M16 8v-2a2 2 0 0 0 -2 -2h-8a2 2 0 0 0 -2 2v8a2 2 0 0 0 2 2h2"></path>
# </svg>
# </button>
# </div>
# </div> 
# 
# 
# 
# 
# 
# <div class="admonition important">
# <p class="admonition-title">Wowsie</p>
# <p>This is really helpful, thank you.</p>
# </div>
# 
# <p>directive in a Markdown cell. Jupyter Book automatically converts these
# cells into helpful margin content.</p>
# </aside>
# 
#     
# 
# <p>Controlling margin content with code cells uses a slightly different syntax,
# which we’ll cover below.</p>
# </section>
# <section id="margins-with-code-cells">
# <h3>Margins with code cells<a class="headerlink" href="#margins-with-code-cells" title="Permalink to this heading">#</a></h3>
# <p>You can make a code cell move to the right margin by adding <code class="docutils literal notranslate"><span class="pre">margin</span></code> to your
# cell’s tags.</p>
# <div class="sd-tab-set docutils">
# <input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
# <label class="sd-tab-label" for="sd-tab-item-0">
# Jupyter Notebook</label><div class="sd-tab-content docutils">
# <p>Here’s what the cell metadata for a margin cell looks like:</p>
# <div class="highlight-json notranslate"><div class="highlight"><pre id="codecell4"><span></span><span class="p">{</span>
# <span class="w">    </span><span class="nt">"tags"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
# <span class="w">        </span><span class="s2">"margin"</span><span class="p">,</span>
# <span class="w">    </span><span class="p">]</span>
# <span class="p">}</span>
# </pre><button class="copybtn o-tooltip--left" data-tooltip="Copy" data-clipboard-target="#codecell4">
#       <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-copy" width="44" height="44" viewBox="0 0 24 24" stroke-width="1.5" stroke="#000000" fill="none" stroke-linecap="round" stroke-linejoin="round">
#   <title>Copy to clipboard</title>
#   <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
#   <rect x="8" y="8" width="12" height="12" rx="2"></rect>
#   <path d="M16 8v-2a2 2 0 0 0 -2 -2h-8a2 2 0 0 0 -2 2v8a2 2 0 0 0 2 2h2"></path>
# </svg>
#     </button></div>
# </div>
# <div class="admonition seealso">
# <p class="admonition-title">See also</p>
# <p><a class="reference internal" href="metadata.html#jupyter-cell-tags"><span class="std std-ref">Add metadata to notebooks</span></a></p>
# </div>
# </div>
# <input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
# <label class="sd-tab-label" for="sd-tab-item-1">
# MyST Text File</label><div class="sd-tab-content docutils">
# <p>For a MyST text file these tags can be added to the <code class="docutils literal notranslate"><span class="pre">code-cell</span></code></p>
# <div class="highlight-md notranslate"><div class="highlight"><pre id="codecell5"><span></span>```{code-cell} &lt;language&gt;
# :tags: [margin]
# ```
# </pre><button class="copybtn o-tooltip--left" data-tooltip="Copy" data-clipboard-target="#codecell5">
#       <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-copy" width="44" height="44" viewBox="0 0 24 24" stroke-width="1.5" stroke="#000000" fill="none" stroke-linecap="round" stroke-linejoin="round">
#   <title>Copy to clipboard</title>
#   <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
#   <rect x="8" y="8" width="12" height="12" rx="2"></rect>
#   <path d="M16 8v-2a2 2 0 0 0 -2 -2h-8a2 2 0 0 0 -2 2v8a2 2 0 0 0 2 2h2"></path>
# </svg>
#     </button></div>
# </div>
# </div>
# </div>
# <p>For example, we’ll re-display the figure above, and add a <code class="docutils literal notranslate"><span class="pre">margin</span></code> tag to the code cell.</p>
# <div class="cell tag_margin docutils container">
# <div class="cell_input docutils container">
# <div class="highlight-ipython3 notranslate"><div class="highlight"><pre id="codecell6"><span></span><span class="n">make_fig</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">5</span><span class="p">))</span>
# </pre><button class="copybtn o-tooltip--left" data-tooltip="Copy" data-clipboard-target="#codecell6">
#       <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-copy" width="44" height="44" viewBox="0 0 24 24" stroke-width="1.5" stroke="#000000" fill="none" stroke-linecap="round" stroke-linejoin="round">
#   <title>Copy to clipboard</title>
#   <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
#   <rect x="8" y="8" width="12" height="12" rx="2"></rect>
#   <path d="M16 8v-2a2 2 0 0 0 -2 -2h-8a2 2 0 0 0 -2 2v8a2 2 0 0 0 2 2h2"></path>
# </svg>
#     </button></div>
# </div>
# </div>
# <div class="cell_output docutils container">
# <img alt="../_images/40467a5c76498c535f614c6cd35f51859dcd4d36d426022fff300f5010b0f03e.png" src="../_images/40467a5c76498c535f614c6cd35f51859dcd4d36d426022fff300f5010b0f03e.png">
# </div>
# </div>
# <p>This can be combined with other tags like <code class="docutils literal notranslate"><span class="pre">remove-input</span></code> to <strong>only display the figure</strong>.</p>
# <p>The <a class="reference internal" href="../reference/cheatsheet.html#myst-cheatsheet"><span class="std std-ref">MyST cheat sheet</span></a> provides a <a class="reference internal" href="../reference/cheatsheet.html#myst-cheatsheet-code-cell-tags"><span class="std std-ref">list of <code class="docutils literal notranslate"><span class="pre">code-cell</span></code> tags available</span></a></p>
# </section>

# `````{admonition} This admonition was styled...
# :class: seealso
# With a seealso class!
# `````

# ```{admonition} Here's your admonition
# Here's the admonition content
# ```

# <div class="myownstyle admonition">
#   <p class="first admonition-title">my title goes here</p>
#   <p class="last">this is the admonition text</p>
# </div>

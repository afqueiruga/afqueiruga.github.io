---
layout: post
title:  "New Workflow for Scientific Blogging"
date:   2017-11-28 22:30:22 -0800
categories: workflow
---

## POST IN PROGRESS

# Goal

For better or for worse, I'm constantly tweaking my workflow. (Usually
for worse.) If you've read the footer to this website, you've gathered
that I'm trying some drastic changes with this outlet yet again.

Here's the current problem I'm trying to tackle. As a scientist, I
am hyperfocused on a topic of interest, and I'll code it up, come up
with conclusions, and start writing up a paper draft. The problem is
that 90% of the time the research goes nowhere, so all of my notes,
codes, and journal paper drafts die in a decentralized
graveyard across hard drives and moleskines. 

A talk I just attended by Nkosi Muse had an interesting take on classifying
the form of communication:
1. Scientist-to-scientist
2. Scientist-to-public
I'm only interested in the scientist-to-scientist aspect right now,
but the scientist-to-public aspect brings up some interesting
questions on what a new format should look like. I want an s2s format
to absolutely complete: one report repository should contain all of
the code, manuscript, and referenced data that is needed to replicate
the analysis. 

A good format should have this:
1. Everything LaTeX can do: equations, BibTeX bibliography
2. Simplified markup syntax (LaTeX is both ugly and unexpressive)
3. Embed some basic codes that can execute, e.g. to create plots or
tables
4. Make hyperlink-esque references to the source code base
5. Compile into both journal-friendly tex and website friendly html,
   with conditional outputting, a la org-mode publish targets
6. Easy to use, collaborate-able.


# History

I've tried tons of different work flows over the years:

1. Pure LaTeX
  - *Pro:* Lowest common denominator; will never be obsolete
  - *Pro:* Online editors like overleaf
  - *Pro:* A lot of control over the pdf layout; good for
    presentations and posters too
  - *Con:* The markup language is ugly, and too much control
  - *Con:* Looks ugly when it turns into html
  - *Con:* Not a format for embedding code
2. Pure LyX
  - *Pro:* Equation editor
  - *Pro:* Easy to use, but not common
  - *Con:* Very clunky.
  - *Con:* Subject to 
3. IPython/Jupyter notebooks
  - *Pro:* Interactively runs code
  - *Pro:* github will render it
  - *Pro:* Can output to PDF with embedded markdown
  - *Con:* Meant for code, no control over what gets rendered
  - *Con* Only one language at a time
  - *Con:* Subject to becoming obsolete
4. org-mode:
  - *Pro:* It can do everything I want and more
  - *Pro:* Plain text; Emacs will never be obsolete
  - *Con:* Only emacs users use it, inaccessible to new users
  - *Con:* It's an abomination, but in a good way
  - *Con:* Setting up interactive code can be finicky, but I was
    trying to do too much

# On org-mode

My last paper, ["Numerical experiments on the convergence properties of state-based peridynamic laws and influence functions in two-dimensional problems"](http://www.sciencedirect.com/science/article/pii/S0045782516311598), was writen in a combo of LyX, LaTeX, org-mode, and a
build script, across two git repos :eyerollemoji:. It was an
abomination. The paper would load the databases my results were stored
in, do the post processing using embedded python code, output figures
and plots, and embed the figures and plots into the final pdf. 

Org-mode enables you to embed sections like this
```
#+NAME: tbl:fbased_conv
#+BEGIN_SRC ipython :session mysession :results output raw :exports results
    print "|$w(r)$|",
    for n in problems: print n,"|",
    print '\n|-|'
    for w in weights:
        print "| "+w+" | ",
        for n,db in problems.iteritems():
          print "{0:1.4f}|".format(order('Fbased_strain',1.5,w,db[0])),
        print ''
#+END_SRC
#+LABEL: tbl:fbased_conv 
#+CAPTION: Order of convergence for the deformation gradient based model with $RF=1.5$ using each influence function.
#+ATTR_LATEX: 
#+RESULTS: tbl:fbased_conv
| $w(r)$ | Uniaxial |  Shear | Isotropic |
|--------+----------+--------+-----------|
| const  |   0.9860 | 0.9704 |    1.0005 |
| inv    |   0.9939 | 0.9247 |    0.9999 |
| linear |   0.9991 | 1.0370 |    0.9996 |
| quadr  |   0.9999 | 1.0192 |    0.9999 |
| cubic  |   0.9999 | 1.0166 |    0.9999 |
```
directly into the document. The session can be persistent between code
blocks, letting you define global variables and functions throughout
the document for code reuse. The `#+RESULTS` section is the result of
the calculation, which spits out the table in very clean org-mode
syntax. That will then get converted to LaTeX or HTML when you publish
the file. The `:exports results` tag 
says to ommit the actaul source block when I publish it (this is one
major feature that is missing from Jupyter notebooks that prevents
them from being used for actual documents.) 

I stopped using the `ipython` environment, and switched to just
"python" for the embedded code blocks.

# What I'm trying right now

Currently I am back to pure LaTeX because I am collaborating with
multiple different authors on this latest batch of papers. However,
with this site I'm trying something new. I'm looking for a new format
to live in a more web-facing ecosystem. I'm trying to put intermediate
stuff on github directly. 

I'm trying to get org-mode to render into Jekyll, but I can't get any
of the Jekyll plugins to work. I'll have to rely on a build script.

I also experimented with writing posts in Jupyter notebooks. The
[hessian_mnist]({{/tensorflow/2017/12/28/hessian-mnist.html}}) post is
an example of this. This also needs a build script to convert the
notebook into a Jekyll-friendly markdown format. I modified some I
found on the internet and included it in this site's repository: [https://github.com/afqueiruga/afqueiruga.github.io/tree/master/scripts/jupyterconverter](https://github.com/afqueiruga/afqueiruga.github.io/tree/master/scripts/jupyterconverter)

# Maths in Jekyll

Typesetting math is the most important requirement. I need the system
to be able to typeset equations like
\begin{equation}
\int_\Omega \nabla \delta \mathbf{u} : \nabla \mathbf{u} \mathrm{d}^3x
\end{equation}
in a way that will be parsed and rendered properly in both print and
the web page, without any editting. pandoc's markdown engine will
handle embedded LaTeX properly. The above source is just
```latex
\begin{equation}
\int_\Omega \nabla \delta \mathbf{u} : \nabla \mathbf{u} \mathrm{d}^3x
\end{equation}
```
The syntax hylighting in emacs got confused, but that's a different issue.

I got the equations to show up after building with Jekyll using
MathJax. It just requires modifying the head code, though there isn't
an easy way to insert new code into the template. Instead, you have to
copy the entire template, `_includes/head.html`, from
`vendor/bundle/ruby/2.4.0/gems/minima-2.1.1/` into your site's root
directory. Then, I put 
```html
<script type="text/javascript"
    src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'],
      inlineMath: [['$','$']]
    }
  });
</script>
```
between the `head` tags in `head.html`. The inline modification lets
me write the standard commands like `\$\alpha\$` embedded in the text,
$\alpha$. Dollar signs in the code blocks are now an issue, but
fortunately I don't program in any languages that use them. Note the
'http**s**'; github.io won't load the script over http.

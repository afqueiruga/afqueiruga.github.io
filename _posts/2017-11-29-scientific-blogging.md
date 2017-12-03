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

# History

I've tried tons of different work flows over the years:

1. Pure LaTeX
  - *Pro:* Lowest common denominater
  - *Pro:* Online editors like overleaf
  - *Pro:* A lot of control over layout
  - *Con:* The markup language is ugly, and too much control
  - *Con:* Looks ugly when it turns into html
2. Pure LyX
  - *Pro:* Equation editor
  - *Con:* Everything else
3. IPython/Jupyter notebooks
  - *Pro:* Interactively runs code,
  - *Pro:* github will render it.
  - *Con:* No control over what gets rendered when it
   turns into a document.
 4. org-mode:
   - *Con:* Only emacs users use it.
  - *Con:* It's an abomination.

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

# What I'm looking for now

Currently I am back to pure LaTeX because I am collaborating with
multiple different authors on this latest batch of papers. However, I
still find my self

Presently, I'm looking for a new format to live in a more web-facing
ecosystem. 

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
    src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
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
fortunately I don't program in any languages that use them.

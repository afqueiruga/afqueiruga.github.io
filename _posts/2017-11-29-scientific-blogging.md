---
layout: post
title:  "New Workflow Scientific Blogging"
date:   2017-11-28 22:30:22 -0800
categories: workflow
---

# Goal

# History

# Maths

$$\int_\Omega \mathrm{d}^3x$$

copied `_includes/head.html` and put
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
between the `head` tags.

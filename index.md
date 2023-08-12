---
layout: page
title: About
permalink: /
---
<video id="myVideo" src="assets/full_screen_animation_iPhone12.mp4"  muted autoplay playsInline style="width: 100%; position: fixed; top: 0; left: 0;">
</video>
<script>
var video = document.getElementById("myVideo");
video.addEventListener("ended", function() {
  video.style.display = "none";
});
document.addEventListener("DOMContentLoaded", function() {
  video.playbackRate = 3.0;
  video.play();
});
</script>>


<img align="center" src="about/images/mug2018.jpeg" width="250" style="margin:25px 25px">

I'm a software engineer and researcher in computational methods.  I'm currently at Google, where I work on ML quality and infrastructure for serving ads on the Discover Feed (those recommended sites below the search bar.)

<!--bard
My research interests lie in the intersection of machine learning, scientific properties, and deep learning settings. I am particularly interested in studying how machine learning can be used to learn and understand scientific properties, and how these insights can be applied to solve scientific problems and improve deep learning models.
-->
My research interests lie in the intersection of machine learning and scientific settings. I am particularly interested in studying and correcting failure models in applying ML to scientific problems and developing robust validation methods.

The pageload animation is the Stable Diffusion inpainting process. The first frame is the initial random image, and each frame is one step of denoising towards the top-of-fold rendering. (The animation looks best on mobile.)

The site icon is a heatmap of an ML weight matrix learning the 1D possion equation. You can see an explantion on my [research](research) page.

<!-- 
I research the quirks and failure modes of applying ML to scientific problems, to developing rigorous verification methods. And, applying the numerical methods to DL problems. -->

<!-- Bard:
I study the limitations and pitfalls of using machine learning (ML) to solve scientific problems, and I develop rigorous methods to verify the accuracy and reliability of ML models. I also apply numerical methods to deep learning (DL) problems. -->
<!-- 
My research interests are applying ML to scientific problems, and developing verification methods. -->

<!-- I got into machine learning after spending my early career working on theory and numerical simulation. I once spent a year writing a giant automatic code generation and differentation library just to exhaustively *disprove* a theory with a literature backing. Now, I work on  -->

<!-- I used to think I was pretty good at deriving equations and writing programs, but now I think my computer can do a better job at both of those things. Metaprogramming methods have proved invaluable for empirical studies; [cornflakes](https://github.com/afqueiruga/cornflakes) and [popcorn](https://github.com/afqueiruga/popcorn) are a general-purpose runtime and symbolic generation package. The benchmarking and verification solutions I've compiled over the years have spun out into an automated test suite, [detest](https://github.com/afqueiruga/detest). Lately, I have been working on machine learning and differential programming methods to seek new ways of describing and solving physical systems. -->

Some of my active work can be found on Github and in my hosted [presentations](https://afqueiruga.github.io/CV).
There are links to as many of my publications as possible on the CV page of this site. Conference presentations also have links to the recordings or slides. You can also find different things I work on around the internet:  
[google scholar](https://scholar.google.com/citations?user=5lV0WOgAAAAJ&hl=en&oi=ao)  
[<i class="fa fa-github"></i > afqueiruga](https://github.com/afqueiruga) Research codes  
[<i class="fa fa-instagram"></i > goblinfightsraccoon](https://www.instagram.com/goblinfightsraccoon) Art  
[<i class="fa fa-reddit"></i > drgobble](https://www.reddit.com/user/drgobble/submitted/) Keyboard builds  

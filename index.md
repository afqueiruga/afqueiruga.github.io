---
layout: page
title: About
permalink: /
---
<video id="myVideo" muted autoplay playsInline style="width: 100%; height:100%; position: fixed; top: 0; left: 0; object-fit: fill;">
<source src="assets/full_screen_animation_iPhone12.mp4"  type="video/mp4"  media="(max-width: 768px)" />
<source src="assets/full_screen_animation_desktop_1280p.mp4"  type="video/mp4" />
</video>

<script>
var video = document.getElementById("myVideo");
video.addEventListener("ended", function() {
  video.style.display = "none";
});
document.addEventListener("scroll", function() {
  video.style.display = "none";
});
document.addEventListener("DOMContentLoaded", function() {
  video.playbackRate = 3.0;
  video.play();
});
</script>


<img align="center" src="about/images/mug2018.jpeg" width="250" style="margin:25px 25px">

I'm a machine learning engineer and researcher, working on computational methods broadly.
I'm currently at Google, where I TL AI-powered Retail Ads, optimizing product ad copy using LLMs on Search, and designing new monetization strategies for LLM-driven experiences.
I formerly worked on ML quality and infrastructure for serving ads on the Discover Feed (those recommended sites below the search bar.)

My research interests lie in the intersection of machine learning and scientific settings. I am particularly interested in studying and correcting failure models in applying ML to scientific problems and developing robust validation methods.

The pageload animation is the Stable Diffusion in-painting process. The first frame is the initial random image, and each frame is one step of denoising towards a top-of-fold screenshot. It's just a pre-rendered video with two variations for mobile and desktop. [Inspect it here.](assets/full_screen_animation_iPhone12.mp4)

The site icon is a heatmap of an ML weight matrix learning the 1D Poisson equation. You can see an explanation on my [research](research) page.

Some of my active work can be found on Github and in my hosted [presentations](https://afqueiruga.github.io/cv).
There are links to as many of my publications as possible on the CV page of this site. Conference presentations also have links to the recordings or slides. You can also find different things I work on around the internet:  

[google scholar](https://scholar.google.com/citations?user=5lV0WOgAAAAJ&hl=en&oi=ao) Papers  
[<i class="fa fa-linkedin"></i > afqueiruga](https://www.linkedin.com/in/afqueiruga/) LinkedIn  
[<i class="fa fa-github"></i > afqueiruga](https://github.com/afqueiruga) Research codes  
[<i class="fa fa-instagram"></i > goblinfightsraccoon](https://www.instagram.com/goblinfightsraccoon) Art  
[<i class="fa fa-reddit"></i > drgobble](https://www.reddit.com/user/drgobble/submitted/) Keyboard builds  

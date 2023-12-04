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
document.addEventListener("scroll", function() {
  video.style.display = "none";
});
document.addEventListener("DOMContentLoaded", function() {
  video.playbackRate = 3.0;
  video.play();
});
</script>>


<img align="center" src="about/images/mug2018.jpeg" width="250" style="margin:25px 25px">

I'm a software engineer and researcher in computational methods.  I'm currently at Google, where I work on ML quality and infrastructure for serving ads on the Discover Feed (those recommended sites below the search bar.)

My research interests lie in the intersection of machine learning and scientific settings. I am particularly interested in studying and correcting failure models in applying ML to scientific problems and developing robust validation methods.

The pageload animation is the Stable Diffusion inpainting process. The first frame is the initial random image, and each frame is one step of denoising towards the top-of-fold rendering. (The animation looks best on mobile.) [Inspect it here.](assets/full_screen_animation_iPhone12.mp4)

The site icon is a heatmap of an ML weight matrix learning the 1D Poisson equation. You can see an explanation on my [research](research) page.

Some of my active work can be found on Github and in my hosted [presentations](https://afqueiruga.github.io/cv).
There are links to as many of my publications as possible on the CV page of this site. Conference presentations also have links to the recordings or slides. You can also find different things I work on around the internet:  
[google scholar](https://scholar.google.com/citations?user=5lV0WOgAAAAJ&hl=en&oi=ao) Papers  
[<i class="fa fa-github"></i > afqueiruga](https://github.com/afqueiruga) Research codes  
[<i class="fa fa-instagram"></i > goblinfightsraccoon](https://www.instagram.com/goblinfightsraccoon) Art  
[<i class="fa fa-reddit"></i > drgobble](https://www.reddit.com/user/drgobble/submitted/) Keyboard builds  
